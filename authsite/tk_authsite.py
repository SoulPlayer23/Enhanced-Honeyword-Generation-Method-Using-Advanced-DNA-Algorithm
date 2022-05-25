from tkinter import *
import os

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

def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Success").pack()
    Button(screen3, text="OK", command = delete3).pack()

def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Password not found")
    screen4.geometry("150x100")
    Label(screen4, text="Password not found").pack()
    Button(screen4, text="OK", command = delete4).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("User not found")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command = delete5).pack()

def wrong_password():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Wrong Password")
    screen6.geometry("150x100")
    Label(screen6, text="Wrong Password").pack()
    Button(screen6, text="OK", command = delete6).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    credentials.username, credentials.password = username_info, password_info

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success").pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1["bg"] = "#7abecc"
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password

    username = StringVar()
    password = StringVar()

    global username_entry
    global password_entry

    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text="Register", height="2", width="15", command=register_user).pack()

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
    screen2.geometry("300x250")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()

    Button(screen2, text="Login", height="2", width="15", command=login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen["bg"] = "#7abecc"
    screen.geometry("500x500")
    screen.title("Authsite")
    Label(text="Main Page", bg="#74cfbf", font=("Calibri", 12)).pack()
    Button(text="Login", height="2", width="15", command=login).pack()
    Button(text="Register", height="2", width="15", command=register).pack()

    screen.mainloop()

main_screen()