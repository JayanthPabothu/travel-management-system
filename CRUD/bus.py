import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_bus():

    def insert_bus():

        vehicle_id1 = vehicle_id.get()
        name1 = name.get()
        start_time1 = start_time.get()
        rating1 = rating.get()
        price1 = price.get()
        sleeper1 = sleeper.get()
        seater1 = seater.get()
        route_id1 = route_id.get()
        company_id1 = company_id.get()
        amenities1 = amenities.get()
        con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="TMS"
                )
        cursor = con.cursor()

        cursor.execute("SELECT COMPANY_ID FROM COMPANY WHERE COMPANY_NAME=%s", [company_id1])
        company_id1 = cursor.fetchall()[0][0]
        cursor.execute("INSERT INTO VEHICLE VALUES(%s, %s, %s, %s, %s, %s, %s, %s);", [vehicle_id1, name1, start_time1, price1, rating1, route_id1, company_id1, amenities1])
        cursor.execute("commit")
        cursor.execute("INSERT INTO BUS VALUES(%s, %s, %s);", [vehicle_id1, sleeper1, seater1])
        cursor.execute("commit")
        messagebox.showinfo("Request successful", "Successfully added Bus.")

        Bus.destroy()



    Bus = tk.Tk()
    Bus.resizable(height = False, width = False)
    Bus.title('Travel Management System')
    Bus.geometry('720x500')

    tk.Label(Bus, text="Bus", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(Bus, text="Vehicle ID").grid(column=0, row=1)
    tk.Label(Bus, text="Model Name").grid(column=0, row=2)
    tk.Label(Bus, text="Start Time").grid(column=0, row=3)
    tk.Label(Bus, text="Price").grid(column=0, row=4)
    tk.Label(Bus, text="Route Id").grid(column=0, row=5)
    tk.Label(Bus, text="Company Id").grid(column=0, row=6)
    tk.Label(Bus, text="Amenity Id").grid(column=0, row=7)
    tk.Label(Bus, text="No of Sleeper seats").grid(column=0, row=8)
    tk.Label(Bus, text="No of Seater seats").grid(column=0, row=9)

    vehicle_id = tk.ttk.Entry(Bus)
    vehicle_id.grid(column=1, row=1)

    name = tk.ttk.Entry(Bus)
    name.grid(column=1, row=2)

    start_time = tk.ttk.Entry(Bus)
    start_time.grid(column=1, row=3)


    price = tk.ttk.Entry(Bus)
    price.grid(column=1, row=4)



    sleeper = tk.ttk.Entry(Bus)
    sleeper.grid(column=1, row=8)

    seater = tk.ttk.Entry(Bus)
    seater.grid(column=1, row=9)


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
    cursor.execute("SELECT COMPANY_NAME FROM COMPANY;")
    records = cursor.fetchall()
    n_company_id = tk.StringVar()
    company_id = ttk.Combobox(Bus, width = 10, textvariable = n_company_id)
    company_id['values'] = [
                        company[0] for company in records
                                ]
    company_id.current(0)

    cursor.execute("SELECT AMENITY_ID FROM AMENITIES;")
    records = cursor.fetchall()
    n_amenities = tk.StringVar()
    amenities = ttk.Combobox(Bus, width = 10, textvariable = n_amenities)
    amenities['values'] = [
                        (amenity[0]) for amenity in records
                                ]
    amenities.current(0)




    route_id.grid(column=1, row=5)
    company_id.grid(column=1, row=6)
    amenities.grid(column=1, row=7)
    tk.ttk.Button(Bus, text="Submit", command=insert_bus).grid(column=0, row=12, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        Bus.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        Bus.grid_columnconfigure(i,  weight =1)

    Bus.mainloop()
