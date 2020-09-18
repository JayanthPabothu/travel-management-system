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

    else:
        cursor.execute("SELECT FLIGHT_NO, JOURNEY_ID FROM JOURNEY_FLIGHT WHERE JOURNEY_DATE=%s AND JOURNEY_STATUS=1;", [str(date)])
        records = cursor.fetchall()

        if len(records)==0:
            messagebox.showwarning("Record not found!", "No flights available for the given journey details.")
        else:

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

            final_dict={
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

            for i in records:
                new_dict[i[0]] = i[1]
            print(new_dict)

            cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(source)])
            record = cursor.fetchmany(size=1)
            data_dict['start_city']=str(record[0][0])
            data_dict['start_airport']=str(record[0][1])
            final_dict['start_city']=str(record[0][0])
            final_dict['start_airport']=str(record[0][1])

            cursor.execute("SELECT CITY_NAME, AIRPORT FROM CITY WHERE CITY_CODE=%s", [str(dest)])
            record = cursor.fetchmany(size=1)
            data_dict['dest_city']=str(record[0][0])
            data_dict['dest_airport']=str(record[0][1])
            final_dict['dest_city']=str(record[0][0])
            final_dict['dest_airport']=str(record[0][1])

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

            curr_time = datetime.datetime.now()
            hrs = curr_time.hour
            mins = curr_time.minute
            counter=0
            print(str(date)[8:], datetime.datetime.today().strftime('%d'), int((data_dict['start_time'][0])[0:2]), int((data_dict['start_time'][0])[3:]))
            for i in range(len(data_dict['flight_id'])):
                if(str(date)[8:] > datetime.datetime.today().strftime('%d')):
                    final_dict['flight_id'].append(data_dict['flight_id'][i])
                    final_dict['comp_name'].append(data_dict['comp_name'][i])
                    final_dict['start_time'].append(data_dict['start_time'][i])
                    final_dict['duration'].append(data_dict['duration'][i])
                    final_dict['model_name'].append(data_dict['model_name'][i])
                    # tk.Label(scrollable_frame, text=data_dict['comp_name'][i], font=font20).grid(column=0, row=0+(6*i), padx=70)
                    #
                    # tk.Label(scrollable_frame, text=data_dict['start_city'], font=font15).grid(column=0, row=1+(6*i))
                    # tk.Label(scrollable_frame, text=data_dict['start_time'][i], font=font30).grid(column=0, row=2+(6*i))
                    # tk.Label(scrollable_frame, text=data_dict['start_airport'], font=font10).grid(column=0, row=3+(6*i))
                    #
                    # tk.Label(scrollable_frame, text=data_dict['duration'][i], font=font10).grid(column=2, row=1+(6*i), sticky="S")
                    # tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i))
                    #
                    # tk.Label(scrollable_frame, text=data_dict['model_name'][i], font=font10).grid(column=4, row=0+(6*i), padx=70)
                    # tk.Label(scrollable_frame, text=data_dict['dest_city'], font=font15).grid(column=4, row=1+(6*i))
                    # tk.Label(scrollable_frame, text=data_dict['end_time'][i], font=font30).grid(column=4, row=2+(6*i))
                    # tk.Label(scrollable_frame, text=data_dict['dest_airport'], font=font10).grid(column=4, row=3+(6*i))
                    # tk.Label(scrollable_frame, text=data_dict['flight_id'][i], font=font10).grid(column=2, row=3+(6*i), sticky="N")
                    #
                    # tk.ttk.Button(scrollable_frame, text="Book now", command=partial(get_payment, data_dict['flight_id'][i], user_id, new_dict[data_dict['flight_id'][i]])).grid(column=2, row=4+(6*i), pady=(10, 70))
                    counter = counter+1
                elif(str(date)[8:] == datetime.datetime.today().strftime('%d')):
                    if(int((data_dict['start_time'][i])[0:2]) > hrs):
                        counter = counter+1
                        final_dict['flight_id'].append(data_dict['flight_id'][i])
                        final_dict['comp_name'].append(data_dict['comp_name'][i])
                        final_dict['start_time'].append(data_dict['start_time'][i])
                        final_dict['duration'].append(data_dict['duration'][i])
                        final_dict['model_name'].append(data_dict['model_name'][i])
                        final_dict['end_time'].append(data_dict['end_time'][i])
                    elif(int((data_dict['start_time'][i])[0:2]) == hrs):
                        if(int((data_dict['start_time'][i])[3:]) > mins):
                            counter = counter+1
                            final_dict['flight_id'].append(data_dict['flight_id'][i])
                            final_dict['comp_name'].append(data_dict['comp_name'][i])
                            final_dict['start_time'].append(data_dict['start_time'][i])
                            final_dict['duration'].append(data_dict['duration'][i])
                            final_dict['model_name'].append(data_dict['model_name'][i])
                            final_dict['end_time'].append(data_dict['end_time'][i])
                            # tk.Label(scrollable_frame, text=data_dict['comp_name'][i], font=font20).grid(column=0, row=0+(6*i), padx=70)
                            #
                            # tk.Label(scrollable_frame, text=data_dict['start_city'], font=font15).grid(column=0, row=1+(6*i))
                            # tk.Label(scrollable_frame, text=data_dict['start_time'][i], font=font30).grid(column=0, row=2+(6*i))
                            # tk.Label(scrollable_frame, text=data_dict['start_airport'], font=font10).grid(column=0, row=3+(6*i))
                            #
                            # tk.Label(scrollable_frame, text=data_dict['duration'][i], font=font10).grid(column=2, row=1+(6*i), sticky="S")
                            # tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i))
                            #
                            # tk.Label(scrollable_frame, text=data_dict['model_name'][i], font=font10).grid(column=4, row=0+(6*i), padx=70)
                            # tk.Label(scrollable_frame, text=data_dict['dest_city'], font=font15).grid(column=4, row=1+(6*i))
                            # tk.Label(scrollable_frame, text=data_dict['end_time'][i], font=font30).grid(column=4, row=2+(6*i))
                            # tk.Label(scrollable_frame, text=data_dict['dest_airport'], font=font10).grid(column=4, row=3+(6*i))
                            # tk.Label(scrollable_frame, text=data_dict['flight_id'][i], font=font10).grid(column=2, row=3+(6*i), sticky="N")
                            #
                            # tk.ttk.Button(scrollable_frame, text="Book now", command=partial(get_payment, data_dict['flight_id'][i], user_id, new_dict[data_dict['flight_id'][i]])).grid(column=2, row=4+(6*i), pady=(10, 70))
            if (counter == 0):
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
                print(final_dict)

                for i in range(len(final_dict['flight_id'])):
                    tk.Label(scrollable_frame, text=final_dict['comp_name'][i], font=font20).grid(column=0, row=0+(6*i), padx=70)

                    tk.Label(scrollable_frame, text=final_dict['start_city'], font=font15).grid(column=0, row=1+(6*i))
                    tk.Label(scrollable_frame, text=final_dict['start_time'][i], font=font30).grid(column=0, row=2+(6*i))
                    tk.Label(scrollable_frame, text=final_dict['start_airport'], font=font10).grid(column=0, row=3+(6*i))

                    tk.Label(scrollable_frame, text=final_dict['duration'][i], font=font10).grid(column=2, row=1+(6*i), sticky="S")
                    tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i))

                    tk.Label(scrollable_frame, text=final_dict['model_name'][i], font=font10).grid(column=4, row=0+(6*i), padx=70)
                    tk.Label(scrollable_frame, text=final_dict['dest_city'], font=font15).grid(column=4, row=1+(6*i))
                    tk.Label(scrollable_frame, text=final_dict['end_time'][i], font=font30).grid(column=4, row=2+(6*i))
                    tk.Label(scrollable_frame, text=final_dict['dest_airport'], font=font10).grid(column=4, row=3+(6*i))
                    tk.Label(scrollable_frame, text=final_dict['flight_id'][i], font=font10).grid(column=2, row=3+(6*i), sticky="N")

                    tk.ttk.Button(scrollable_frame, text="Book now", command=partial(get_payment, final_dict['flight_id'][i], user_id, new_dict[final_dict['flight_id'][i]])).grid(column=2, row=4+(6*i), pady=(10, 70))

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
