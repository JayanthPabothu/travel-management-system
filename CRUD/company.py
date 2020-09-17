import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# import mysql.connector as mysql




# def crud_Company():
#     con = mysql.connect(
#     host="localhost",
#     user="root",
#     password="shobhit2000@",
#     database="FMS"
#     )
#     cursor = con.cursor()
#
#     # old_Company_code = ""
#
#     def view_Company():
#
#         cursor = con.cursor()
#         cursor.execute("SELECT *FROM Company;")
#         records = cursor.fetchall()
#         Company_list.delete(0, tk.END)
#         for rec in records:
#             Company_list.insert(tk.END, rec)
#
#     def get_selected_row(event):
#         global old_Company_code
#         print(Company_list.curselection())
#         index = Company_list.curselection()[0]
#         selected_tuple = Company_list.get(index)
#         print(selected_tuple)
#         Company_code.delete(0, tk.END)
#         Company_code.insert(tk.END,selected_tuple[0])
#         old_Company_code= Company_code.get()
#         print(old_Company_code)
#         Company.delete(0, tk.END)
#         Company.insert(tk.END, selected_tuple[1])
#         zip_code.delete(0, tk.END)
#         zip_code.insert(tk.END, selected_tuple[2])
#         airport.delete(0, tk.END)
#         airport.insert(tk.END, selected_tuple[3])
#
#
#     def insert_Company():
#         Company1 = Company.get()
#         Company_code1 = Company_code.get()
#         zip_code1 = zip_code.get()
#         airport1 = airport.get()
#
#         if(Company1 == '' or Company_code1 == '' or zip_code1 == '' or airport1 == ''):
#             messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
#         elif (len(str(zip_code1)) != 6):
#             messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
#         else:
#             args = cursor.callproc("CHECK_IF_Company_EXISTS", [Company_code1, None])
#             if (args[-1] == 1):
#                 messagebox.showwarning("Company already exists", "Please enter a new Company.")
#             else:
#                 cursor.callproc("INSERT_Company_DETAILS", [Company_code1, Company1, int(zip_code1), airport1])
#                 cursor.execute("commit")
#                 messagebox.showinfo("Request successful", "Successfully added Company.")
#
#     def update_Company():
#         Company1 = Company.get()
#         Company_code1 = Company_code.get()
#         zip_code1 = zip_code.get()
#         airport1 = airport.get()
#         print(old_Company_code)
#
#         if(Company1 == '' or Company_code1 == '' or zip_code1 == '' or airport1 == ''):
#             messagebox.showwarning("Invalid request", "Please make sure you have fetched all the fields.")
#         elif (len(str(zip_code1)) != 6):
#             messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
#         else:
#             cursor.callproc("UPDATE_Company_DETAILS", [old_Company_code, Company_code1, Company1, zip_code1, airport1])
#             cursor.execute("commit")
#             messagebox.showinfo("Request successful", "Successfully updated Company.")
#
#     def delete_Company():
#         if (Company == '' or Company_code == '' or zip_code == '' or airport == ''):
#             messagebox.showwarning("Invalid request", "Please make sure you have selected a Company to delete.")
#         else:
#             cursor.callproc("DELETE_Company_BY_CODE", [old_Company_code])
#             cursor.execute("commit")
#             messagebox.showinfo("Request successful", "Successfully deleted Company.")
#
#     def search_Company():
#         Company1 = Company.get()
#         Company_code1 = Company_code.get()
#         zip_code1 = zip_code.get()
#         airport1 = airport.get()
#         cursor.execute("SELECT * FROM Company WHERE Company_CODE = %s OR Company_NAME = %s OR ZIPCODE = %s OR AIRPORT = %s;", [Company_code1, Company1, zip_code1, airport1])
#         records = cursor.fetchall()
#         Company_list.delete(0, tk.END)
#         for rec in records:
#             Company_list.insert(tk.END, rec)


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



Company_list = tk.Listbox(Company, height = 17, width = 50)
Company_list.grid(row = 4, column = 0, columnspan = 2, rowspan = 5)

# Company_list.bind('<<ListboxSelect>>', get_selected_row)

sb1= tk.Scrollbar(Company, width = 10)
sb1.grid(row=3, column=1, columnspan = 2, rowspan = 6)

Company_list.configure(yscrollcommand = sb1.set)
sb1.configure(command = Company_list.yview)


tk.ttk.Button(Company, text="Insert",  width = 12).grid(row= 4, column=3)
tk.ttk.Button(Company, text="Update",  width = 12).grid(row= 5, column=3)
tk.ttk.Button(Company, text="Delete", width = 12).grid(row= 6, column=3)
tk.ttk.Button(Company, text="View All",  width = 12).grid(row= 7, column=3)
tk.ttk.Button(Company, text="Search", width = 12).grid(row= 8, column=3)

# Makes the widgets responsive and centered
n_rows = 12
n_columns = 4
for i in range(n_rows):
    Company.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    Company.grid_columnconfigure(i,  weight =1)

Company.mainloop()
# crud_Company()
