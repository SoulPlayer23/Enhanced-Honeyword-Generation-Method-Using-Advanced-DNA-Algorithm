from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login") #window title
        self.root.geometry("1199x600+300+200") #aspect ratio and position
        self.root.resizable("False", "False")
        
        #Login frame
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=330, y=100, width=500, height=400)

        #Title
        title = Label(Frame_login, text="Login", font=("Impact", 35, "bold"), fg="#6162FF", bg="white").place(x=90, y=30)
        
        #Username
        acc_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey",  bg="white").place(x=90, y=140)
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")
        self.username.place(x=90, y=170, width=320, height=35)

        #Password
        acc_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey",  bg="white").place(x=90, y=210)
        self.password = Entry(Frame_login, font=("Goudy old style", 15), show="*", bg="#E7E6E6")
        self.password.place(x=90, y=240, width=320, height=35)

        #Button
        forgot = Button(Frame_login, text="forgot password?", cursor="hand2", bd=0, font=("Goudy old style", 12), fg="#6162FF", bg="white").place(x=90, y=280)
        login = Button(Frame_login, command= self.check_funtion, text="Login", cursor="hand2", bd=1, font=("Goudy old style", 15), bg="#6162FF", fg="white").place(x=90, y=320, width=180, height=40)

    def check_funtion(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get() != "username" or self.password.get() != "password":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")

root  = Tk()
obj = Login(root)
root.mainloop()    