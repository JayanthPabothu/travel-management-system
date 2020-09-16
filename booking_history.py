import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import mysql.connector as mysql
from mysql.connector import Error
from functools import partial
from tkinter import messagebox

def history_screen(cust_id):

    con = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="FMS",
            port = 3306
            )

    dict_data = {
                    'journey_ids':[],
                    'date_book':[],
                    'date_journey':[],
                    'price':[],
                    'seat_type':[],
                    'seat_num':[],
                    'start':[],
                    'dest':[]
                }
    cursor = con.cursor()
    cursor.execute("SELECT JOURNEY_ID, DATE_OF_BOOKING, PRICE, SEAT_TYPE, SEAT_NO FROM BOOKS_FLIGHT WHERE CUSTOMER_ID=%s;", [cust_id])
    res = cursor.fetchall()
    if len(res)==0:
        messagebox.showwarning("Record not found!", "No bookings done yet.")
    else:
        dict_data['journey_ids']=[str(id[0]) for id in res]
        dict_data['date_book']=[str(id[1]) for id in res]
        dict_data['price']=[str(id[2]) for id in res]
        dict_data['seat_type']=[str(id[3]) for id in res]
        dict_data['seat_num']=[str(id[4]) for id in res]

        for journey in dict_data['journey_ids']:
            cursor.execute("SELECT START_CITY, DEST_CITY FROM ROUTE WHERE ROUTE_ID=(SELECT ROUTE_ID FROM FLIGHT WHERE FLIGHT_NO=(SELECT FLIGHT_NO FROM JOURNEY_FLIGHT WHERE JOURNEY_ID=%s));", [journey])
            cities=cursor.fetchmany(size=1)
            dict_data["start"].append(cities[0][0])
            dict_data["dest"].append(cities[0][1])
            cursor.execute("SELECT JOURNEY_DATE FROM JOURNEY_FLIGHT WHERE JOURNEY_ID=%s;", [journey])
            jdate=cursor.fetchmany(size=1)
            dict_data["date_journey"].append(jdate[0][0])
        
        print(dict_data)

        
        root = tk.Tk()
        root.title('Flight Management System')
        root.geometry('720x420')
        root.resizable(height = False, width = False)
        container = tk.Frame(root, width=720, height=420, bg="blue")
        canvas = tk.Canvas(container, width=700, height=400)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        font10 = Font(family='Arial', size=10)
        font15 = Font(family='Arial', size=15)
        font20 = Font(family='Arial', size=20)
        font30 = Font(family='Arial', size=30, weight='bold')

        print(dict_data)
        for i in range(len(dict_data['journey_ids'])):
            tk.Label(scrollable_frame, text="Booking No: "+str(i+1), font=font20).grid(column=0, row=0+(6*i), padx=50)
            tk.Label(scrollable_frame, text="Journey ID: "+dict_data['journey_ids'][i], font=font15).grid(column=0, row=1+(6*i), padx=50)
            tk.Label(scrollable_frame, text="Date of Booking: "+dict_data['date_book'][i], font=font10).grid(column=4, row=1+(6*i))

            tk.Label(scrollable_frame, text=dict_data['start'][i], font=font15).grid(column=0, row=2+(6*i))
            tk.Label(scrollable_frame, text=dict_data['dest'][i], font=font15).grid(column=4, row=2+(6*i))
            tk.Label(scrollable_frame, text=dict_data['date_journey'][i]).grid(column=2, row=1+(6*i), padx=(0, 50))

            
            tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i), padx=(0, 50))
            tk.Label(scrollable_frame, text="Seat:   "+dict_data['seat_type'][i]+"   "+dict_data['seat_num'][i], font=font10).grid(column=2, row=3+(6*i), padx=(0, 50), pady=(0, 30))
            tk.Label(scrollable_frame, text="Price: "+dict_data['price'][i], font=font10).grid(column=0, row=3+(6*i), pady=(0, 30))
            #tk.Label(scrollable_frame, text=dict_data['seat_num'][i]).grid(column=4, row=0+(6*i), padx=70)
            
            
            # tk.Label(scrollable_frame, text=dict_data['dest_airport'], font=font10).grid(column=4, row=3+(6*i))
            # tk.Label(scrollable_frame, text=dict_data['flight_id'][i], font=font10).grid(column=2, row=3+(6*i), sticky="N")

        n_rows = 30
        n_columns = 10
        for i in range(n_rows):
            root.grid_rowconfigure(i,  weight =1)
        for i in range(n_columns):
            root.grid_columnconfigure(i,  weight =1)

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        root.mainloop()
history_screen(1)

