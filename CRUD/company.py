import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_company():

    def insert_company():

        name = company_name.get()
        email1 = email.get()
        phone1 = phone.get()
        street1 = street.get()
        zipcode1 = zipcode.get()
        city1 = city.get()

        con = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
            )
        cursor = con.cursor()
        cursor.execute("INSERT INTO COMPANY(COMPANY_NAME, EMAIL_ID, CONTACT_DETAILS, STREET, CITY, ZIPCODE) VALUES(%s, %s, %s, %s, %s, %s);", [name, email1, phone1, street1, city1, zipcode1])
        cursor.execute("commit")
        cursor.close()
        con.close()
        company.destroy()
        messagebox.showinfo("Request successful", "Successfully added Company.")

    company = tk.Tk()
    company.resizable(height = False, width = False)
    company.title('Travel Management System')
    company.geometry('720x500')

    tk.Label(company, text="Company", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(company, text="Company name").grid(column=0, row=1)
    tk.Label(company, text="Email id").grid(column=0, row=2)
    tk.Label(company, text="Contact details").grid(column=0, row=3)
    tk.Label(company, text="Street").grid(column=0, row=4)
    tk.Label(company, text="City").grid(column=0, row=5)
    tk.Label(company, text="Zip code").grid(column=0, row=6)



    company_name = tk.ttk.Entry(company)
    company_name.grid(column=1, row=1)

    email = tk.ttk.Entry(company)
    email.grid(column=1, row=2)

    phone = tk.ttk.Entry(company)
    phone.grid(column=1, row=3)

    street = tk.ttk.Entry(company)
    street.grid(column=1, row=4)

    city = tk.ttk.Entry(company)
    city.grid(column=1, row=5)

    zipcode = tk.ttk.Entry(company)
    zipcode.grid(column=1, row=6)


    tk.ttk.Button(company, text="Submit", command=insert_company).grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        company.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        company.grid_columnconfigure(i,  weight =1)

    company.mainloop()
