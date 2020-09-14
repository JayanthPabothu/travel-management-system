import tkinter as tk
from tkinter import ttk
import datetime
import booking
from functools import partial
import mysql.connector as mysql
from tkinter import messagebox
from tkinter.font import Font



def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def journey_screen(user_id):


    def search_booking():
        source = start_city_options.get()
        dest = dest_city_options.get()
        #mode = mode_of_trans_options.get()
        date = date_options.get()
        x = datetime.datetime.strptime(date, "%d-%b-%Y")
        date = str(x.strftime("%Y"))+'-'+str(x.strftime("%m"))+'-'+str(x.strftime("%d"))
        booking.booking_screen(source, dest, date, user_id, journey)


    journey = tk.Tk()
    journey.resizable(height = False, width = False)
    journey.title('Travel Management System')
    journey.geometry('720x420')
    background = tk.PhotoImage(file='Images/Travel.png')
    background_label = tk.Label(journey,  image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    adam = Font(family="ADAM.CG PRO", size=20)

    heading = tk.Label(journey, text="Select your Journey", font=('Helvetica', '25'))

    # ---------Creating labels----------
    start_city = tk.Label(journey, text="FROM" ,fg='white', font=(15))
    start_city.configure(bg=_from_rgb((9, 15, 134)))

    dest_city = tk.Label(journey, text="TO" ,fg='white', font=(15))
    dest_city.configure(bg=_from_rgb((9, 15, 134)))

    date = tk.Label(journey, text="DEPARTURE" ,fg='white', font=(15))
    date.configure(bg=_from_rgb((9, 15, 134)))

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="FMS",
        )
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT START_CITY FROM ROUTE")
    records = cursor.fetchall()
    n_start = tk.StringVar()
    start_city_options = ttk.Combobox(journey, width = 8, textvariable = n_start)
    start_city_options['values'] = [
                              city[0] for city in records
                            ]
    start_city_options.current(0)

    cursor.execute("SELECT DISTINCT DEST_CITY FROM ROUTE")
    records = cursor.fetchall()
    n_dest = tk.StringVar()
    dest_city_options = ttk.Combobox(journey, width = 8, textvariable = n_dest)
    dest_city_options['values'] = [
                            city[0] for city in records
                            ]


    dest_city_options.current(0)
    cursor.close()
    con.close()

    x = datetime.datetime.now()
    list_1 = []
    list_1.append(str(x.strftime("%d"))+'-'+str(x.strftime("%b"))+'-'+str(x.strftime("%Y")))
    for i in range(0, 6):
        x = x + datetime.timedelta(days=1)
        list_1.append(str(x.strftime("%d"))+'-'+str(x.strftime("%b"))+'-'+str(x.strftime("%Y")))

    n_date = tk.StringVar()
    date_options = ttk.Combobox(journey, width = 12, textvariable = n_date)
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

    get_details = tk.ttk.Button(journey, text="Search", command=search_booking)


    # ---------Placing on grid---------
    start_city.place(x=180, y=150)
    dest_city.place(x=310, y=150)
    date.place(x=410, y=150)

    start_city_options.place(x=180, y=190)
    dest_city_options.place(x=310, y=190)
    date_options.place(x=425, y=190)
    get_details.place(x=310, y=250)


    # Makes the widgets rsponsive and centered
    n_rows = 8
    n_columns = 2
    for i in range(n_rows):
        journey.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        journey.grid_columnconfigure(i,  weight =1)

    journey.mainloop()
#
# journey_screen(1)
