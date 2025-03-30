import streamlit as st
import os
import fitz 
import docx
import numpy as np
import faiss
import psycopg2
import google.generativeai as genai
from langchain.text_splitter import RecursiveCharacterTextSplitter
from serpapi.google_search import GoogleSearch
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY_1") # Replace with your Gemini API key
SERPAPI_KEY = os.getenv("SERP_API_KEY") # Replace with your SerpAPI key

genai.configure(api_key=API_KEY)
embedding_model = "models/embedding-001"

st.set_page_config(page_title="Gemini RAG Chatbot")
st.title(" Gemini RAG-based Chatbot")

if "document_chunks" not in st.session_state:
    st.session_state.document_chunks = []
if "faiss_index" not in st.session_state:
    st.session_state.faiss_index = None
if "stored_embeddings" not in st.session_state:
    st.session_state.stored_embeddings = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False 

def get_db_connection():
    return psycopg2.connect(
        host="localhost", port=5432, user="postgres", dbname="Chat_Bot_Agent", password="kanha"
    )

def extract_product_name(query):
    keywords_to_remove = ["what is the price of", "tell me the price of", "how much is", "cost of", "price of", "how much does"]
    cleaned_query = query.lower().strip()
    for phrase in keywords_to_remove:
        cleaned_query = cleaned_query.replace(phrase, "").strip()
    return "".join([c for c in cleaned_query if c.isalnum() or c.isspace()]).strip()

def get_db_data(query):
    try:
        product_name = extract_product_name(query)
        if not product_name:
            return None
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, price FROM productdata WHERE LOWER(name) = LOWER(%s) LIMIT 5;", (product_name,))
                exact_match = cur.fetchall()
                if exact_match:
                    return exact_match
                cur.execute("SELECT name, price FROM productdata WHERE LOWER(name) LIKE %s LIMIT 5;", (f"%{product_name}%",))
                return cur.fetchall()
    except Exception:
        return None

def extract_text(file):
    try:
        if file.name.endswith(".txt"):
            return file.getvalue().decode("utf-8")
        elif file.name.endswith(".pdf"):
            return "\n".join([page.get_text() for page in fitz.open(stream=file.read(), filetype="pdf")])
        elif file.name.endswith(".docx"):
            return "\n".join([para.text for para in docx.Document(file).paragraphs])
    except Exception:
        return ""
    return ""

def split_text(text, chunk_size=1000, chunk_overlap=100):
    return RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap).split_text(text)

def get_embedding(text):
    try:
        response = genai.embed_content(model=embedding_model, content=text, task_type="retrieval_document")
        return np.array(response["embedding"], dtype=np.float32)
    except Exception:
        return None

def store_embeddings(chunks):
    embeddings = [get_embedding(chunk) for chunk in chunks if get_embedding(chunk) is not None]
    if embeddings:
        faiss_index = faiss.IndexFlatL2(len(embeddings[0]))
        faiss_index.add(np.array(embeddings))
        st.session_state.faiss_index = faiss_index
        st.session_state.stored_embeddings = list(zip(chunks, embeddings))

uploaded_file = st.file_uploader("Upload Document", type=["pdf", "txt", "docx"])
if uploaded_file:
    text = extract_text(uploaded_file)
    if "Error" in text:
        st.error(text)
    else:
        chunks = split_text(text)
        store_embeddings(chunks)
        st.session_state.document_chunks = chunks  
        st.session_state.document_uploaded = True 
        st.success("Document Uploaded successfully!")

if st.button("Remove Document"): 
    st.session_state.document_chunks = []
    st.session_state.faiss_index = None
    st.session_state.stored_embeddings = []
    st.session_state.document_uploaded = False 
    st.success("🚀 Document removed successfully!")

def retrieve_relevant_chunks(query, top_k=3):
    if not st.session_state.document_uploaded or st.session_state.faiss_index is None:
        return []
    query_embedding = get_embedding(query)
    if query_embedding is None:
        return []
    D, I = st.session_state.faiss_index.search(np.array([query_embedding]), top_k)
    return [st.session_state.stored_embeddings[i][0] for i in I[0] if i != -1]

def generate_answer(query, context):
    if not context:
        return "No relevant information found in the document."
    model = genai.GenerativeModel("gemini-1.5-flash-latest")
    prompt = f"""
    Use the following document excerpts to answer the question.
    DOCUMENT EXCERPTS:
    {context}
    **User's Question:** {query}
    Provide a clear and relevant answer based only on the document.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Error generating response."

def search_serpapi(query):
    try:
        search = GoogleSearch({"q": query, "api_key": SERPAPI_KEY})
        results = search.get_dict().get("organic_results", [])
        extracted_content = []
        for res in results[:10]:
            title = res.get("title", "No Title")
            snippet = res.get("snippet", "")
            link = res.get("link", "")
            if snippet:
                extracted_content.append(f"🔹 **{title}**\n{snippet}\n🔗 [Read more]({link})\n")
        return "\n\n".join(extracted_content) if extracted_content else "I couldn't find any relevant information."
    except Exception as e:
        return f"Error fetching results: {e}"

user_question = st.text_input("Ask a question:")
st.subheader("Chat History")
for role, text in st.session_state.chat_history:
    st.markdown(f"**{role}:** {text}")

if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared!")

if user_question:
    response = None
    db_data = get_db_data(user_question)
    
    if db_data:
        response = "\n".join([f"🔹 **{row[0]}** -  Price: ₹{row[1]}" for row in db_data])
    
    elif st.session_state.document_uploaded: 
        relevant_chunks = retrieve_relevant_chunks(user_question, top_k=3)
        response = generate_answer(user_question, "\n\n".join(relevant_chunks)) if relevant_chunks else None

    if not response: 
        response = search_serpapi(user_question)

    st.session_state.chat_history.append(("You", user_question))
    st.session_state.chat_history.append((" AI", response))
    st.subheader(" AI Response:")
    st.write(response)


