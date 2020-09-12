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


def login_user():
    email = login_entry_email.get()
    password = login_entry_password.get()

    if(email == '' or password == ''):
        messagebox.showwarning("Invalid request", "Please enter correct email/password")
    else:
        con = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
            )
        cursor = con.cursor()
        cursor.execute("SELECT CUSTOMER_ID, CUSTOMER_NAME, CREDIT_POINTS FROM CUSTOMER WHERE EMAIL_ID=%s AND CUSTOMER_PASSWORD=%s;", [str(email), str(password)])
        records = cursor.fetchmany(size=1)
        print(records)
        if (len(records) == 0):
            cursor.execute("SELECT ADMIN_ID, ADMIN_NAME FROM SYS_ADMIN WHERE EMAIL_ID=%s AND ADMIN_PASSWORD=%s;", [str(email), str(password)])
            records = cursor.fetchmany(size=1)
            if (len(records) == 0):
                messagebox.showwarning("Invalid request", "Please enter correct email/password")
            else:
                admin_id = records[0][0]
                admin_name = records[0][1]
                window.destroy()
                admin.admin_screen(admin_id, admin_name)
        else:
            user_id = records[0][0]
            user_name = records[0][1]
            credit_points = records[0][2]
            window.destroy()
            homepage.homepage_screen(user_id, user_name, credit_points)


def register_user():
    name = register_entry_name.get()
    email = register_entry_email.get()
    password = register_entry_password.get()
    password_again = register_entry_password_again.get()
    DOB_day = register_entry_day.get()
    DOB_month = register_entry_month.get()
    DOB_year = register_entry_year.get()
    gender = g.get()
    street = register_entry_street.get()
    city = register_entry_city.get()
    zipcode = register_entry_zipcode.get()
    phone = register_entry_contact.get()
    dob = str(DOB_year)+'-'+str(DOB_month)+'-'+str(DOB_day)
    credit = 5
    id = 3
    print(dob)
    if(name=='' or email=='' or password=='' or street=='' or city=='' or phone==''):
        messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
    else:
        con = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
            )
        cursor = con.cursor()
        args = cursor.callproc("CHECK_IF_EXISTS", (email, None))
        con.close()
        print(args)
        if(args[1] == 1):
            messagebox.showwarning("User already exists", "Try registering with different email-id.")
        else:
            if(password != password_again):
                messagebox.showwarning("Invalid request", "Your passwords don't match. Please try again.")
            else:
                gender_new = ''
                if (gender == 1):
                    gender_new = 'M'
                elif (gender == 2):
                    gender_new = 'F'
                elif (gender == 3):
                    gender_new = 'T'

                con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="TMS"
                )
                cursor = con.cursor()
                cursor.execute("INSERT INTO CUSTOMER(CUSTOMER_NAME, EMAIL_ID, CUSTOMER_PASSWORD, GENDER, DOB, STREET, CITY, ZIPCODE, CONTACT_DETAILS, CREDIT_POINTS) VALUES(%s, %s, %s, %s, %s, %s, %s,%s, %s, %s);", [name, email, password, gender_new, dob,street, city, int(zipcode), int(phone), credit])
                cursor.execute("commit")

                messagebox.showinfo("Status", "You have successfully registered!")
                con.close()

window = tk.Tk()
window.resizable(height = False, width = False)
window.title('Travel Management System')
window.geometry('720x420')
heading = tk.Label(window, text="Travel Management System", font=('Helvetica', '25'))

login_head = tk.Label(window, text="Login here", bg='grey',font=('Helvetica', '20'))
register_head = tk.Label(window, text="Register here", bg='grey',font=('Helvetica', '20'))

