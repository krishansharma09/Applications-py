# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode

# For Encoding
a=input("enter a string : ")
if len(a)<=2:
    a=a[::-1]
    print(a)
elif len(a)>2:
    add1=input("enter 3 alphabets to the start : ")
    add2=input("enter 3 alphabets to the end : ")
    modified=a[1:]+a[0]
    add=add1+modified+add2
    print(add)
    
# For decoding
b=input("enter the word to decode : ")
if len(b)<=2:
    b=b[::-1]
    print(b)
elif len(b)>2:
    modified1=b[3:-4]
    modified=modified1
    modified2=b[-4]
    modified=modified2+modified1
    print(modified)

# 2nd Way To Decode And Encode Your Program...!

st = input("Enter message")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
  nwords = []
  for word in words:
    if(len(word)>=3):
      r1 = "dsf"
      r2 = "jkr"
      stnew = r1+ word[1:] +  r2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])    #Covert reversed String
  print(" ".join(nwords))

else:
  nwords = []
  for word in words:
    if(len(word)>=3): 
      stnew = word[3:-3]
      stnew = stnew[-1] + stnew[:-1]   # End To First Element
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])          #Covert reversed String
  print(" ".join(nwords))

#Easy Way To Decode And Encode Your Program...!

str="Hello! Welcome to Tutorialspoint."
str_encoded= str.encode('utf_16','strict')
print("The encoded string is: ", str_encoded)
str_decoded=str_encoded.decode('utf_16', 'strict')
print("The decoded string is: ", str_decoded)
  

from encodings.aliases import aliases
 
# Printing list available
print("The available encodings are : ")
print(aliases.keys())
  