from tkinter import *
from datetime import date

root=Tk()
root.title('Getting started with widgets')
root.geometry('400x300')
root.mainloop()
lbl=Label(text="hey there!",fg='white',bg="#072f5f",height=1,width=3000)
name_lbl=Label(text="full name",bg="#3895D3")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcome to the application!\ntoday's date is :"
    greet="Hello"+name+"\n"
    text_box.insert(END.greet)
    text_box.insert(END.message)
    text_box.insert(END.date.today())
text_box=Text(height=3) 
bln=Button(text="bigen",command=display,height=1,bg="#1261A0",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
bln.pack()
text_box.pack()
