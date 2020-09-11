import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_city():

    def insert_city():
        city1 = city.get()
        city_code1 = city_code.get()
        zip_code1 = zip_code.get()
        boarding_point1 = boarding_point.get()

        con = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
            )
        cursor = con.cursor()
        cursor.execute("INSERT INTO CITY VALUES(%s, %s, %s, %s);", [city_code1, city1, int(zip_code1), boarding_point1])
        cursor.execute("commit")
        cursor.close()
        con.close()
        City.destroy()
        messagebox.showinfo("Request successful", "Successfully added city.")

    City = tk.Tk()
    City.resizable(height = False, width = False)
    City.title('Travel Management System')
    City.geometry('720x500')

    tk.Label(City, text="City", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(City, text="City name").grid(column=0, row=1)
    tk.Label(City, text="City Code").grid(column=0, row=2)
    tk.Label(City, text="Zip Code").grid(column=0, row=3)
    tk.Label(City, text="Boarding Point").grid(column=0, row=4)



    city = tk.ttk.Entry(City)
    city.grid(column=1, row=1)
    city_code = tk.ttk.Entry(City)
    city_code.grid(column=1, row=2)
    zip_code = tk.ttk.Entry(City)
    zip_code.grid(column=1, row=3)
    boarding_point = tk.ttk.Entry(City)
    boarding_point.grid(column=1, row=4)


    tk.ttk.Button(City, text="Submit", command=insert_city).grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        City.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        City.grid_columnconfigure(i,  weight =1)

    City.mainloop()
