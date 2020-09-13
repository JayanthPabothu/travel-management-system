import tkinter as tk
from tkinter.ttk import *
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox
import homepage
import admin
from tkinter.font import Font


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def get_register():
    login.destroy()
    import register

def main_screen():


    def login_user():
        email = email_entry.get()
        password = password_entry.get()

        if(email == '' or password == ''):
            messagebox.showwarning("Invalid request", "Please enter your credentials.")
        else:
            con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="FMS"
                )
            cursor = con.cursor()
            args = cursor.callproc("CHECK_IF_CUSTOMER_EXISTS", [email, password,None])
            if (args[-1] == 1):
                cursor.execute("SELECT CUSTOMER_ID, CUSTOMER_NAME, CREDIT_POINTS FROM CUSTOMER WHERE EMAIL_ID=%s AND CUSTOMER_PASSWORD=%s;", [str(email), str(password)])
                records = cursor.fetchmany(size=1)
                user_id = records[0][0]
                user_name = records[0][1]
                credit_points = records[0][2]
                login.destroy()
                homepage.homepage_screen(user_id, email,user_name, credit_points)

            else:
                args = cursor.callproc("CHECK_IF_ADMIN_EXISTS", [email, password,None])

                if (args[-1] == 1):
                    cursor.execute("SELECT ADMIN_ID, ADMIN_NAME FROM SYS_ADMIN WHERE EMAIL_ID=%s AND ADMIN_PASSWORD=%s;", [str(email), str(password)])
                    records = cursor.fetchmany(size=1)
                    admin_id = records[0][0]
                    admin_name = records[0][1]
                    login.destroy()
                    admin.admin_screen(admin_id, admin_name)
                else:
                    messagebox.showwarning("Invalid request", "Please enter correct email/password")


    login = tk.Tk()
    login.resizable(height = False, width = False)
    login.title('Flight Management System')
    login.geometry('720x420')
    adam = Font(family="ADAM.CG PRO", size=20)
    # heading = tk.Label(login, text="Travel Management System")
    # register_head = tk.Label(login, text="Register here", bg='grey',font=('Helvetica', '20'))

    background = tk.PhotoImage(file='Images/background.png')
    description = tk.Label(login, text="\n\n\n\n\n\n")
    background_label = tk.Label(login,  image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    login_head = tk.Label(login, text="Login here",font=adam)
    login_head.place(x=540, y=75)
    login_head.configure(bg=_from_rgb((133, 237, 157)))

    email = tk.Label(login, text="Email ID:")

    email.place(x=510, y=130)
    email.configure(bg=_from_rgb((133, 237, 157)))

    password = tk.Label(login, text="Password:")
    password.place(x=510, y=160)
    password.configure(bg=_from_rgb((133, 237, 157)))

    email_entry = tk.Entry(login, width=15)
    password_entry = tk.Entry(login, width=15)
    email_entry.place(x=600, y=130)
    password_entry.place(x=600, y=160)
    tk.ttk.Button(login, text="Login", command=login_user).place(x=600, y=195)

    message = tk.Label(login, text="OR")
    message.place(x=625, y=230)
    message.configure(bg=_from_rgb((133, 237, 157)))
    tk.ttk.Button(login, text="Signup", command=get_register).place(x=600, y=260)


    login.mainloop()

if __name__=="__main__":
    main_screen()
