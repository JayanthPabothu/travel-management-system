import tkinter as tk
from tkinter import ttk
from functools import partial
import mysql.connector as mysql
import datetime as dt
from tkinter import messagebox
import homepage


def update_user(user_id, homepage):

    def update_data(user_id, homepage):
        name = register_entry_name1.get()
        email = register_entry_email.get()
        password = register_entry_password.get()
        password_again = register_entry_password_again.get()
        DOB_day = register_entry_day.get()
        DOB_month = register_entry_month.get()
        DOB_year = register_entry_year.get()
        street = register_entry_street.get()
        city = register_entry_city.get()
        zipcode = register_entry_zipcode.get()
        phone = register_entry_contact.get()
        dob = str(DOB_year)+'-'+str(DOB_month)+'-'+str(DOB_day)
        print(name, email, password, dob, street, zipcode, phone)


        if(name=='' or email=='' or password=='' or street=='' or city=='' or phone==''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:

            if(password != password_again):
                messagebox.showwarning("Invalid request", "Your passwords don't match. Please try again.")
            else:

                con1 = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
                )
                cursor1 = con1.cursor()
                args = cursor1.callproc("UPDATE_CUST_DETAILS", [int(user_id), str(name), str(email), str(password), str(dob), str(street), str(city), int(zipcode), int(phone)])
                print(args)
                cursor1.execute("commit")
                messagebox.showinfo("Updation successful", "Your data has been successfully updated.")
                cursor1.close()
                con1.close()
                update.destroy()
                homepage.destroy()
                import main

    update = tk.Tk()
    update.resizable(height = False, width = False)
    update.title('Travel Management System')
    update.geometry('800x600')

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="TMS"
        )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID=%s", [int(user_id)])
    records = cursor.fetchmany(size=1)[0]

    tk.Label(update, text="Update details", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=3)
    tk.Label(update, text="Enter your Name").grid(column=0, row=1)
    tk.Label(update, text="Enter your Email Id").grid(column=0, row=2)
    tk.Label(update, text="Enter your Password").grid(column=0, row=3)
    tk.Label(update, text="Enter your Password again").grid(column=0, row=4)
    register_DOB = []
    register_DOB.append(tk.Label(update, text="Enter yor Date of Birth (dd mm yyyy)"))
    register_DOB.append(tk.Label(update, text="D:"))
    register_DOB.append(tk.Label(update, text="M:"))
    register_DOB.append(tk.Label(update, text="Y:"))

    register_DOB[0].grid(column=0, row=5)
    register_DOB[1].grid(column=1, row=5)
    register_DOB[2].grid(column=2, row=5)
    register_DOB[3].grid(column=3, row=5)
    tk.Label(update, text="Street").grid(column=0, row=6)
    tk.Label(update, text="City").grid(column=0, row=7)
    tk.Label(update, text="Zipcode").grid(column=0, row=8)
    tk.Label(update, text="Contact number").grid(column=0, row=9)

    # Entries
    register_entry_name1 = tk.Entry(update)
    register_entry_name1.insert(0, records[1])

    register_entry_email = tk.Entry(update)
    register_entry_email.insert(0, records[2])

    register_entry_password = tk.Entry(update)
    register_entry_password.insert(0, records[3])

    register_entry_password_again = tk.Entry(update)
    register_entry_password_again.insert(0, records[3])

    register_entry_street = tk.Entry(update)
    register_entry_street.insert(0, records[6])

    register_entry_city = tk.Entry(update)
    register_entry_city.insert(0, records[7])

    register_entry_zipcode = tk.Entry(update)
    register_entry_zipcode.insert(0, records[8])

    register_entry_contact = tk.Entry(update)
    register_entry_contact.insert(0, records[9])

    register_entry_day = tk.Entry(update,width=10)
    register_entry_day.insert(0, records[5].strftime("%d"))

    register_entry_month = tk.Entry(update,width=10)
    register_entry_month.insert(0, records[5].strftime("%m"))

    register_entry_year = tk.Entry(update,width=10)
    register_entry_year.insert(0, records[5].strftime("%Y"))

    # Placing entries on grid
    register_entry_name1.grid(column=1, row=1, columnspan=3)
    register_entry_email.grid(column=1, row=2, columnspan=3)
    register_entry_password.grid(column=1, row=3, columnspan=3)
    register_entry_password_again.grid(column=1, row=4, columnspan=3)
    register_entry_street.grid(column=1, row=6, columnspan=3)
    register_entry_city.grid(column=1, row=7, columnspan=3)
    register_entry_zipcode.grid(column=1, row=8, columnspan=3)
    register_entry_contact.grid(column=1, row=9, columnspan=3)
    register_entry_day.grid(column=1, row=5)
    register_entry_month.grid(column=2, row=5)
    register_entry_year.grid(column=3, row=5)

    tk.ttk.Button(update, text="Update values", command=partial(update_data, user_id, homepage)).grid(column=1, row=10, columnspan=2)
    # Makes the widgets responsive and centered
    n_rows = 15
    n_columns = 4
    for i in range(n_rows):
        update.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        update.grid_columnconfigure(i,  weight =1)


    update.mainloop()
