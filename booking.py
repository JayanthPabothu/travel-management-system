import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox

def convert_timedelta(duration, code):
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    if code==1:
        return str(hours)+":"+str(minutes)
    else:
        return str(hours)+"h "+str(minutes)+"m"

def booking_screen():

    con = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="FMS",
            port = 3306
            )
    cursor = con.cursor()
    cursor.execute("SELECT FLIGHT_NO FROM JOURNEY_FLIGHT WHERE JOURNEY_DATE=%s AND JOURNEY_STATUS=1;", ['2020-09-15'])
    records = cursor.fetchall()
    if len(records)==0:
        messagebox.showwarning("Record not found!", "No flights available for the given journey details.")
    else:    
        root = tk.Tk()
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
            'start_city':'Mumbai',
            'dest_city':'Delhi',
            'start_time':[],
            'duration':[],
            'end_time':[],
            'comp_name':[],
            'start_airport':'Chhatrapati Shivaji Airport',
            'dest_airport':'Indira Gandhi Airport'
        }
        #cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(BOM)])
        #record = cursor.fetchmany(size=1)
        #data_dict['start_city']=str(record[0][0])
        #data_dict['start_airport']=str(record[0][1])

        # cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(DEL)])
        # record = cursor.fetchmany(size=1)
        # data_dict['dest_city']=str(record[0][0])
        # data_dict['dest_airport']=str(record[0][1])

        data_dict['flight_id']=[id[0] for id in records]
        format_strings = ','.join(['%s'] * len(data_dict['flight_id']))
        cursor.execute("SELECT F.FLIGHT_NO, F.MODEL_NAME, C.COMPANY_NAME, F.DEPARTURE_TIME, R.TIME_TAKEN FROM (FLIGHT F INNER JOIN COMPANY C ON F.COMPANY_ID=C.COMPANY_ID) INNER JOIN ROUTE R ON F.ROUTE_ID=R.ROUTE_ID WHERE R.START_CITY='BOM' AND R.DEST_CITY='DEL' AND FLIGHT_NO IN (%s);" %format_strings, tuple(data_dict['flight_id']))
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

            tk.ttk.Button(scrollable_frame, text="Book now").grid(column=2, row=4+(6*i), pady=(10, 70))
    # for i in range(0, no_of_results):
    #
    #     tk.Label(scrollable_frame, text="Air India").grid(column=0, row=(1+(i*4)))
    #     tk.Label(scrollable_frame, text="Journey Begins").grid(column=0, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Journey Ends").grid(column=2, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Duration").grid(column=1, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Cost").grid(column=3, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="00:00").grid(column=0, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="12:10").grid(column=2, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="12h 10m").grid(column=1, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="Rs.5000").grid(column=3, row=3+(i*4))
    #
    #     tk.Label(scrollable_frame, text="Seats Available: 69").grid(column=1, row=4+(i*4))
    #     n_seat_type = tk.StringVar()
    #     seat_type = ttk.Combobox(scrollable_frame, width = 25, textvariable = n_seat_type)
    #     seat_type['values'] =             (
    #                               '------Select seat type------',
    #                               'Economy',
    #                               'Business',
    #                             )
    #     seat_type.current(0)
    #
    #     submit = tk.ttk.Button(scrollable_frame, text="Select")
    #     seat_type.grid(column=0, row=4+(i*4))
    #     submit.grid(column=2, row=4+(i*4))

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
booking_screen()
