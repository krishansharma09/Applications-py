from tkinter import *
import random
Root=Tk()
Root.geometry('900x900')
Root.title("Love Calculater...!")
Root.config(bg="aqua")

#Crating Function From Random Number Import...!
def Calculate_Love():
    st='123456789'
    digit=2
    temp=" ".join(random.sample(st,digit))
    result.config(text=temp)

#Heading On Top 
heading=Label(Root,text="Love Calculater-How Much is He/She into You:",bg="Red",font=("bold italic",10,"bold"))
heading.place(x=25,y=20,height=50,width=450)
# heading.pack()

#input From The User ...
slot1=Label(Root,text="Enter Your Name..",bg="green",font=("lucida calligraphy",10,"bold"))
slot1.place(x=25,y=120,height=50,width=450)
# slot1.pack()
Name1=Entry(Root,border=5)
Name1.place(x=25,y=200,height=50,width=450)

# Input Your Partner Name...!
slot2=Label(Root,text="Enter Your Partner Name..!",bg="green",font=("lucida calligraphy",10,"bold"))
slot2.place(x=25,y=300,height=50,width=450)
Name2=Entry(Root,border=5)
Name2.place(x=25,y=380,height=50,width=450)

#Creating Button From Output...!
btn=Button(Root,text="Calculate",height=1,width=7,command=Calculate_Love,bg="Blue",font=("bold italic",15,"bold"))
btn.place(x=25,y=480,height=50,width=450)

result = Label(Root,text="Love Parcentage Between Both OF You..",bg="green",font=("lucida calligraphy",10,"bold"))
result.place(x=25,y=580,height=50,width=450)

Root.mainloop()
