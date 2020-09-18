import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql



def crud_company():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="testpassword",
    database="FMS"
    )
    cursor = con.cursor()

    # old_city_code = ""

    def view_company():

        cursor = con.cursor()
        cursor.execute("SELECT * FROM COMPANY;")
        records = cursor.fetchall()
        company_list.delete(0, tk.END)
        for rec in records:
            company_list.insert(tk.END, rec)

    def get_selected_row(event):
        global old_company_id
        index = company_list.curselection()
        if (len(index) != 0):
            selected_tuple = company_list.get(index)
            old_company_id = selected_tuple[0]
            # old_city_code= city_code.get()
            company_name.delete(0, tk.END)
            company_name.insert(tk.END, selected_tuple[1])
            contact_details.delete(0, tk.END)
            contact_details.insert(tk.END, selected_tuple[3])
            city.delete(0, tk.END)
            city.insert(tk.END, selected_tuple[5])
            email_ID.delete(0, tk.END)
            email_ID.insert(tk.END, selected_tuple[2])
            street.delete(0, tk.END)
            street.insert(tk.END, selected_tuple[4])
            zip_code.delete(0, tk.END)
            zip_code.insert(tk.END, selected_tuple[6])
        else:
            pass


    def insert_company():
        company_name1 = company_name.get()
        phone1 = contact_details.get()
        zip_code1 = zip_code.get()
        city1 = city.get()
        email_ID1 = email_ID.get()
        street1 = street.get()

        if(company_name1 == '' or phone1 == '' or zip_code1 == '' or city1 == '' or email_ID1 == '' or street1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:
            try:
                phone1 = int(phone1)
                zip_code1 = int(zip_code1)

                if (len(str(zip_code1)) != 6):
                    messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
                elif (len(phone1) != 10):
                    messagebox.showwarning("Invalid request", "Enter a valid phone number.")

                else:
                    args = cursor.callproc("CHECK_IF_COMPANY_EXISTS", [company_name1, None])
                    if (args[-1] == 1):
                        messagebox.showwarning("Company already exists", "Please enter a unique company.")
                    else:
                        cursor.callproc("INSERT_COMPANY", [company_name1, email_ID1, int(phone1), street1, city1, int(zip_code1)])
                        cursor.execute("commit")
                        company_name.delete(0, tk.END)
                        city.delete(0, tk.END)
                        zip_code.delete(0, tk.END)
                        email_ID.delete(0, tk.END)
                        street.delete(0, tk.END)
                        contact_details.delete(0, tk.END)
                        company_list.delete(0, tk.END)
                        view_company()
                        messagebox.showinfo("Request successful", "Successfully added the Company.")
            except:
                messagebox.showwarning("Invalid request", "Please enter valid integer values for the required fields.")


    def update_company():
        company_name1 = company_name.get()
        phone1 = contact_details.get()
        zip_code1 = zip_code.get()
        city1 = city.get()
        email_ID1 = email_ID.get()
        street1 = street.get()

        if(company_name1 == '' or phone1 == '' or zip_code1 == '' or city1 == '' or email_ID1 == '' or street1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have inserted all the fields.")
        else:
            if (len(str(zip_code1)) != 6):
                messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
            else:
                try:
                    phone1 = int(phone1)
                    zip_code1 = int(zip_code1)

                    args = cursor.callproc("CHECK_IF_COMPANY_EXISTS", [company_name1, None])
                    if (args[-1] == 1):
                        cursor.callproc("UPDATE_COMPANY_DETAILS", [old_company_id, company_name1, email_ID1, phone1, street1,city1, zip_code1])
                        cursor.execute("commit")
                        company_name.delete(0, tk.END)
                        city.delete(0, tk.END)
                        zip_code.delete(0, tk.END)
                        email_ID.delete(0, tk.END)
                        street.delete(0, tk.END)
                        contact_details.delete(0, tk.END)
                        company_list.delete(0, tk.END)
                        view_company()
                        messagebox.showinfo("Request successful", "Successfully updated the company.")
                    else:
                        messagebox.showwarning("Invalid Request", "The company does not exists.")
                except:
                    messagebox.showwarning("Invalid request", "Please enter valid integer values for the required fields.")

    def delete_company():
        name = company_name.get()
        if (name == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have selected any company to delete.")
        else:
            args = cursor.callproc("CHECK_IF_COMPANY_EXISTS", [name, None])
            if (args[-1] == 1):
                cursor.callproc("DELETE_COMPANY_DETAILS", [name])
                cursor.execute("commit")
                company_name.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                email_ID.delete(0, tk.END)
                street.delete(0, tk.END)
                contact_details.delete(0, tk.END)
                company_list.delete(0, tk.END)
                view_company()
                messagebox.showinfo("Request successful", "Successfully deleted the company.")
            else:
                messagebox.showwarning("Invalid Request", "Company does not exists.")

    def search_company():
        company_name1 = company_name.get()
        phone1 = contact_details.get()
        zip_code1 = zip_code.get()
        city1 = city.get()
        email_ID1 = email_ID.get()
        street1 = street.get()

        if(company_name1 == '' and phone1 == '' and zip_code1 == '' and city1 == '' and email_ID1 == '' and street1 == ''):
            messagebox.showwarning("Invalid request", "Enter the data you want to search.")
        else:
            cursor.execute("SELECT * FROM COMPANY WHERE COMPANY_NAME = %s OR EMAIL_ID = %s OR CONTACT_DETAILS = %s OR CITY = %s OR STREET = %s OR ZIPCODE = %s;", [company_name1, email_ID1, phone1, city1, street1, zip_code1])
            records = cursor.fetchall()
            if(len(records) == 0):
                messagebox.showwarning("Invalid request", "No Records Found.")
            else:
                company_name.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                email_ID.delete(0, tk.END)
                street.delete(0, tk.END)
                contact_details.delete(0, tk.END)
                company_list.delete(0, tk.END)
                for rec in records:
                    company_list.insert(tk.END, rec)



    Company = tk.Tk()
    Company.resizable(height = False, width = False)
    Company.title('Travel Management System')
    Company.geometry('720x500')

    #tk.Label(Company, text="Company", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(Company, text="Company Name").grid(row = 0, column = 0)
    tk.Label(Company, text="Contact Details").grid(row = 1, column = 0)
    tk.Label(Company, text="City").grid(row = 2, column = 0)
    tk.Label(Company, text="Email_ID").grid(row = 0, column = 2)
    tk.Label(Company, text="Street").grid(row = 1, column = 2)
    tk.Label(Company, text="Zip Code").grid(row = 2, column = 2)


    company_name = tk.ttk.Entry(Company)
    company_name.grid(row = 0, column = 1)
    contact_details = tk.ttk.Entry(Company)
    contact_details.grid(row = 1, column = 1)
    city = tk.ttk.Entry(Company)
    city.grid(row = 2, column = 1)
    email_ID = tk.ttk.Entry(Company)
    email_ID.grid(row = 0,column = 3)
    street = tk.ttk.Entry(Company)
    street.grid(row = 1, column = 3)
    zip_code = tk.ttk.Entry(Company)
    zip_code.grid(row = 2, column = 3)



    company_list = tk.Listbox(Company, height = 17, width = 50)
    company_list.grid(row = 4, column = 0, columnspan = 2, rowspan = 5)

    company_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(Company, width = 10)
    sb1.grid(row=3, column=1, columnspan = 2, rowspan = 6)

    company_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = company_list.yview)


    tk.ttk.Button(Company, text="Insert",  width = 12, command=insert_company).grid(row= 4, column=3)
    tk.ttk.Button(Company, text="Update",  width = 12, command=update_company).grid(row= 5, column=3)
    tk.ttk.Button(Company, text="Delete", width = 12, command=delete_company).grid(row= 6, column=3)
    tk.ttk.Button(Company, text="View All",  width = 12, command=view_company).grid(row= 7, column=3)
    tk.ttk.Button(Company, text="Search", width = 12, command=search_company).grid(row= 8, column=3)

    # Makes the widgets responsive and centered
    n_rows = 12
    n_columns = 4
    for i in range(n_rows):
        Company.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        Company.grid_columnconfigure(i,  weight =1)

    Company.mainloop()
crud_company()
