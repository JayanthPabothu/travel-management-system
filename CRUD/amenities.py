import tkinter as tk
from tkinter import ttk

def crud_amenities():

    amenities = tk.Tk()
    amenities.resizable(height = False, width = False)
    amenities.title('Travel Management System')
    amenities.geometry('720x500')

    tk.Label(amenities, text="Amenities", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(amenities, text="Amenity Set").grid(column=0, row=1)
    tk.Label(amenities, text="Rating").grid(column=0, row=2)
    tk.Label(amenities, text="Day set").grid(column=0, row=3)
    tk.Label(amenities, text="Route Id").grid(column=0, row=4)



    tk.ttk.Entry(amenities).grid(column=1, row=1)
    tk.ttk.Entry(amenities).grid(column=1, row=2)
    tk.ttk.Entry(amenities).grid(column=1, row=3)
    tk.ttk.Entry(amenities).grid(column=1, row=4)


    tk.ttk.Button(amenities, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        amenities.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        amenities.grid_columnconfigure(i,  weight =1)

    amenities.mainloop()
