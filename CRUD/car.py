import tkinter as tk
from tkinter import ttk

def crud_car():

    Car = tk.Tk()
    Car.resizable(height = False, width = False)
    Car.title('Travel Management System')
    Car.geometry('720x500')

    tk.Label(Car, text="Car", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(Car, text="Model Name").grid(column=0, row=1)
    tk.Label(Car, text="Start Time").grid(column=0, row=2)
    tk.Label(Car, text="Rating").grid(column=0, row=3)
    tk.Label(Car, text="Day set").grid(column=0, row=4)
    tk.Label(Car, text="Route Id").grid(column=0, row=5)
    tk.Label(Car, text="City Hierarchy").grid(column=0, row=6)
    tk.Label(Car, text="Company Id").grid(column=0, row=7)
    tk.Label(Car, text="Amenity Id").grid(column=0, row=8)


    tk.Label(Car, text="No of Seats").grid(column=0, row=9)

    tk.ttk.Entry(Car).grid(column=1, row=1)
    tk.ttk.Entry(Car).grid(column=1, row=2)
    tk.ttk.Entry(Car).grid(column=1, row=3)
    tk.ttk.Entry(Car).grid(column=1, row=4)
    tk.ttk.Entry(Car).grid(column=1, row=5)
    tk.ttk.Entry(Car).grid(column=1, row=6)
    tk.ttk.Entry(Car).grid(column=1, row=7)
    tk.ttk.Entry(Car).grid(column=1, row=8)
    tk.ttk.Entry(Car).grid(column=1, row=9)




    tk.ttk.Button(Car, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        Car.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        Car.grid_columnconfigure(i,  weight =1)

    Car.mainloop()
