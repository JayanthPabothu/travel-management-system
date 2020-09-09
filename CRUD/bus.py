import tkinter as tk
from tkinter import ttk

def crud_bus():

    Bus = tk.Tk()
    Bus.resizable(height = False, width = False)
    Bus.title('Travel Management System')
    Bus.geometry('720x500')

    tk.Label(Bus, text="Bus", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(Bus, text="Model Name").grid(column=0, row=1)
    tk.Label(Bus, text="Start Time").grid(column=0, row=2)
    tk.Label(Bus, text="Rating").grid(column=0, row=3)
    tk.Label(Bus, text="Day set").grid(column=0, row=4)
    tk.Label(Bus, text="Route Id").grid(column=0, row=5)
    tk.Label(Bus, text="City Hierarchy").grid(column=0, row=6)
    tk.Label(Bus, text="Company Id").grid(column=0, row=7)
    tk.Label(Bus, text="Amenity Id").grid(column=0, row=8)

    tk.Label(Bus, text="No of Sleeper seats").grid(column=0, row=9)
    tk.Label(Bus, text="No of Seater seats").grid(column=0, row=10)

    tk.ttk.Entry(Bus).grid(column=1, row=1)
    tk.ttk.Entry(Bus).grid(column=1, row=2)
    tk.ttk.Entry(Bus).grid(column=1, row=3)
    tk.ttk.Entry(Bus).grid(column=1, row=4)
    tk.ttk.Entry(Bus).grid(column=1, row=5)
    tk.ttk.Entry(Bus).grid(column=1, row=6)
    tk.ttk.Entry(Bus).grid(column=1, row=7)
    tk.ttk.Entry(Bus).grid(column=1, row=8)
    tk.ttk.Entry(Bus).grid(column=1, row=9)
    tk.ttk.Entry(Bus).grid(column=1, row=10)



    tk.ttk.Button(Bus, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        Bus.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        Bus.grid_columnconfigure(i,  weight =1)

    Bus.mainloop()
