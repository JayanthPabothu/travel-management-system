import tkinter as tk
from tkinter.ttk import *
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox
import admin
from tkinter.font import Font


con = mysql.connect(
        host="localhost",
        user="root",
        password="testpassword",
        database="FMS"
    )

def register_user():
    name = register_entry_name.get()
    email = register_entry_email.get()
    password = register_entry_password.get()
    DOB_day = register_entry_day.get()
    DOB_month = register_entry_month.get()
    DOB_year = register_entry_year.get()
    gender = g.get()
    street = register_entry_street.get()
    city = register_entry_city.get()
    zipcode = register_entry_zipcode.get()
    phone = register_entry_contact.get()
    dob = str(DOB_year)+'-'+str(DOB_month)+'-'+str(DOB_day)

    if(name=='' or email=='' or password=='' or street=='' or city=='' or phone=='' or DOB_day=='' or DOB_month=='' or DOB_year==''):
        messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
    else:
        cursor = con.cursor()
        cursor.execute("SELECT EXISTS(SELECT EMAIL_ID FROM CUSTOMER WHERE EMAIL_ID = %s);", [email])
        status = cursor.fetchall()
        if (status[0][0] == 0):
            cursor.callproc("INSERT_CUSTOMER", [name, email, password, gender, dob, street, city, zipcode, phone])
            cursor.execute("commit")

            messagebox.showinfo("Status", "You have successfully registered!")
            cursor.execute('SELECT CUSTOMER_ID, CREDIT_POINTS FROM CUSTOMER WHERE EMAIL_ID = %s;', [email])
            records = cursor.fetchall()
            id = records[0][0]
            credit = records[0][1]
            con.close()
            register.destroy()
            homepage.homepage_screen(id, email, name, credit)

        else:
            messagebox.showwarning("User already exists", "Try registering with different email-id.")



def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


register = tk.Tk()
register.resizable(height = False, width = False)
register.title('Flight Management System')
register.geometry('720x420')
adam = Font(family="ADAM.CG PRO", size=20)

background1 = tk.PhotoImage(file='Images/flight4.png')
background_label = tk.Label(register,  image=background1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ----------Creating labels---------
register_name = tk.Label(register, text="Name:")
register_name.place(x=20 , y=50)
register_name.configure(bg=_from_rgb((133, 237, 157)))

register_email = tk.Label(register, text="Email Id:")
register_email.place(x=20 , y=80)
register_email.configure(bg=_from_rgb((133, 237, 157)))

register_password = tk.Label(register, text="Password:")
register_password.place(x=20 , y=110)
register_password.configure(bg=_from_rgb((133, 237, 157)))

dob = tk.Label(register, text="DOB:")
dob.place(x=20 , y=140)
dob.configure(bg=_from_rgb((133, 237, 157)))

day = tk.Label(register, text="D:")
day.place(x=85, y=140)
day.configure(bg=_from_rgb((133, 237, 157)))

month = tk.Label(register, text="M:")
month.place(x=135 , y=140)
month.configure(bg=_from_rgb((133, 237, 157)))

year = tk.Label(register, text="Y:")
year.place(x=190 , y=140)
year.configure(bg=_from_rgb((133, 237, 157)))

register_gender = tk.Label(register, text="Gender:")
register_gender.place(x=20 , y=170)
register_gender.configure(bg=_from_rgb((133, 237, 157)))

register_street=tk.Label(register, text="Street:")
register_street.place(x=20 , y=200)
register_street.configure(bg=_from_rgb((133, 237, 157)))

register_city = tk.Label(register, text="City:")
register_city.place(x=20 , y=230)
register_city.configure(bg=_from_rgb((133, 237, 157)))

register_zipcode = tk.Label(register, text="Zipcode:")
register_zipcode.place(x=20 , y=260)
register_zipcode.configure(bg=_from_rgb((133, 237, 157)))

register_contact = tk.Label(register, text="Contact:")
register_contact.place(x=20 , y=290)
register_contact.configure(bg=_from_rgb((133, 237, 157)))

# -------------Creating Entries--------------
register_entry_name = tk.Entry()
register_entry_name.place(x=100 , y=50)

register_entry_email = tk.Entry()
register_entry_email.place(x=100 , y=80)

register_entry_password = tk.Entry()
register_entry_password.place(x=100 , y=110)

register_entry_day = tk.Entry(width=4)
register_entry_day.place(x=100 , y=140)

register_entry_month = tk.Entry(width=4)
register_entry_month.place(x=153, y=140)

register_entry_year = tk.Entry(width=8)
register_entry_year.place(x=205, y=140)

register_entry_street = tk.Entry()
register_entry_street.place(x=100, y=200)

register_entry_city = tk.Entry()
register_entry_city.place(x=100, y=230)

register_entry_zipcode = tk.Entry()
register_entry_zipcode.place(x=100, y=260)

register_entry_contact = tk.Entry()
register_entry_contact.place(x=100, y=290)

g = tk.IntVar()

gender1 = tk.Radiobutton(register, text="M", variable=g, value=1)
gender2 = tk.Radiobutton(register, text="F", variable=g, value=2)
gender3 = tk.Radiobutton(register, text="T", variable=g, value=3)

gender1.place(x=100, y=170)
gender1.configure(bg=_from_rgb((133, 237, 157)))

gender2.place(x=150, y=170)
gender2.configure(bg=_from_rgb((133, 237, 157)))

gender3.place(x=195, y=170)
gender3.configure(bg=_from_rgb((133, 237, 157)))

tk.ttk.Button(register, text="Register", command=register_user).place(x=70, y=330)



register.mainloop()
