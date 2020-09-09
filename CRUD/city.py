import tkinter as tk
from tkinter import ttk

def crud_city():

    City = tk.Tk()
    City.resizable(height = False, width = False)
    City.title('Travel Management System')
    City.geometry('720x500')

    tk.Label(City, text="City", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(City, text="City name").grid(column=0, row=1)
    tk.Label(City, text="Zip Code").grid(column=0, row=2)
    tk.Label(City, text="Boarding Point").grid(column=0, row=3)



    tk.ttk.Entry(City).grid(column=1, row=1)
    tk.ttk.Entry(City).grid(column=1, row=2)
    tk.ttk.Entry(City).grid(column=1, row=3)


    tk.ttk.Button(City, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        City.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        City.grid_columnconfigure(i,  weight =1)

    City.mainloop()
