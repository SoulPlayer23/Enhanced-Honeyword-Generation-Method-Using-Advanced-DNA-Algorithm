import imp
from tkinter import *
import os
from tkinter import messagebox
import re

import honeychecker as h 



class credentials:

    def __init__(self):
        self.username = None
        self.password = None

class login_credentials:

    def __init__(self):
        self.username = None
        self.password = None        

def delete3():
    screen3.destroy()

def delete4():
    screen4.destroy()

def delete5():
    screen5.destroy()

def delete6():
    screen6.destroy()

def delete7():
    screen7.destroy()

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.configure(bg='#fff')
    screen3.geometry("300x300+800+350")
    screen3.resizable(False, False)
    Label(screen3, text="Login Success", fg='#74cfbf', bg='white', font=("Calibri", 20, "bold")).pack()
    Button(screen3, text="OK", height="2", width="15", pady=5, bg='#74cfbf', fg='white', border=0, command = delete3).pack()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.configure(bg='#fff')
    screen4.geometry("300x300+800+350")
    screen4.resizable(False, False)
    Label(screen4, text="Password not found", fg='#E97451', bg='white', font=("Calibri", 20, "bold")).pack()
    Button(screen4, text="OK", height="2", width="15", pady=5, bg='#74cfbf', fg='white', border=0, command = delete4).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.configure(bg='#fff')
    screen5.geometry("300x300+800+350")
    screen5.resizable(False, False)
    Label(screen5, text="User not found", fg='#E97451', bg='white', font=("Calibri", 20, "bold")).pack()
    Button(screen5, text="OK", height="2", width="15", pady=5, bg='#74cfbf', fg='white', border=0, command = delete5).pack()

def wrong_password():
    global screen6
    screen6 = Toplevel(screen)
    screen6.configure(bg='#fff')
    screen6.geometry("300x300+800+350")
    screen6.resizable(False, False)
    Label(screen6, text="Wrong Password", fg='#E97451', bg='white', font=("Calibri", 20, "bold")).pack()
    Button(screen6, text="OK", height="2", width="15", pady=5, bg='#74cfbf', fg='white', border=0, command = delete6).pack()

def register_user():
    global screen7
    screen7 = Toplevel(screen)
    screen7.configure(bg='#fff')
    screen7.geometry("300x300+800+350")
    screen7.resizable(False, False)

    username_info = username.get()
    password_info = password.get()

    txt = 'Weak Password'

    if len(password_info) > 5:
   
        # checks for occurrence of a character 
        # three or more times in a row
        if re.search(r'(.)\1\1', password_info) :
            txt = 'Weak Password'

        # checks for occurrence of same string 
        # pattern( minimum of two character length)
        # repeating
        if re.search(r'(..)(.*?)\1', password_info):
            txt = 'Weak Password'

        else:
            txt = 'Strong Password'

    else:
        txt = 'Weak Password'

    credentials.username, credentials.password = username_info, password_info

    username_entry.delete(0, END)
    password_entry.delete(0, END)




    Label(screen7, text="Registration Success\n" + txt, fg='#74cfbf', bg='white', font=("Calibri", 20, "bold")).pack()
    Button(screen7, text="OK", height="2", width="15", pady=5, bg='#74cfbf', fg='white', border=0, command = delete7).pack()



def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.configure(bg='#fff')
    screen1.geometry("925x500+300+200")
    screen1.resizable(False, False)

    img = PhotoImage(file='authsite\login.png')
    Label(screen1, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(screen1, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text="Register", fg='#74cfbf', bg='white', font=("Calibri", 30, "bold"))
    heading.place(x=100, y=5)

    global username
    global password

    username = StringVar()
    password = StringVar()

    global username_entry
    global password_entry

    def on_enter(e):
        username_entry.delete(0, 'end')
    
    def on_enter_p(e):
        password_entry.delete(0, 'end')

    def on_leave(e):
        if username_entry.get()=='':
            username_entry.insert(0, 'Username')

    def on_leave_p(e):
        if password_entry.get()=='':
            password_entry.insert(0, 'Password')

    username_entry = Entry(frame, width = 25, border=0, fg='black', bg = 'white', font=("Calibri", 12), textvariable = username)
    username_entry.place(x=50, y=80)
    username_entry.insert(0, 'Username')
    username_entry.bind("<FocusIn>", on_enter)
    username_entry.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    password_entry = Entry(frame, width = 25, border=0, fg='black', bg = 'white', font=("Calibri", 12), textvariable = password)
    password_entry.place(x=50, y=130)
    password_entry.insert(0, 'Password')
    password_entry.bind("<FocusIn>", on_enter_p)
    password_entry.bind("<FocusOut>", on_leave_p)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)

    Button(frame, text="Register", height="2", width="40", pady=7, bg='#74cfbf', fg='white', border=0, command=register_user).place(x=30, y=170)

    screen1.mainloop()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    login_credentials.username, login_credentials.password = username1, password1
    h.honeychecker()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.configure(bg = '#fff')
    screen2.geometry("925x500+300+200")
    screen2.resizable(False, False)

    img = PhotoImage(file='authsite\login.png')
    Label(screen2, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(screen2, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text="Login", fg='#74cfbf', bg='white', font=("Calibri", 30, "bold"))
    heading.place(x=100, y=5)

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    def on_enter(e):
        username_entry1.delete(0, 'end')
    
    def on_enter_p(e):
        password_entry1.delete(0, 'end')

    def on_leave(e):
        if username_entry1.get()=='':
            username_entry1.insert(0, 'Username')

    def on_leave_p(e):
        if password_entry1.get()=='':
            password_entry1.insert(0, 'Password')

  
    username_entry1 = Entry(frame, width = 25, border=0, fg='black', bg = 'white', font=("Calibri", 12), textvariable = username_verify)
    username_entry1.place(x=50, y=80)
    username_entry1.insert(0, 'Username')
    username_entry1.bind("<FocusIn>", on_enter)
    username_entry1.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    password_entry1 = Entry(frame, width = 25, border=0, fg='black', bg = 'white', font=("Calibri", 12), textvariable = password_verify)
    password_entry1.place(x=50, y=130)
    password_entry1.insert(0, 'Password')
    password_entry1.bind("<FocusIn>", on_enter_p)
    password_entry1.bind("<FocusOut>", on_leave_p)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=157)

    Button(frame, text="Login", height="2", width="40", pady=7, bg='#74cfbf', fg='white', border=0, command=login_verify).place(x=30, y=170)

    screen2.mainloop()

def main_screen():
    global screen
    screen = Tk()
    screen.configure(bg = '#fff')
     #7abecc
    screen.geometry("925x500+300+200")
    screen.title("Authsite")
    screen.resizable(False, False)
    

    img = PhotoImage(file='authsite\login.png')
    Label(screen, image=img, border=0, bg='white').place(x=50, y=90)

    frame = Frame(screen, width=350, height=390, bg='#fff')
    frame.place(x=480, y=50)

    heading = Label(frame, text="Main Page", fg='#74cfbf', bg='white', font=("Calibri", 30, "bold"))
    heading.place(x=100, y=5)

    loginbtn = Button(frame, text="Login", height="2", width="40", pady=7, bg='#74cfbf', fg='white', border=0, command=login)
    registerbtn = Button(frame, text="Register", height="2", width="40", pady=7, bg='#74cfbf', fg='white', border=0, command=register)

    loginbtn.place(x=50, y=80)
    registerbtn.place(x=50, y=140)

    screen.mainloop()


main_screen()