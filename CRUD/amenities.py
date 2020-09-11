import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_amenities():


    def insert_amenities():
        amenities2 = amenities1.get()

        con = mysql.connect(
                host="localhost",
                user="root",
                password="testpassword",
                database="TMS"
            )
        cursor = con.cursor()
        cursor.execute("INSERT INTO AMENITIES(AMENITY_SET) VALUES(%s);", [amenities2])
        cursor.execute("commit")
        cursor.close()
        con.close()
        amenities.destroy()
        messagebox.showinfo("Request successful", "Successfully added amenities.")

    amenities = tk.Tk()
    amenities.resizable(height = False, width = False)
    amenities.title('Travel Management System')
    amenities.geometry('720x500')

    tk.Label(amenities, text="Amenities", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(amenities, text="Amenity Set").grid(column=0, row=1)



    amenities1 = tk.ttk.Entry(amenities)
    amenities1.grid(column=1, row=1)


    tk.ttk.Button(amenities, text="Submit", command=insert_amenities).grid(column=0, row=2, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        amenities.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        amenities.grid_columnconfigure(i,  weight =1)

    amenities.mainloop()
