import tkinter as tk
from tkinter import ttk
import datetime
import booking
import mysql.connector as mysql
from tkinter import messagebox

def journey_screen():


    def search_booking():
        source = start_city_options.get()
        dest = dest_city_options.get()
        mode = mode_of_trans_options.get()
        date = date_options.get()
        booking.booking_run(source, dest, mode, date)


    journey = tk.Tk()
    journey.resizable(height = False, width = False)
    journey.title('Travel Management System')
    journey.geometry('720x500')

    heading = tk.Label(journey, text="Select your Journey", font=('Helvetica', '25'))

    # ---------Creating labels----------
    start_city = tk.Label(journey, text="Source City")
    dest_city = tk.Label(journey, text="Destination City")
    mode_of_trans = tk.Label(journey, text="Mode of journey")
    date = tk.Label(journey, text="Date of journey")

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="TMS"
        )
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT START_CITY FROM ROUTE")
    records = cursor.fetchall()
    n_start = tk.StringVar()
    start_city_options = ttk.Combobox(journey, width = 20, textvariable = n_start)
    start_city_options['values'] = [
                              city[0] for city in records
                            ]
    start_city_options.current(0)

    cursor.execute("SELECT DISTINCT DEST_CITY FROM ROUTE")
    records = cursor.fetchall()
    n_dest = tk.StringVar()
    dest_city_options = ttk.Combobox(journey, width = 20, textvariable = n_dest)
    dest_city_options['values'] = [
                            city[0] for city in records
                            ]


    dest_city_options.current(1)
    cursor.close()
    con.close()

    n_mode = tk.StringVar()
    mode_of_trans_options = ttk.Combobox(journey, width = 20, textvariable = n_mode)
    mode_of_trans_options['values'] = (
                                'Flight',
                                'Bus',
                                'Car'
                            )
    mode_of_trans_options.current(0)

    x = datetime.datetime.now()
    list_1 = []
    list_1.append(str(x.strftime("%d"))+'-'+str(x.strftime("%b"))+'-'+str(x.strftime("%Y")))
    for i in range(0, 6):
        x = x + datetime.timedelta(days=1)
        list_1.append(str(x.strftime("%d"))+'-'+str(x.strftime("%b"))+'-'+str(x.strftime("%Y")))

    n_date = tk.StringVar()
    date_options = ttk.Combobox(journey, width = 20, textvariable = n_date)
    date_options['values'] = (
                    list_1[0],
                    list_1[1],
                    list_1[2],
                    list_1[3],
                    list_1[4],
                    list_1[5],
                    list_1[6],
                )

    date_options.current(0)

    get_details = tk.ttk.Button(journey, text="Get Details", command=search_booking)


    # ---------Placing on grid---------
    heading.grid(column=0, row=0, columnspan=2)
    start_city.grid(column=0, row=1)
    dest_city.grid(column=0, row=2)
    mode_of_trans.grid(column=0, row=3)
    date.grid(column=0, row=4)

    start_city_options.grid(column=1, row=1)
    dest_city_options.grid(column=1, row=2)
    mode_of_trans_options.grid(column=1, row=3)
    date_options.grid(column=1, row=4)
    get_details.grid(column=0, row=5, columnspan=2)


    # Makes the widgets rsponsive and centered
    n_rows = 8
    n_columns = 2
    for i in range(n_rows):
        journey.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        journey.grid_columnconfigure(i,  weight =1)

    journey.mainloop()
# 
# journey_screen()
