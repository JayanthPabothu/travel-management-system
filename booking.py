import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import mysql.connector as mysql
from mysql.connector import Error
from functools import partial
from tkinter import messagebox
import pay
import journey as j
import datetime

def convert_timedelta(duration, code):
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    if code==1:
        return str(hours)+":"+str(minutes)
    else:
        return str(hours)+"h "+str(minutes)+"m"

def booking_screen(source, dest, date, user_id, journey):


    def on_closing():
        root.destroy()
        j.journey_screen(user_id)

    def get_payment(flight_id, user_id, journey_id):
        root.destroy()
        pay.pay_screen(flight_id, user_id, journey_id)

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="FMS",
            )
    cursor = con.cursor()
    cursor.execute("SELECT ROUTE_ID FROM ROUTE WHERE START_CITY=%s AND DEST_CITY=%s", [source, dest])
    routes = cursor.fetchall()
    if len(routes)==0:
        messagebox.showwarning("Record not found!", "No flights available for the given journey details.")
        root.destroy()
        j.journey_screen(user_id)



    else:
        cursor.execute("SELECT FLIGHT_NO, JOURNEY_ID FROM JOURNEY_FLIGHT WHERE JOURNEY_DATE=%s AND JOURNEY_STATUS=1;", [str(date)])
        records = cursor.fetchall()
        flight_nos = []
        time_values = []
        curr_time = datetime.datetime.now()
        hrs = curr_time.hour
        mins = curr_time.minute
        for i in records:
            flight_nos.append(i[0])
        for flight in flight_nos:
            cursor.execute("SELECT DEPARTURE_TIME FROM FLIGHT WHERE FLIGHT_NO = %s", [flight])
            time_values.append(cursor.fetchall()[0][0])
        for i in range(len(flight_nos)):
            if (time_values[i].seconds//3600 <= hrs):   # Hours check
                if (((time_values[i]).seconds//60)%60 <= mins ):    # Min check
                    print("Deleting data")
                    records.pop(i)


        if len(records)==0:
            messagebox.showwarning("Record not found!", "No flights available for the given journey details.")
        else:
            journey.destroy()
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

            canvas.configure(yscrollcommand=scrollbar.set)
            result_box = []
            no_of_results = 10
            ini_col = 0
            ini_row = 1

            font10 = Font(family='Arial', size=10)
            font15 = Font(family='Arial', size=15)
            font20 = Font(family='Arial', size=20)
            font30 = Font(family='Arial', size=30, weight='bold')

            data_dict = {
                'flight_id':[],
                'model_name':[],
                'start_city':'',
                'dest_city':'',
                'start_time':[],
                'duration':[],
                'end_time':[],
                'comp_name':[],
                'start_airport':'',
                'dest_airport':''
            }
            new_dict = {}
            for i in records:
                new_dict[i[0]] = i[1]
            print(new_dict)

            cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(source)])
            record = cursor.fetchmany(size=1)
            data_dict['start_city']=str(record[0][0])
            data_dict['start_airport']=str(record[0][1])

            cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(dest)])
            record = cursor.fetchmany(size=1)
            data_dict['dest_city']=str(record[0][0])
            data_dict['dest_airport']=str(record[0][1])

            data_dict['flight_id']=[id[0] for id in records]
            data_dict['journey_id']=[id[1] for id in records]
            format_strings = ','.join(['%s'] * len(data_dict['flight_id']))
            cursor.execute(f"SELECT F.FLIGHT_NO, F.MODEL_NAME, C.COMPANY_NAME, F.DEPARTURE_TIME, R.TIME_TAKEN FROM (FLIGHT F INNER JOIN COMPANY C ON F.COMPANY_ID=C.COMPANY_ID) INNER JOIN ROUTE R ON F.ROUTE_ID=R.ROUTE_ID WHERE R.START_CITY='{source}' AND R.DEST_CITY='{dest}' AND FLIGHT_NO IN (%s);" %format_strings, tuple(data_dict['flight_id']))
            records = cursor.fetchall()
            data_dict['flight_id']=[id[0] for id in records]
            data_dict['model_name']=[id[1] for id in records]
            data_dict['comp_name']=[id[2] for id in records]
            data_dict['start_time']=[id[3] for id in records]
            data_dict['duration']=[id[4] for id in records]
            data_dict['end_time']=[a+b for a, b in zip(data_dict['start_time'], data_dict['duration'])]
            data_dict['start_time']=list(map(convert_timedelta, data_dict['start_time'], [1]*len(data_dict['start_time'])))
            data_dict['duration']=list(map(convert_timedelta, data_dict['duration'], [2]*len(data_dict['duration'])))
            data_dict['end_time']=list(map(convert_timedelta, data_dict['end_time'], [1]*len(data_dict['end_time'])))
            print(data_dict)
            for i in range(len(data_dict['flight_id'])):

                tk.Label(scrollable_frame, text=data_dict['comp_name'][i], font=font20).grid(column=0, row=0+(6*i), padx=70)

                tk.Label(scrollable_frame, text=data_dict['start_city'], font=font15).grid(column=0, row=1+(6*i))
                tk.Label(scrollable_frame, text=data_dict['start_time'][i], font=font30).grid(column=0, row=2+(6*i))
                tk.Label(scrollable_frame, text=data_dict['start_airport'], font=font10).grid(column=0, row=3+(6*i))

                tk.Label(scrollable_frame, text=data_dict['duration'][i], font=font10).grid(column=2, row=1+(6*i), sticky="S")
                tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i))

                tk.Label(scrollable_frame, text=data_dict['model_name'][i], font=font10).grid(column=4, row=0+(6*i), padx=70)
                tk.Label(scrollable_frame, text=data_dict['dest_city'], font=font15).grid(column=4, row=1+(6*i))
                tk.Label(scrollable_frame, text=data_dict['end_time'][i], font=font30).grid(column=4, row=2+(6*i))
                tk.Label(scrollable_frame, text=data_dict['dest_airport'], font=font10).grid(column=4, row=3+(6*i))
                tk.Label(scrollable_frame, text=data_dict['flight_id'][i], font=font10).grid(column=2, row=3+(6*i), sticky="N")

                tk.ttk.Button(scrollable_frame, text="Book now", command=partial(get_payment, data_dict['flight_id'][i], user_id, new_dict[data_dict['flight_id'][i]])).grid(column=2, row=4+(6*i), pady=(10, 70))

            n_rows = 30
            n_columns = 10
            for i in range(n_rows):
                root.grid_rowconfigure(i,  weight =1)
            for i in range(n_columns):
                root.grid_columnconfigure(i,  weight =1)

            container.pack()
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            root.protocol("WM_DELETE_WINDOW", on_closing)

            root.mainloop()
