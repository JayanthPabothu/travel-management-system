import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import datetime as dt

def crud_route():
    con = mysql.connect(
    host="localhost",
    user="root",
    password="testpassword",
    database="FMS"
    )
    cursor = con.cursor()

    def view_route():

        cursor = con.cursor()
        cursor.execute("SELECT *FROM ROUTE;")
        records = cursor.fetchall()
        route_list.delete(0, tk.END)
        for rec in records:
            route_list.insert(tk.END, rec)

    def get_selected_row(event):
        global old_start_city, old_dest_city, old_route_id
        print(route_list.curselection())
        if(len(route_list.curselection()) != 0):

            index = route_list.curselection()[0]
            selected_tuple = route_list.get(index)
            print(selected_tuple)
            old_route_id = selected_tuple[0]
            start_city.delete(0, tk.END)
            start_city.insert(tk.END,selected_tuple[1])
            old_start_city= start_city.get()
            print(old_start_city)
            dest_city.delete(0, tk.END)
            dest_city.insert(tk.END, selected_tuple[2])
            old_dest_city = dest_city.get()
            time_taken.delete(0, tk.END)
            time_taken.insert(tk.END, selected_tuple[3])

        else:
            pass

    #
    def insert_route():
        start_city1 = start_city.get()
        dest_city1 = dest_city.get()
        time_taken1 = time_taken.get()

        if(start_city1 == '' or dest_city1 == '' or time_taken1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:
            try:
                time_taken1 = dt.datetime.strptime(time_taken1, "%H:%M:%S")
                args = cursor.callproc("CHECK_IF_ROUTE_EXISTS", [start_city1, dest_city1, None])
                if (args[-1] == 1):
                    messagebox.showwarning("Route already exists", "Please enter a new route.")
                else:
                    cursor.callproc("INSERT_ROUTE", [start_city1, dest_city1, time_taken1])
                    cursor.execute("commit")
                    start_city.delete(0, tk.END)
                    dest_city.delete(0, tk.END)
                    time_taken.delete(0, tk.END)
                    route_list.delete(0, tk.END)
                    view_route()

                    messagebox.showinfo("Request successful", "Successfully added route.")
            except:
                messagebox.showwarning("Invalid request", "Please enter time taken in the valid format.")


    def update_route():
        start_city1 = start_city.get()
        dest_city1 = dest_city.get()
        time_taken1 = time_taken.get()
        print(old_start_city)

        if(start_city1 == '' or dest_city1 == '' or time_taken1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have fetched all the fields.")
        else:
            args = cursor.callproc("CHECK_IF_ROUTE_EXISTS", [start_city1, dest_city1, None])
            if (args[-1] == 1):
                try:
                    time_taken1 = dt.datetime.strptime(time_taken1, "%H:%M:%S")
                    cursor.callproc("UPDATE_ROUTE", [old_route_id, time_taken1])
                    cursor.execute("commit")
                    start_city.delete(0, tk.END)
                    dest_city.delete(0, tk.END)
                    time_taken.delete(0, tk.END)
                    route_list.delete(0, tk.END)
                    view_route()
                    messagebox.showinfo("Request successful", "Successfully updated route.")
                except:
                    messagebox.showwarning("Invalid Request", "Please enter time taken in the valid format.")

            else:
                messagebox.showwarning("Invalid Request", "Route does not exists.")

    def delete_route():

        if (start_city == '' or dest_city == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have selected a route to delete.")
        else:
            cursor.callproc("DELETE_ROUTE", [old_start_city, old_dest_city])
            cursor.execute("commit")
            start_city.delete(0, tk.END)
            dest_city.delete(0, tk.END)
            time_taken.delete(0, tk.END)
            route_list.delete(0, tk.END)
            view_route()
            messagebox.showinfo("Request successful", "Successfully deleted city.")

    def search_route():
        start_city1 = start_city.get()
        dest_city1 = dest_city.get()
        time_taken1 = time_taken.get()
        cursor.execute("SELECT * FROM ROUTE WHERE START_CITY = %s OR DEST_CITY = %s OR TIME_TAKEN = %s;", [start_city1,dest_city1, time_taken1])
        records = cursor.fetchall()
        route_list.delete(0, tk.END)
        for rec in records:
            route_list.insert(tk.END, rec)


    route = tk.Tk()
    route.resizable(height = False, width = False)
    route.title('Travel Management System')
    route.geometry('720x500')

    #tk.Label(City, text="City", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(route, text="Start City:").grid(row = 0, column = 0)
    tk.Label(route, text="Dest City:").grid(row = 1, column = 0)
    tk.Label(route, text="Time Taken:").grid(row = 0, column = 2)
    tk.Label(route, text="Available cities:").grid(row=1, column=2)

    cursor.execute("SELECT CITY_CODE FROM CITY")
    cities = cursor.fetchall()

    seatnofc = tk.StringVar()
    seats_fc = ttk.Combobox(route, textvariable = seatnofc)
    seats_fc['values'] = [
                    city for city in cities

    ]
    seats_fc.current(0)
    seats_fc.grid(row=1, column=3)




    start_city = tk.ttk.Entry(route)
    start_city.grid(row = 0, column = 1)
    dest_city = tk.ttk.Entry(route)
    dest_city.grid(row = 1, column = 1)
    time_taken = tk.ttk.Entry(route)
    time_taken.grid(row = 0, column = 3)



    route_list = tk.Listbox(route, height = 15, width = 50)
    route_list.grid(row = 2, column = 0, columnspan = 2, rowspan = 5)

    route_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(route, width = 10)
    sb1.grid(row=3, column=1, columnspan = 2, rowspan = 2, sticky='ns')

    route_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = route_list.yview)


    tk.ttk.Button(route, text="Insert", width = 12, command=insert_route).grid(row= 2, column=3)
    tk.ttk.Button(route, text="Update", width = 12, command=update_route).grid(row= 3, column=3)
    tk.ttk.Button(route, text="Delete", width = 12, command=delete_route).grid(row= 4, column=3)
    tk.ttk.Button(route, text="View All", width = 12, command=view_route).grid(row= 5, column=3)
    tk.ttk.Button(route, text="Search", width = 12, command=search_route).grid(row= 6, column=3)

    #Makes the widgets responsive and centered
    n_rows = 10
    n_columns = 5
    for i in range(n_rows):
        route.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        route.grid_columnconfigure(i,  weight =1)

    route.mainloop()
# crud_route()
