from tkinter import *
from pyshorteners import *
master=Tk()
master.title("Url Shortner")

input_url=Shortener()

def shorten():
    long=url.get()
    shortened=input_url.tinyurl.short(long)
    short_url.insert(0,shortened)
def delete1():
    url.delete(0,END)
    short_url.delete(0,END)

label1=Label(master,text="Welcome To URL Shortner  ",font=("Helvetica",20,"bold"))
label2=Label(master,text="Enter your Url Here :-",font=("roboto",14))
url=Entry(master)
label3=Label(master,text="Get your TinyURL Here :-",font=("roboto",14))
short_url=Entry(master)
button1=Button(master,text="Generate URL",command=shorten,padx=20,pady=5)
button2=Button(master,text="Clear",command=delete1,padx=50,pady=5)
button3=Button(master,text="Exit",command=master.quit,padx=46,pady=5)
label4=Label(master,text="Software Designed By Suneet Verma",font=("roboto",8,"italic"))



label1.grid(row=0,column=0,columnspan=3)
label2.grid(row=1,column=0)
url.grid(row=1,column=1,ipadx=20,ipady=10)
label3.grid(row=2,column=0)
short_url.grid(row=2,column=1,ipadx=20,ipady=10)
button1.grid(row=3,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=0)
label4.grid(row=5,column=0,columnspan=2)

master.mainloop()