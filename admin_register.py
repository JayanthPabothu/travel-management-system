import tkinter as tk
from tkinter.ttk import *
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox
import admin
from tkinter.font import Font


gender_mapper = {1: 'M', 2: 'F', 3: 'T'}

con = mysql.connect(
        host="localhost",
        user="root",
        password="testpassword",
        database="FMS",
        port=3306
    )


def register_user():
    name = register_entry_name.get()
    email = register_entry_email.get()
    password = register_entry_password.get()
    DOB_day = register_entry_day.get()
    DOB_month = register_entry_month.get()
    DOB_year = register_entry_year.get()
    gender = gender_mapper[g.get()]
    street = register_entry_street.get()
    city = register_entry_city.get()
    zipcode = register_entry_zipcode.get()
    phone = register_entry_contact.get()
    dob = str(DOB_year)+'-'+str(DOB_month)+'-'+str(DOB_day)
    code = entry_code.get()

    if(name=='' or email=='' or password=='' or street=='' or city=='' or phone=='' or DOB_day=='' or DOB_month=='' or DOB_year=='' or code==''):
        messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
    else:
        if code=='1111':
            cursor = con.cursor()
            cursor.execute("SELECT EXISTS(SELECT EMAIL_ID FROM SYS_ADMIN WHERE EMAIL_ID = %s);", [email])
            status = cursor.fetchall()
            if (status[0][0] == 0):
                cursor.callproc("INSERT_ADMIN", [name, email, password, gender, dob, street, city, zipcode, phone])
                cursor.execute("commit")

                messagebox.showinfo("Status", "You have successfully registered!")
                cursor.execute('SELECT ADMIN_ID FROM SYS_ADMIN WHERE EMAIL_ID = %s;', [email])
                records = cursor.fetchall()
                id = records[0][0]
                con.close()
                admin_register.destroy()
                #homepage.homepage_screen(id, email, name, credit)

            else:
                messagebox.showwarning("User already exists", "Try registering with different email-id.")
        else:
            messagebox.showwarning("Code Error", "Please enter the correct code provided to you by FMS Developers.")


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


admin_register = tk.Tk()
admin_register.resizable(height = False, width = False)
admin_register.title('Flight Management System')
admin_register.geometry('720x420')
adam = Font(family="ADAM.CG PRO", size=20)

background1 = tk.PhotoImage(file='Images/flight4.png')
background_label = tk.Label(admin_register,  image=background1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ----------Creating labels---------
register_name = tk.Label(admin_register, text="Name:")
register_name.place(x=20 , y=50)
register_name.configure(bg=_from_rgb((133, 237, 157)))

register_email = tk.Label(admin_register, text="Email Id:")
register_email.place(x=20 , y=80)
register_email.configure(bg=_from_rgb((133, 237, 157)))

register_password = tk.Label(admin_register, text="Password:")
register_password.place(x=20 , y=110)
register_password.configure(bg=_from_rgb((133, 237, 157)))

dob = tk.Label(admin_register, text="DOB:")
dob.place(x=20 , y=140)
dob.configure(bg=_from_rgb((133, 237, 157)))

day = tk.Label(admin_register, text="D:")
day.place(x=85, y=140)
day.configure(bg=_from_rgb((133, 237, 157)))

month = tk.Label(admin_register, text="M:")
month.place(x=135 , y=140)
month.configure(bg=_from_rgb((133, 237, 157)))

year = tk.Label(admin_register, text="Y:")
year.place(x=190 , y=140)
year.configure(bg=_from_rgb((133, 237, 157)))

register_gender = tk.Label(admin_register, text="Gender:")
register_gender.place(x=20 , y=170)
register_gender.configure(bg=_from_rgb((133, 237, 157)))

register_street=tk.Label(admin_register, text="Street:")
register_street.place(x=20 , y=200)
register_street.configure(bg=_from_rgb((133, 237, 157)))

register_city = tk.Label(admin_register, text="City:")
register_city.place(x=20 , y=230)
register_city.configure(bg=_from_rgb((133, 237, 157)))

register_zipcode = tk.Label(admin_register, text="Zipcode:")
register_zipcode.place(x=20 , y=260)
register_zipcode.configure(bg=_from_rgb((133, 237, 157)))

register_contact = tk.Label(admin_register, text="Contact:")
register_contact.place(x=20 , y=290)
register_contact.configure(bg=_from_rgb((133, 237, 157)))

admin_code = tk.Label(admin_register, text="Admin Code:")
admin_code.place(x=20 , y=320)
admin_code.configure(bg=_from_rgb((133, 237, 157)))
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

entry_code = tk.Entry()
entry_code.place(x=100, y=320)

g = tk.IntVar()

gender1 = tk.Radiobutton(admin_register, text="M", variable=g, value=1)
gender2 = tk.Radiobutton(admin_register, text="F", variable=g, value=2)
gender3 = tk.Radiobutton(admin_register, text="T", variable=g, value=3)

gender1.place(x=100, y=170)
gender1.configure(bg=_from_rgb((133, 237, 157)))

gender2.place(x=150, y=170)
gender2.configure(bg=_from_rgb((133, 237, 157)))

gender3.place(x=195, y=170)
gender3.configure(bg=_from_rgb((133, 237, 157)))

tk.ttk.Button(admin_register, text="Register", command=register_user).place(x=70, y=360)



admin_register.mainloop()
