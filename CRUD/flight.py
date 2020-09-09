import tkinter as tk
from tkinter import ttk

def crud_flight():

    flight = tk.Tk()
    flight.resizable(height = False, width = False)
    flight.title('Travel Management System')
    flight.geometry('720x500')

    tk.Label(flight, text="Flight", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(flight, text="Model name").grid(column=0, row=1)
    tk.Label(flight, text="Rating").grid(column=0, row=2)
    tk.Label(flight, text="Day set").grid(column=0, row=3)
    tk.Label(flight, text="Route Id").grid(column=0, row=4)
    tk.Label(flight, text="City Hierarchy").grid(column=0, row=5)
    tk.Label(flight, text="Company Id").grid(column=0, row=6)
    tk.Label(flight, text="Amenity Id").grid(column=0, row=7)

    tk.Label(flight, text="Number of First class seats").grid(column=0, row=8)
    tk.Label(flight, text="Number of Economy seats").grid(column=0, row=9)
    tk.Label(flight, text="Number of Business seats").grid(column=0, row=10)
    tk.Label(flight, text="Number of Premium seats").grid(column=0, row=11)

    tk.ttk.Entry(flight).grid(column=1, row=1)
    tk.ttk.Entry(flight).grid(column=1, row=2)
    tk.ttk.Entry(flight).grid(column=1, row=3)
    tk.ttk.Entry(flight).grid(column=1, row=4)
    tk.ttk.Entry(flight).grid(column=1, row=5)
    tk.ttk.Entry(flight).grid(column=1, row=6)
    tk.ttk.Entry(flight).grid(column=1, row=7)
    tk.ttk.Entry(flight).grid(column=1, row=8)
    tk.ttk.Entry(flight).grid(column=1, row=9)
    tk.ttk.Entry(flight).grid(column=1, row=10)
    tk.ttk.Entry(flight).grid(column=1, row=11)


    tk.ttk.Button(flight, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        flight.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        flight.grid_columnconfigure(i,  weight =1)

    flight.mainloop()
