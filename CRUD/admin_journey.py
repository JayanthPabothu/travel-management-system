import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox

def crud_admin_journey():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="shobhit2000@",
    database="FMS"
    )

    def get_selected_row():
        global old_flight_no
        index = admin_journey_list.curselection()
        if (len(index) != 0):
            selected_tuple = admin_journey_list.get(index)
            flight_no.delete(0, tk.END)
            flight_no.insert(tk.END,selected_tuple[0])
            old_flight_no= flight_no.get()
            Model_name.delete(0, tk.END)
            Model_name.insert(tk.END, selected_tuple[1])
            Departure_time.delete(0, tk.END)
            Departure_time.insert(tk.END, selected_tuple[2])
            Route.delete(0, tk.END)
            Route.insert(tk.END, selected_tuple[3])
            Price.delete(0, tk.END)
            Price.insert(tk.END, selected_tuple[4])
            Baggage.delete(0, tk.END)
            Baggage.insert(tk.END, selected_tuple[5])
            Firstclass.delete(0, tk.END)
            Firstclass.insert(tk.END, selected_tuple[6])
            Economy.delete(0, tk.END)
            Economy.insert(tk.END, selected_tuple[7])
            Business.delete(0, tk.END)
            Business.insert(tk.END, selected_tuple[8])
            Premium.delete(0, tk.END)
            Premium.insert(tk.END, selected_tuple[9])
            Company.delete(0, tk.END)
            Company.insert(tk.END, selected_tuple[10])
        else:
            pass


    admin_journey = tk.Tk()
    admin_journey.resizable(height = False, width = False)
    admin_journey.title('Travel Management System')
    admin_journey.geometry('800x600')

    #tk.Label(admin_journey, text="admin_journey", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(admin_journey, text="Journey Date").grid(row = 0, column = 0)
    tk.Label(admin_journey, text="Status").grid(row = 1, column = 0)
    tk.Label(admin_journey, text="Flight No").grid(row = 1, column = 3)
    tk.Label(admin_journey, text="Avbl Firstclass seats").grid(row = 2, column = 3)
    tk.Label(admin_journey, text="Avbl Economy seats").grid(row = 2, column = 0)
    tk.Label(admin_journey, text="Avbl Business seats").grid(row = 3, column = 3)
    tk.Label(admin_journey, text="Avbl Premium Seats").grid(row = 3, column = 0)
    tk.Label(admin_journey, text="Journey ID").grid(row = 0, column =3)

    # tk.ttk.Button(admin_journey, text="Search",  width = 12).grid(row= 3, column=3, columnspan = 2)



    journey_date = tk.ttk.Entry(admin_journey)
    journey_date.grid(row = 0, column = 1)
    status = tk.ttk.Entry(admin_journey)
    status.grid(row = 1, column = 1)
    flight_no = tk.ttk.Entry(admin_journey)
    flight_no.grid(row = 0, column =4)
    journ_id = tk.ttk.Entry(admin_journey)
    journ_id.grid(row = 1, column = 4)
    first_seat = tk.ttk.Entry(admin_journey, state = tk.DISABLED)
    first_seat.grid(row = 2, column =4)
    eco_seat = tk.ttk.Entry(admin_journey, state = tk.DISABLED)
    eco_seat.grid(row = 2, column =1)
    buss_seat = tk.ttk.Entry(admin_journey, state = tk.DISABLED)
    buss_seat.grid(row = 3, column =4)
    pre_seat = tk.ttk.Entry(admin_journey, state = tk.DISABLED)
    pre_seat.grid(row = 3, column =1)



    admin_journey_list = tk.Listbox(admin_journey, height = 17, width = 60)
    admin_journey_list.grid(row = 4, column = 0, columnspan = 2, rowspan = 4)


    # admin_journey_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(admin_journey, width = 10)
    sb1.grid(row=3, column=1, columnspan = 3, rowspan = 6)

    admin_journey_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = admin_journey_list.yview)


    admin_journey_list1 = tk.Listbox(admin_journey, height = 17, width = 60)
    admin_journey_list1.grid(row = 4, column = 2, columnspan = 4, rowspan = 4)

    sb1= tk.Scrollbar(admin_journey, width = 10)
    sb1.grid(row=3, column=5, columnspan =5 , rowspan = 6)

    admin_journey_list1.configure(yscrollcommand = sb1.set)
    sb1.configure(command = admin_journey_list1.yview)






    tk.ttk.Button(admin_journey, text="Insert",  width = 12).grid(row= 8, column=0)
    tk.ttk.Button(admin_journey, text="Update",  width = 12).grid(row= 8, column=1)
    tk.ttk.Button(admin_journey, text="Delete", width = 12).grid(row= 8, column=3)
    tk.ttk.Button(admin_journey, text="View All",  width = 12).grid(row= 8, column=4)


    # Makes the widgets responsive and centered
    n_rows = 12
    n_columns = 6
    for i in range(n_rows):
        admin_journey.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        admin_journey.grid_columnconfigure(i,  weight =1)

    admin_journey.mainloop()
crud_admin_journey()
