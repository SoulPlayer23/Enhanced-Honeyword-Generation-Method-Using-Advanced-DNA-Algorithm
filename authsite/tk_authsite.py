from cgitb import text
from tkinter import *
import os

def delete3():
    screen3.destroy()

def delete4():
    screen4.destroy()

def delete5():
    screen5.destroy()

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
    screen5.title("Password not found")
    screen5.geometry("150x100")
    Label(screen5, text="User not found").pack()
    Button(screen5, text="OK", command = delete5).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

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

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognised()
    else:
        user_not_found()

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