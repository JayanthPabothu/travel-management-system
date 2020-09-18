import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox

def crud_admin_journey():

    con = mysql.connect(
    host="localhost",
    user="root",
    password="testpassword",
    database="FMS"
    )
    cursor = con.cursor()

    def get_selected_row(event):
        global old_flight_no
        index = admin_journey_list.curselection()
        if (len(index) != 0):
            selected_tuple = admin_journey_list.get(index)
            journ_id.delete(0, tk.END)
            journ_id.insert(tk.END,selected_tuple[0])
            old_flight_no= flight_no.get()
            journey_date.delete(0, tk.END)
            journey_date.insert(tk.END, selected_tuple[1])
            first_seat.config(state = tk.NORMAL)
            first_seat.delete(0, tk.END)
            first_seat.insert(tk.END, selected_tuple[2])
            first_seat.config(state = tk.DISABLED)
            eco_seat.config(state = tk.NORMAL)
            eco_seat.delete(0, tk.END)
            eco_seat.insert(tk.END, selected_tuple[3])
            eco_seat.config(state = tk.DISABLED)
            buss_seat.config(state = tk.NORMAL)
            buss_seat.delete(0, tk.END)
            buss_seat.insert(tk.END, selected_tuple[4])
            buss_seat.config(state = tk.DISABLED)
            pre_seat.config(state = tk.NORMAL)
            pre_seat.delete(0, tk.END)
            pre_seat.insert(tk.END, selected_tuple[5])
            pre_seat.config(state = tk.DISABLED)
            flight_no.delete(0, tk.END)
            flight_no.insert(tk.END, selected_tuple[6])
            status.delete(0, tk.END)
            status.insert(tk.END, selected_tuple[7])
        else:
            pass

    def view_data():
        cursor.execute("SELECT *FROM JOURNEY_FLIGHT;")
        records = cursor.fetchall()
        admin_journey_list.delete(0, tk.END)
        for rec in records:
            admin_journey_list.insert(tk.END, rec)

    def insert_admin_journey():
        journey_date1 = journey_date.get()
        flight_no1 = flight_no.get()
        status1 = status.get()
        journey_id1 = journ_id.get()
        if(flight_no1 == '' or journey_date1 == '' or status1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled the required fields.")
        elif(journey_id1 != ''):
            messagebox.showwarning("Invalid request", "Dont Enter Journey ID. It is auto generated.")
        else:
            args = cursor.callproc("CHECK_IF_JOURNEY_EXISTS", [flight_no1, journey_date1, None])
            if (args[-1] == 1):
                messagebox.showwarning("Invalid Request", "Journey already exists.")
            else:
                cursor.callproc("INSERT_JOURNEY_DETAILS", [journey_date1, flight_no1, status1])
                cursor.execute("commit")
                flight_no.delete(0, tk.END)
                journ_id.delete(0, tk.END)
                status.delete(0, tk.END)
                journey_date.delete(0, tk.END)
                view_data()
                messagebox.showinfo("Request successful", "Successfully added Journey.")

    def search_journey():
        journey_date1 = journey_date.get()
        print(journey_date1)
        # journey_date1 = journey_date1.strftime("%Y-%m-%d")
        # print(journey_date1)
        flight_no1 = flight_no.get()
        status1 = status.get()
        # print(status1)
        journey_id1 = journ_id.get()
        # print(journey_id1)
        if(flight_no1 != '' and journey_date1 != '' and status1 != '' and journey_id1 != ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled the required fields.")
        elif(status1 == '' ):
            # print(journey_id1)
            # print(status1)
            # print(flight_no1)
            # print(journey_date1)
            if(journey_date1 != ''):
                cursor.execute("SELECT * FROM JOURNEY_FLIGHT WHERE JOURNEY_ID = %s OR FLIGHT_NO = %s OR JOURNEY_DATE = %s;", [journey_id1, flight_no1, journey_date1])
                records = cursor.fetchall()
                print(records)
                if(len(records) == 0):
                    messagebox.showwarning("Invalid request", "No Records Found.")
                else:
                    flight_no.delete(0, tk.END)
                    journ_id.delete(0, tk.END)
                    status.delete(0, tk.END)
                    journey_date.delete(0, tk.END)
                    admin_journey_list.delete(0, tk.END)
                    for rec in records:
                        admin_journey_list.insert(tk.END, rec)
            else:
                cursor.execute("SELECT * FROM JOURNEY_FLIGHT WHERE JOURNEY_ID = %s OR FLIGHT_NO = %s;", [journey_id1, flight_no1])
                records = cursor.fetchall()
                print(records)
                if(len(records) == 0):
                    messagebox.showwarning("Invalid request", "No Records Found.")
                else:
                    flight_no.delete(0, tk.END)
                    journ_id.delete(0, tk.END)
                    status.delete(0, tk.END)
                    journey_date.delete(0, tk.END)
                    admin_journey_list.delete(0, tk.END)
                    for rec in records:
                        admin_journey_list.insert(tk.END, rec)

        else:
            print(journey_id1)
            print(status1)
            print(flight_no1)
            print(journey_date1)
            cursor.execute("SELECT * FROM JOURNEY_FLIGHT WHERE JOURNEY_ID = %s OR FLIGHT_NO = %s OR JOURNEY_DATE = %s OR JOURNEY_STATUS = %s;", [journey_id1, flight_no1, journey_date1, status1])
            records = cursor.fetchall()
            print(records)
            if(len(records) == 0):
                messagebox.showwarning("Invalid request", "No Records Found.")
            else:
                flight_no.delete(0, tk.END)
                journ_id.delete(0, tk.END)
                status.delete(0, tk.END)
                journey_date.delete(0, tk.END)
                admin_journey_list.delete(0, tk.END)
                for rec in records:
                    admin_journey_list.insert(tk.END, rec)


    def update_journey():
        flight_no1 = flight_no.get()
        journey_date1 = journey_date.get()
        journey_id1 = journ_id.get()
        status1 = status.get()
        if(flight_no1 == '' and journey_date1 == '' and status1 == '' and journey_id1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled the required fields.")
        else:
            args = cursor.callproc("CHECK_IF_JOURNEY_EXISTS", [flight_no1, journey_date1, None])
            if (args[-1] == 1):
                cursor.callproc("CHANGE_JOURNEY_STATUS", [journey_id1, status1])
                cursor.execute("commit")
                flight_no.delete(0, tk.END)
                journ_id.delete(0, tk.END)
                status.delete(0, tk.END)
                journey_date.delete(0, tk.END)
                view_data()
                messagebox.showinfo("Request successful", "Successfully updated journey.")
            else:
                messagebox.showwarning("Invalid Request", "Journey does not exists.")

    def delete_journey():
        journey_id1 = journ_id.get()
        journey_date1 = journey_date.get()
        flight_no1 = flight_no.get()
        if (journey_id1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have selected a flight.")
        else:
            args = cursor.callproc("CHECK_IF_JOURNEY_EXISTS", [flight_no1, journey_date1, None])
            if (args[-1] == 1):
                cursor.callproc("DELETE_JOURNEY", [journey_id1])
                cursor.execute("commit")
                flight_no.delete(0, tk.END)
                journ_id.delete(0, tk.END)
                status.delete(0, tk.END)
                journey_date.delete(0, tk.END)
                view_data()
                messagebox.showinfo("Request successful", "Successfully deleted journey.")
            else:
                messagebox.showwarning("Invalid Request", "Journey does not exists.")

    def clear_data():
        flight_no.delete(0, tk.END)

        journ_id.delete(0, tk.END)

        buss_seat.config(state = tk.NORMAL)
        buss_seat.delete(0, tk.END)
        buss_seat.config(state = tk.DISABLED)

        journey_date.delete(0, tk.END)

        eco_seat.config(state = tk.NORMAL)
        eco_seat.delete(0, tk.END)
        eco_seat.config(state = tk.DISABLED)

        status.delete(0, tk.END)

        first_seat.config(state = tk.NORMAL)
        first_seat.delete(0, tk.END)
        first_seat.config(state = tk.DISABLED)

        pre_seat.config(state = tk.NORMAL)
        pre_seat.delete(0, tk.END)
        pre_seat.config(state = tk.DISABLED)





    admin_journey = tk.Tk()
    admin_journey.resizable(height = False, width = False)
    admin_journey.title('Travel Management System')
    admin_journey.geometry('800x600')

    #tk.Label(admin_journey, text="admin_journey", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(admin_journey, text="Journey ID").grid(row = 0, column = 0)
    tk.Label(admin_journey, text="Status").grid(row = 1, column = 0)
    tk.Label(admin_journey, text="Flight No").grid(row = 1, column = 3)
    tk.Label(admin_journey, text="Avbl Firstclass seats").grid(row = 2, column = 3)
    tk.Label(admin_journey, text="Avbl Economy seats").grid(row = 2, column = 0)
    tk.Label(admin_journey, text="Avbl Business seats").grid(row = 3, column = 3)
    tk.Label(admin_journey, text="Avbl Premium Seats").grid(row = 3, column = 0)
    tk.Label(admin_journey, text="Journey Date").grid(row = 0, column =3)



    journey_date = tk.ttk.Entry(admin_journey)
    journey_date.grid(row = 0, column = 4)
    status = tk.ttk.Entry(admin_journey)
    status.grid(row = 1, column = 1)
    flight_no = tk.ttk.Entry(admin_journey)
    flight_no.grid(row = 1, column =4)
    journ_id = tk.ttk.Entry(admin_journey)
    journ_id.grid(row = 0, column = 1)
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

    admin_journey_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(admin_journey, width = 10)
    sb1.grid(row=3, column=1, columnspan = 3, rowspan = 6)

    admin_journey_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = admin_journey_list.yview)


    admin_journey_list1 = tk.Listbox(admin_journey, height = 17, width = 60)
    admin_journey_list1.grid(row = 4, column = 2, columnspan = 4, rowspan = 4)

    cursor.execute("SELECT FLIGHT.FLIGHT_NO, ROUTE.START_CITY, ROUTE.DEST_CITY FROM FLIGHT INNER JOIN ROUTE ON FLIGHT.ROUTE_ID = ROUTE.ROUTE_ID;")
    flight_records = cursor.fetchall()
    admin_journey_list1.delete(0, tk.END)
    for rec in flight_records:
        admin_journey_list1.insert(tk.END, rec)

    sb1= tk.Scrollbar(admin_journey, width = 10)
    sb1.grid(row=3, column=5, columnspan =5 , rowspan = 6)

    admin_journey_list1.configure(yscrollcommand = sb1.set)
    sb1.configure(command = admin_journey_list1.yview)


    tk.ttk.Button(admin_journey, text="Insert", command = insert_admin_journey, width = 12).grid(row= 8, column=0)
    tk.ttk.Button(admin_journey, text="Update", command = update_journey, width = 12).grid(row= 8, column=1)
    tk.ttk.Button(admin_journey, text="Delete", command = delete_journey, width = 12).grid(row= 8, column=3)
    tk.ttk.Button(admin_journey, text="View All", command = view_data,  width = 12).grid(row= 8, column=4)
    tk.ttk.Button(admin_journey, text="Search", command = search_journey, width = 12).grid(row= 9, column=1)
    tk.ttk.Button(admin_journey, text="Clear", command = clear_data, width = 12).grid(row= 9, column=3)

    # Makes the widgets responsive and centered
    n_rows = 12
    n_columns = 6
    for i in range(n_rows):
        admin_journey.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        admin_journey.grid_columnconfigure(i,  weight =1)

    admin_journey.mainloop()
