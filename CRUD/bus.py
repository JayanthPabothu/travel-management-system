import tkinter as tk
from tkinter import ttk

def crud_bus():

    Bus = tk.Tk()
    Bus.resizable(height = False, width = False)
    Bus.title('Travel Management System')
    Bus.geometry('720x500')

    tk.Label(Bus, text="Bus", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(Bus, text="Vehicle ID").grid(column=0, row=1)
    tk.Label(Bus, text="Model Name").grid(column=0, row=2)
    tk.Label(Bus, text="Start Time").grid(column=0, row=3)
    tk.Label(Bus, text="Rating").grid(column=0, row=4)
    tk.Label(Bus, text="Price").grid(column=0, row=5)
    tk.Label(Bus, text="Route Id").grid(column=0, row=6)
    tk.Label(Bus, text="Company Id").grid(column=0, row=7)
    tk.Label(Bus, text="Amenity Id").grid(column=0, row=8)
    tk.Label(Bus, text="No of Sleeper seats").grid(column=0, row=9)
    tk.Label(Bus, text="No of Seater seats").grid(column=0, row=10)

    vehicle_id = tk.ttk.Entry(Bus)
    vehicle_id.grid(column=1, row=1)

    name = tk.ttk.Entry(Bus)
    name.grid(column=1, row=2)

    start_time = tk.ttk.Entry(Bus)
    start_time.grid(column=1, row=3)

    rating = tk.ttk.Entry(Bus)
    rating.grid(column=1, row=4)

    price = tk.ttk.Entry(Bus)
    price.grid(column=1, row=5)

    route_id = tk.ttk.Entry(Bus)
    route_id.grid(column=1, row=6)

    company_id = tk.ttk.Entry(Bus)
    company_id.grid(column=1, row=7)

    amenity = tk.ttk.Entry(Bus)
    amenity.grid(column=1, row=8)

    sleeper = tk.ttk.Entry(Bus)
    slepper.grid(column=1, row=9)

    seater = tk.ttk.Entry(Bus)
    seater.grid(column=1, row=10)



    tk.ttk.Button(Bus, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        Bus.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        Bus.grid_columnconfigure(i,  weight =1)

    Bus.mainloop()
