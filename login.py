import tkinter as tk
from tkinter.ttk import *
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox
import homepage
import admin

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


login = tk.Tk()
login.resizable(height = False, width = False)
login.title('Travel Management System')
login.geometry('720x420')
heading = tk.Label(login, text="Travel Management System", font=('Helvetica', '25'))
# register_head = tk.Label(login, text="Register here", bg='grey',font=('Helvetica', '20'))


background = tk.PhotoImage(file='Images/background.png')
description = tk.Label(login, text="\n\n\n\n\n\n")
background_label = tk.Label(login,  image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

login_head = tk.Label(login, text="Login here", font=('Helvetica', '20'))
login_head.place(x=550, y=75)
login_head.configure(bg=_from_rgb((133, 237, 157)))

email = tk.Label(login, text="Enter Email Id:")
email.place(x=510, y=130)
email.configure(bg=_from_rgb((133, 237, 157)))

password = tk.Label(login, text="Enter Password:")
password.place(x=510, y=160)
password.configure(bg=_from_rgb((133, 237, 157)))

email_entry = tk.Entry(login, width=15)
password_entry = tk.Entry(login, width=15)
email_entry.place(x=600, y=130)
password_entry.place(x=600, y=160)
tk.ttk.Button(login, text="Login").place(x=600, y=195)

message = tk.Label(login, text="OR")
message.place(x=625, y=230)
message.configure(bg=_from_rgb((133, 237, 157)))
tk.ttk.Button(login, text="Signup").place(x=600, y=260)


login.mainloop()
