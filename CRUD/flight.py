import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_flight():

    flight = tk.Tk()
    flight.resizable(height = False, width = False)
    flight.title('Travel Management System')
    flight.geometry('720x500')

    tk.Label(flight, text="Flight", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(flight, text="Vehcle ID").grid(column=0, row=1)
    tk.Label(flight, text="Model name").grid(column=0, row=2)
    tk.Label(flight, text="Route Id").grid(column=0, row=3)
    tk.Label(flight, text="Company Id").grid(column=0, row=4)
    tk.Label(flight, text="Amenity Id").grid(column=0, row=5)
    tk.Label(flight, text="Start time").grid(column=0, row=6)
    tk.Label(flight, text="Rating").grid(column=0, row=7)
    tk.Label(flight, text="Price").grid(column=0, row=8)

    tk.Label(flight, text="Number of First class seats").grid(column=0, row=9)
    tk.Label(flight, text="Number of Economy seats").grid(column=0, row=10)
    tk.Label(flight, text="Number of Business seats").grid(column=0, row=11)
    tk.Label(flight, text="Number of Premium seats").grid(column=0, row=12)

    vehicle_id = tk.ttk.Entry(flight).grid(column=1, row=3)
    name = tk.ttk.Entry(flight).grid(column=1, row=1)

    rating = tk.ttk.Entry(flight).grid(column=1, row=2)
    tk.ttk.Entry(flight).grid(column=1, row=4)
    tk.ttk.Entry(flight).grid(column=1, row=5)
    tk.ttk.Entry(flight).grid(column=1, row=6)
    tk.ttk.Entry(flight).grid(column=1, row=7)
    tk.ttk.Entry(flight).grid(column=1, row=8)
    tk.ttk.Entry(flight).grid(column=1, row=9)
    tk.ttk.Entry(flight).grid(column=1, row=10)
    tk.ttk.Entry(flight).grid(column=1, row=11)

    vehicle_id = tk.ttk.Entry(Flight)
    vehicle_id.grid(column=1, row=1)

    name = tk.ttk.Entry(Flight)
    name.grid(column=1, row=2)

    start_time = tk.ttk.Entry(Flight)
    start_time.grid(column=1, row=6)

    rating = tk.ttk.Entry(Flight)
    rating.grid(column=1, row=7)

    price = tk.ttk.Entry(Flight)
    price.grid(column=1, row=8)

    tk.ttk.Button(flight, text="Submit").grid(column=0, row=13, columnspan=2)

    con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="TMS"
                )
    cursor = con.cursor()

    # Fetching route ids for dropdown
    cursor.execute("SELECT ROUTE_ID FROM ROUTE;")
    records = cursor.fetchall()
    n_route_id = tk.StringVar()
    route_id = ttk.Combobox(Bus, width = 10, textvariable = n_route_id)
    route_id['values'] = [
                        (route[0]) for route in records
                                ]
    route_id.current(0)

    # Fetching companyid for dropdown
    cursor.execute("SELECT COMPANY_ID FROM COMPANY;")
    records = cursor.fetchall()
    n_company_id = tk.StringVar()
    company_id = ttk.Combobox(Bus, width = 10, textvariable = n_company_id)
    company_id['values'] = [
                        company[0] for company in records
                                ]
    company_id.current(0)

    # Fetching for amenities
    cursor.execute("SELECT AMENITY_ID FROM AMENITIES;")
    records = cursor.fetchall()
    n_amenities = tk.StringVar()
    amenities = ttk.Combobox(Bus, width = 10, textvariable = n_amenities)
    amenities['values'] = [
                        (amenity[0]) for amenity in records
                                ]
    amenities.current(0)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        flight.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        flight.grid_columnconfigure(i,  weight =1)

    flight.mainloop()
