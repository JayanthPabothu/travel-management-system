import tkinter as tk
from tkinter import ttk

def crud_route():

    route = tk.Tk()
    route.resizable(height = False, width = False)
    route.title('Travel Management System')
    route.geometry('720x500')

    tk.Label(route, text="Route", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(route, text="Time taken").grid(column=0, row=1)
    tk.Label(route, text="City code").grid(column=0, row=2)



    tk.ttk.Entry(route).grid(column=1, row=1)
    tk.ttk.Entry(route).grid(column=1, row=2)


    tk.ttk.Button(route, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        route.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        route.grid_columnconfigure(i,  weight =1)

    route.mainloop()
