import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

def crud_flight():

    def get_selected_row(event):
        global old_flight_no
        index = flight_list.curselection()
        if (len(index) != 0):
            selected_tuple = flight_list.get(index)
            flight_no.delete(0, tk.END)
            flight_no.insert(tk.END,selected_tuple[0])
            old_flight_no= flight_no.get()
            Model_name.delete(0, tk.END)
            Model_name.insert(tk.END, selected_tuple[1])
            Departure_time.delete(0, tk.END)
            Departure_time.insert(tk.END, selected_tuple[2])
            Price.delete(0, tk.END)
            Price.insert(tk.END, selected_tuple[3])
            Baggage.delete(0, tk.END)
            Baggage.insert(tk.END, selected_tuple[4])
            Firstclass.delete(0, tk.END)
            Firstclass.insert(tk.END, selected_tuple[5])
            Economy.delete(0, tk.END)
            Economy.insert(tk.END, selected_tuple[6])
            Business.delete(0, tk.END)
            Business.insert(tk.END, selected_tuple[7])
            Premium.delete(0, tk.END)
            Premium.insert(tk.END, selected_tuple[8])
        else:
            pass

    flight = tk.Tk()
    flight.resizable(height = False, width = False)
    flight.title('Travel Management System')
    flight.geometry('900x800')

    # tk.Label(flight, text="flight", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(flight, text="Flight No").grid(column=0, row=0)
    tk.Label(flight, text="Model name").grid(column=0, row=1)
    tk.Label(flight, text="Departure Time").grid(column=4, row=1)
    tk.Label(flight, text="Price").grid(column=0, row=1)
    tk.Label(flight, text="Baggage Allowance").grid(column=2, row=2)
    tk.Label(flight, text="First class seats").grid(column=4, row=2)
    tk.Label(flight, text="Economy seats").grid(column=0, row=2)
    tk.Label(flight, text="Business seats").grid(column=2, row=3)
    tk.Label(flight, text="Premium seats").grid(column=4, row=3)

    flight_no = tk.ttk.Entry(flight)
    flight_no.grid(column=1, row=0)

    Model_name = tk.ttk.Entry(flight)
    Model_name.grid(column=3, row=0)

    Departure_time = tk.ttk.Entry(flight)
    Departure_time.grid(column=5, row=0)

    Price = tk.ttk.Entry(flight)
    Price.grid(column=1, row=1)

    Baggage = tk.ttk.Entry(flight)
    Baggage.grid(column=3, row=1)

    Firstclass = tk.ttk.Entry(flight)
    Firstclass.grid(column=5, row=1)

    Economy = tk.ttk.Entry(flight)
    Economy.grid(column=1, row=2)

    Business = tk.ttk.Entry(flight)
    Business.grid(column=3, row=2)

    Premium = tk.ttk.Entry(flight)
    Premium.grid(column=5, row=2)


    flight_list = tk.Listbox(flight, height = 15, width = 50)
    flight_list.grid(row = 3, column = 0, columnspan = 2, rowspan = 5)

    flight_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(flight, width = 10)
    sb1.grid(row=3, column=2, columnspan = 2, rowspan = 5)

    sb2= tk.Scrollbar(flight, width = 10, orient = tk.HORIZONTAL)
    sb2.grid(row=9, column=1, columnspan = 2)

    flight_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = flight_list.yview)

    flight_list.configure(xscrollcommand = sb2.set)
    sb2.configure(command = flight_list.xview)

    # tk.ttk.Button(flight, text="Submit").grid(column=0, row=13, columnspan=2)

    # con = mysql.connect(
    #                 host="localhost",
    #                 user="root",
    #                 password="testpassword",
    #                 database="TMS"
    #             )
    # cursor = con.cursor()

    # # Fetching route ids for dropdown
    # cursor.execute("SELECT ROUTE_ID FROM ROUTE;")
    # records = cursor.fetchall()
    # n_route_id = tk.StringVar()
    # route_id = ttk.Combobox(Bus, width = 10, textvariable = n_route_id)
    # route_id['values'] = [
    #                     (route[0]) for route in records
    #                             ]
    # route_id.current(0)

    # # Fetching companyid for dropdown
    # cursor.execute("SELECT COMPANY_ID FROM COMPANY;")
    # records = cursor.fetchall()
    # n_company_id = tk.StringVar()
    # company_id = ttk.Combobox(Bus, width = 10, textvariable = n_company_id)
    # company_id['values'] = [
    #                     company[0] for company in records
    #                             ]
    # company_id.current(0)

    # # Fetching for amenities
    # cursor.execute("SELECT AMENITY_ID FROM AMENITIES;")
    # records = cursor.fetchall()
    # n_amenities = tk.StringVar()
    # amenities = ttk.Combobox(Bus, width = 10, textvariable = n_amenities)
    # amenities['values'] = [
    #                     (amenity[0]) for amenity in records
    #                             ]
    # amenities.current(0)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        flight.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        flight.grid_columnconfigure(i,  weight =1)

    flight.mainloop()

crud_flight()