background = tk.PhotoImage(file='Images/background.png')
description = tk.Label(window, text="\n\n\n\n\n\n")
background_label = tk.Label(window,  image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# window.configure(image=background)
# ----------Creating labels---------
login_email = tk.Label(window, text="Enter your Email Id")
login_password = tk.Label(window, text="Enter your Password")

register_name = tk.Label(window, text="Enter your Name")
register_email = tk.Label(window, text="Enter your Email Id")
register_password = tk.Label(window, text="Enter your Password")
register_password_again =  tk.Label(window, text="Enter your Password again")
register_DOB = []
register_DOB.append(tk.Label(window, text="Enter yor Date of Birth (dd mm yyyy)"))
register_DOB.append(tk.Label(window, text="D:"))
register_DOB.append(tk.Label(window, text="M:"))
register_DOB.append(tk.Label(window, text="Y:"))
register_gender = tk.Label(window, text="Gender")
register_street=tk.Label(window, text="Street")
register_city = tk.Label(window, text="City")
register_zipcode = tk.Label(window, text="Zipcode")
register_contact = tk.Label(window, text="Contact number")

# ----------Creating entries----------
login_entry_email = tk.Entry()
login_entry_password = tk.Entry()

register_entry_name = tk.Entry()
register_entry_email = tk.Entry()
register_entry_password = tk.Entry()
register_entry_password_again = tk.Entry()
register_entry_street = tk.Entry()
register_entry_city = tk.Entry()
register_entry_zipcode = tk.Entry()
register_entry_contact = tk.Entry()
register_entry_day = tk.Entry(width=10)
register_entry_month = tk.Entry(width=10)
register_entry_year = tk.Entry(width=10)
g = tk.IntVar()

gender1 = tk.Radiobutton(window, text="M", variable=g, value=1)
gender2 = tk.Radiobutton(window, text="F", variable=g, value=2)
gender3 = tk.Radiobutton(window, text="T", variable=g, value=3)


login_button = Button(window, text="Login", command=login_user)
register_button = Button(window, text="Register", command=register_user)

# ----------Placing on grid-----------
heading.grid(columnspan=7)
description.grid(column=0, row=1,columnspan=7)
# login stuff
login_head.grid(column=0, row=2, columnspan=2)
register_head.grid(column=2, row=2, columnspan=4)
login_email.grid(column=0, row=3)
login_password.grid(column=0, row=4)
login_entry_email.grid(column=1, row=3)
login_entry_password.grid(column=1, row=4)
login_button.grid(column=0, row=5, columnspan=2)

# register labels
register_name.grid(column=2, row=3)
register_email.grid(column=2, row=4)
register_password.grid(column=2, row=5)
register_password_again.grid(column=2, row=6)
register_gender.grid(column=2, row=7)
register_street.grid(column=2, row=8)
register_city.grid(column=2, row=9)
register_zipcode.grid(column=2, row=10)
register_contact.grid(column=2, row=11)
register_DOB[0].grid(column=2, row=12)
register_DOB[1].grid(column=3, row=12)
register_DOB[2].grid(column=4, row=12)
register_DOB[3].grid(column=5, row=12)

# register entries
register_entry_name.grid(column=3, row=3, columnspan=3)
register_entry_email.grid(column=3, row=4, columnspan=3)
register_entry_password.grid(column=3, row=5, columnspan=3)
register_entry_password_again.grid(column=3, row=6, columnspan=3)
gender1.grid(column=3, row=7)
gender2.grid(column=4, row=7)
gender3.grid(column=5, row=7)
register_entry_street.grid(column=3, row=8, columnspan=3)
register_entry_city.grid(column=3, row=9, columnspan=3)
register_entry_zipcode.grid(column=3, row=10, columnspan=3)
register_entry_contact.grid(column=3, row=11, columnspan=3)
register_entry_day.grid(column=3, row=12)
register_entry_month.grid(column=4, row=12)
register_entry_year.grid(column=5, row=12)

register_button.grid(column=2, row=15, columnspan=2)




n_rows = 15
n_columns = 7
for i in range(n_rows):
    window.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    window.grid_columnconfigure(i,  weight =1)

window.mainloop()
