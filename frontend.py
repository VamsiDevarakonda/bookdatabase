
from tkinter import *
import tkinter as tk
import backend

def view_text():
    list1.delete(0, END)
    for rows in backend.view():
        list1.insert(END,rows)
def insert_text():
    backend.insert(id_book.get(),isbn_book.get(),author_book.get(),title_book.get())
def update_text():
    backend.update(isbn_book.get(),author_book.get(),title_book.get(),id_book.get())
def search_text():
    list1.delete(0,END)
    for rows in backend.search(isbn_book.get(),author_book.get(),title_book.get()):
        list1.insert(END,rows)
def delete_text():
    backend.delete(id_book.get())



window=tk.Tk()
window.title("BOOK DATA BASE")
window.configure(bg="gray")
#lable
l0=Label(window,text="Details Entry",fg="blue")
l1=Label(window,text="Id",fg="green")
l2=Label(window,text="Title",fg="orange")
l3=Label(window,text="Author",fg="red")
l4=Label(window,text="ISBN",fg="purple")

#entry
id_book=StringVar()
e0=Entry(window,textvariable=id_book)
isbn_book=StringVar()
e1=Entry(window,textvariable=isbn_book)
author_book=StringVar()
e2=Entry(window,textvariable=author_book)
title_book=StringVar()
e3=Entry(window,textvariable=title_book)
#id_book=StringVar()
#e4=Entry(window,textvariable=id_book)


#buttons
b0=Button(window,text="insert",command=insert_text)
b1=Button(window,text="update",command=update_text)
b2=Button(window,text="view all",command=view_text)
b3=Button(window,text="delete",command=delete_text)
b4=Button(window,text="search",command=search_text)

#list
#list1=Listbox(window,height=10,width=40)
#s1=Scrollbar(window)
list1=Listbox(window,height=5,width=50,bg="violet",fg="dark blue",font="Italic")
list1.grid(row=7,column=0,rowspan=5,columnspan=5)
sb=Scrollbar(window)
sb.grid(row=7,column=5,rowspan=12)
list1.configure(yscrollcommand=sb.set)
sb.configure(command=list1.yview)


#grid
l0.grid(row=0,column=2)
l1.grid(row=1,column=0)
l2.grid(row=2,column=0)
l3.grid(row=3,column=0)
l4.grid(row=4,column=0)
e0.grid(row=1,column=1)
e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
e3.grid(row=4,column=1)
#e4.grid(row=4,column=2)
b0.grid(row=0,column=4)
b1.grid(row=1,column=4)
b2.grid(row=2,column=4)
b3.grid(row=3,column=4)
b4.grid(row=4,column=4)
#list1.grid(row=6,column=2)
#s1.grid(row=6,column=3)
window.mainloop() 
