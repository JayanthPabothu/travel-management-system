import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_city():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="testpassword",
    database="FMS"
    )
    cursor = con.cursor()

    # old_city_code = ""

    def view_city():

        cursor = con.cursor()
        cursor.execute("SELECT *FROM CITY;")
        records = cursor.fetchall()
        city_list.delete(0, tk.END)
        for rec in records:
            city_list.insert(tk.END, rec)

    def get_selected_row(event):
        global old_city_code
        index = city_list.curselection()
        if (len(index) != 0):
            selected_tuple = city_list.get(index)
            city_code.delete(0, tk.END)
            city_code.insert(tk.END,selected_tuple[0])
            old_city_code= city_code.get()
            city.delete(0, tk.END)
            city.insert(tk.END, selected_tuple[1])
            zip_code.delete(0, tk.END)
            zip_code.insert(tk.END, selected_tuple[2])
            airport.delete(0, tk.END)
            airport.insert(tk.END, selected_tuple[3])
        else:
            pass


    def insert_city():
        city1 = city.get()
        city_code1 = city_code.get()
        zip_code1 = zip_code.get()
        airport1 = airport.get()

        if(city1 == '' or city_code1 == '' or zip_code1 == '' or airport1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        elif (len(str(zip_code1)) != 6):
            messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
        else:
            args = cursor.callproc("CHECK_IF_CITY_EXISTS", [city_code1, None])
            if (args[-1] == 1):
                messagebox.showwarning("City already exists", "Please enter a new city.")
            else:
                cursor.callproc("INSERT_CITY_DETAILS", [city_code1, city1, int(zip_code1), airport1])
                cursor.execute("commit")
                city_code.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                airport.delete(0, tk.END)
                city_list.delete(0, tk.END)
                view_city()
                messagebox.showinfo("Request successful", "Successfully added city.")

    def update_city():
        city1 = city.get()
        city_code1 = city_code.get()
        zip_code1 = zip_code.get()
        airport1 = airport.get()

        if(city1 == '' or city_code1 == '' or zip_code1 == '' or airport1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have fetched all the fields.")
        elif (len(str(zip_code1)) != 6):
            messagebox.showwarning("Invalid request", "Enter a valid Zip Code.")
        else:
            args = cursor.callproc("CHECK_IF_CITY_EXISTS", [city_code1, None])
            if (args[-1] == 1):
                cursor.callproc("UPDATE_CITY_DETAILS", [old_city_code, city_code1, city1, zip_code1, airport1])
                cursor.execute("commit")
                city_code.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                airport.delete(0, tk.END)
                city_list.delete(0, tk.END)
                view_city()
                messagebox.showinfo("Request successful", "Successfully updated city.")
            else:
                messagebox.showwarning("Invalid Request", "City does not exists.")

    def delete_city():
        # city1 = city.get()
        city_code1 = city_code.get()
        # zip_code1 = zip_code.get()
        # airport1 = airport.get()
        if (city_code1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have selected a city to delete.")
        else:
            args = cursor.callproc("CHECK_IF_CITY_EXISTS", [city_code1, None])
            if (args[-1] == 1):
                cursor.callproc("DELETE_CITY_BY_CODE", [city_code1])
                cursor.execute("commit")
                city_code.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                airport.delete(0, tk.END)
                city_list.delete(0, tk.END)
                view_city()
                messagebox.showinfo("Request successful", "Successfully deleted city.")
            else:
                messagebox.showwarning("Invalid Request", "City does not exists.")

    def search_city():
        city1 = city.get()
        city_code1 = city_code.get()
        zip_code1 = zip_code.get()
        airport1 = airport.get()
        if(city1 == '' and city_code1 == '' and zip_code1 == '' and airport1 == ''):
            messagebox.showwarning("Invalid request", "Enter valid data you want to search.")
        else:
            cursor.execute("SELECT * FROM CITY WHERE CITY_CODE = %s OR CITY_NAME = %s OR ZIPCODE = %s OR AIRPORT = %s;", [city_code1, city1, zip_code1, airport1])
            records = cursor.fetchall()
            if(len(records) == 0):
                messagebox.showwarning("Invalid request", "No Records Found.")
            else:
                city_code.delete(0, tk.END)
                city.delete(0, tk.END)
                zip_code.delete(0, tk.END)
                airport.delete(0, tk.END)
                city_list.delete(0, tk.END)
                for rec in records:
                    city_list.insert(tk.END, rec)


    City = tk.Tk()
    City.resizable(height = False, width = False)
    City.title('Travel Management System')
    City.geometry('720x500')

    #tk.Label(City, text="City", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(City, text="City name").grid(row = 0, column = 0)
    tk.Label(City, text="City Code").grid(row = 1, column = 0)
    tk.Label(City, text="Zip Code").grid(row = 0, column = 2)
    tk.Label(City, text="Airport").grid(row = 1, column = 2)



    city = tk.ttk.Entry(City)
    city.grid(row = 0, column = 1)
    city_code = tk.ttk.Entry(City)
    city_code.grid(row = 1, column = 1)
    zip_code = tk.ttk.Entry(City)
    zip_code.grid(row = 0, column = 3)
    airport = tk.ttk.Entry(City)
    airport.grid(row = 1, column = 3)


    city_list = tk.Listbox(City, height = 15, width = 60)
    city_list.grid(row = 2, column = 0, columnspan = 2, rowspan = 5)

    city_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(City, width = 10)
    sb1.grid(row=2, column=1, columnspan = 3, rowspan = 5)

    city_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = city_list.yview)


    tk.ttk.Button(City, text="Insert", command=insert_city, width = 12).grid(row= 2, column=3)
    tk.ttk.Button(City, text="Update", command=update_city, width = 12).grid(row= 3, column=3)
    tk.ttk.Button(City, text="Delete", command=delete_city, width = 12).grid(row= 4, column=3)
    tk.ttk.Button(City, text="View All", command=view_city, width = 12).grid(row= 5, column=3)
    tk.ttk.Button(City, text="Search", command=search_city, width = 12).grid(row= 6, column=3)

    #Makes the widgets responsive and centered
    n_rows = 10
    n_columns = 5
    for i in range(n_rows):
        City.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        City.grid_columnconfigure(i,  weight =1)

    City.mainloop()
# crud_city()
