from tkinter import *
from tkinter import ttk
import requests
def data_get():
 city=city_name.get()
 data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7e848cde2ca4518957e17f9d1b66a88f").json()
 w_label1.config(text=data["weather"][0]["main"])
 wb_label1.config(text=data["weather"][0]["description"])
 t_label1.config(text=str(int(data["main"]["temp"]-273.15)))
 m_label1.config(text=data["main"]["temp_min"])
 tk_label1.config(text=data["main"]["temp_max"])
 tm_label1.config(text=data["main"]["pressure"])
 tmk_label1.config(text=str(int(data["sys"]["sunset"]-1.666668e-5)))
win = Tk()
win.title("Weather App")
win.config(bg="grey")
win.geometry("900x900")
name_label = Label(win,text="Checking Weather", bg="tan",font=("lucida calligraphy",20,"bold"))
name_label.place(x=25,y=50,height=50,width=450)
list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name = StringVar()
com=ttk.Combobox(win,text="Checking Weather", values=list_name,font=("lucida calligraphy",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)
w_label=Label(win,text="weather climate : ",bg="grey",font=("lucida calligraphy",10,"bold"))
w_label.place(y=270,height=50,width=200,x=30)
w_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
w_label1.place(y=270,height=50,width=200,x=210)
wb_label=Label(win,text="Weather Description : ",bg="grey",font=("lucida calligraphy",10,"bold"))
wb_label.place(y=330,height=30,width=200,x=30)
wb_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
wb_label1.place(y=330,height=30,width=200,x=220)
t_label=Label(win,text="Temprature : ",bg="grey",font=("lucida calligraphy",10,"bold"))
t_label.place(y=390,height=30,width=200,x=30)
t_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
t_label1.place(y=390,height=30,width=200,x=210)
m_label=Label(win,text="Min Weather : ",bg="grey",font=("lucida calligraphy",10,"bold"))
m_label.place(y=450,height=30,width=200,x=30)
m_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
m_label1.place(y=450,height=30,width=200,x=210)
tk_label=Label(win,text="Max Weather : ",bg="grey",font=("lucida calligraphy",10,"bold"))
tk_label.place(y=510,height=30,width=200,x=30)
tk_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
tk_label1.place(y=510,height=30,width=200,x=210)
tm_label=Label(win,text="Presaure : ",bg="grey",font=("lucida calligraphy",10,"bold"))
tm_label.place(y=570,height=30,width=200,x=30)
tm_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
tm_label1.place(y=570,height=30,width=200,x=210)
tmk_label=Label(win,text="Sunset : ",bg="grey",font=("lucida calligraphy",10,"bold"))
tmk_label.place(y=630,height=30,width=200,x=30)
tmk_label1=Label(win,text="",bg="grey",font=("lucida calligraphy",10,"bold"))
tmk_label1.place(y=630,height=30,width=200,x=210)
click = Button(win,text="click", bg="blue",font=("lucida calligraphy",20,"bold"),command=data_get)
click.place(y=190,height=50,width=100,x=200)
win.mainloop()