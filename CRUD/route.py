import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_route():

    def insert_route():

        start_city1 = start_city.get()
        dest_city1 = dest_city.get()
        time_taken1 = time_taken.get()

        if(start_city1 == dest_city1):
            messagebox.showwarning("Invalid request", "Start city and destination city cannot be same.")
        else:

            con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="TMS"
                )
            cursor = con.cursor()
            args = cursor.callproc("CHECK_ROUTE_EXISTS", (start_city1, dest_city1, time_taken1, None))
            if(args[-1] == 0):

                cursor.execute("INSERT INTO ROUTE(START_CITY, DEST_CITY, TIME_TAKEN) VALUES(%s, %s, %s);", [start_city1, dest_city1, time_taken1])

                messagebox.showinfo("Request successful", "Successfully added route.")
                cursor.execute("commit")
                route.destroy()
            else:
                messagebox.showwarning("Invalid request", "Route already exists.")

            cursor.close()
            con.close()

    route = tk.Tk()
    route.resizable(height = False, width = False)
    route.title('Travel Management System')
    route.geometry('720x500')


    start_city = tk.ttk.Entry(route)


    dest_city = tk.ttk.Entry(route)



    time_taken = tk.ttk.Entry(route)
    time_taken.grid(column=2, row=2)

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="TMS"
        )
    cursor = con.cursor()
    cursor.execute("SELECT CITY_CODE FROM CITY;")

    records = cursor.fetchall()
    n_start_city = tk.StringVar()
    start_city = ttk.Combobox(route, width = 25, textvariable = n_start_city)
    start_city['values'] = [
                        (city[0]) for city in records
                                ]
    start_city.current(0)

    n_dest_city = tk.StringVar()

    dest_city = ttk.Combobox(route, width = 25, textvariable = n_dest_city)
    dest_city['values'] = [
                        (city[0]) for city in records
                                ]
    dest_city.current(0)
    start_city.grid(column=0, row=2)
    dest_city.grid(column=1, row=2)
    cursor.close()
    con.close()

    tk.Label(route, text="Route", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=4)
    tk.Label(route, text="Start City").grid(column=0, row=1)
    tk.Label(route, text="Destination city").grid(column=1, row=1)
    tk.Label(route, text="Time taken").grid(column=2, row=1)


    tk.ttk.Button(route, text="Submit", command=insert_route).grid(column=0, row=3, columnspan=4)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 3
    for i in range(n_rows):
        route.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        route.grid_columnconfigure(i,  weight =1)

    route.mainloop()
