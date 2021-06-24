from tkinter import *
import sqlite3


root = Tk()
root.title("PhoneBook")
root.config(bg="light yellow")

conn = sqlite3.connect("mysq.db")
c = conn.cursor()
c.execute('create table if not exists contacts(Name Text , C_Name int[10])')
conn.commit()


def show():
    conn = sqlite3.connect("mysq.db")
    c = conn.cursor()
    c.execute('select * from contacts')
    for i in c.fetchall():
        print(i)

    print("********************")
    conn.close()


def add():
    c_name = e1.get()
    c_num = e2.get()
    conn = sqlite3.connect("mysq.db")
    c = conn.cursor()
    c.execute("insert into contacts values('{}','{}')".format(c_name, c_num))
    print('contact added successfully \n********************')
    conn.commit()
    e1.delete(0, END)
    e2.delete(0, END)


def delete():
    c_name = e1.get()
    conn = sqlite3.connect("mysq.db")
    c = conn.cursor()
    c.execute("delete from contacts where Name is '{}'".format(c_name))
    print("contact deleted successfully \n********************")
    conn.commit()
    conn.close()
    e1.delete(0, END)
    e2.delete(0, END)


def search():
    c_name = e1.get()
    conn = sqlite3.connect("mysq.db")
    c = conn.cursor()
    c.execute("select * from contacts where Name is '{}'".format(c_name))
    print(c.fetchall())
    print('********************')
    conn.close()
    e1.delete(0, END)
    e2.delete(0, END)


def about():
    print("Created by : Rohan Mule \nCreated on : Python using tkinter \n********************")


l1 = Label(root, text="Contact Name:")
l1.grid(row=0, column=1)
l2 = Label(root, text="Number:")
l2.grid(row=2, column=1)

e1 = Entry(root, width=30, bd=3, bg="gray80")
e1.grid(row=0, column=2)
e2 = Entry(root, width=30, bd=3, bg="gray80")
e2.grid(row=2, column=2)

b1 = Button(root, text="Search", bd=3, bg="RoyalBlue1", width=20, command=search)
b1.grid(row=3, column=1)
b2 = Button(root, text="Add", bd=3, bg="RoyalBlue1", width=20, command=add)
b2.grid(row=3, column=2)
b3 = Button(root, text="Show all contacts", bd=3, bg="RoyalBlue1", width=20, command=show)
b3.grid(row=4, column=1)
b4 = Button(root, text="Quit", bd=3, bg="RoyalBlue1", command=root.quit, width=20)
b4.grid(row=5, column=2)
b5 = Button(root, text="Delete", bd=3, bg="RoyalBlue1", width=20, command=delete)
b5.grid(row=4, column=2)
b6 = Button(root, text="About", bd=3, bg="RoyalBlue1", width=20, command=about)
b6.grid(row=5, column=1)

conn.commit()
c.close()
root.mainloop()
