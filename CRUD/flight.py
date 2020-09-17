import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import datetime as dt

def crud_flight():

    con = mysql.connect(
        host="localhost",
        user="root",
        password="shobhit2000@",
        database="FMS"
        )

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

    def view_flight():
        cursor = con.cursor()
        cursor.execute("SELECT *FROM FLIGHT;")
        records = cursor.fetchall()
        flight_list.delete(0, tk.END)
        for rec in records:
            flight_list.insert(tk.END, rec)

    def insert_flight():
        flight_no1 = flight_no.get()
        model = Model_name.get()
        departure = Departure_time.get()
        route1 = Route.get()
        price1 = Price.get()
        baggage1 = Baggage.get()
        first1 = Firstclass.get()
        eco = Economy.get()
        business1 = Business.get()
        premium1 = Premium.get()
        comp1 = Company.get()
        if(flight_no1 == '' or model == '' or departure == '' or route1 == '' or price1 == '' or baggage1 == '' or first1 == '' or 
                eco == '' or business1 == '' or premium1 == '' or comp1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:
            args = cursor.callproc("CHECK_IF_FLIGHT_EXISTS", [flight_no1, None])
            if (args[-1] == 1):
                messagebox.showwarning("Invalid Request", "Flight already exists.")
            else:
                try:
                    departure = dt.datetime.strptime(departure, "%H:%M:%S")
                    price1 = float(price1)
                    baggage1 = int(baggage1)
                    first1 = int(first1)
                    eco = int(eco)
                    business1 = int(business1)
                    premium1 = int(premium1)
                    route1 = int(route1)
                    comp1 = int(comp1)
                    cursor.callproc("INSERT_FLIGHT_DETAILS", [flight_no1, model, departure, route1, price1, baggage1, first1, eco, business1, premium1, comp1])
                    cursor.execute("commit")
                    flight_no.delete(0, tk.END)
                    Model_name.delete(0, tk.END)
                    Departure_time.delete(0, tk.END)
                    Route.delete(0, tk.END)
                    Price.delete(0, tk.END)
                    Baggage.delete(0, tk.END)
                    Firstclass.delete(0, tk.END)
                    Economy.delete(0, tk.END)
                    Business.delete(0, tk.END)
                    Premium.delete(0, tk.END)
                    Company.delete(0, tk.END)
                    view_flight()
                    messagebox.showinfo("Request successful", "Successfully added city.")
                except:
                    messagebox.showwarning("Invalid Request", "Enter fields in proper format")



    def update_flight():
        flight_no1 = flight_no.get()
        model = Model_name.get()
        departure = Departure_time.get()
        route1 = Route.get()
        price1 = Price.get()
        baggage1 = Baggage.get()
        first1 = Firstclass.get()
        eco = Economy.get()
        business1 = Business.get()
        premium1 = Premium.get()
        comp1 = Company.get()
        if(flight_no1 == '' or model == '' or departure == '' or route1 == '' or price1 == '' or baggage1 == '' or first1 == '' or 
                eco == '' or business1 == '' or premium1 == '' or comp1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:
            args = cursor.callproc("CHECK_IF_FLIGHT_EXISTS", [flight_no1, None])
            if (args[-1] == 1):
                try:
                    departure = dt.datetime.strptime(departure, "%H:%M:%S")
                    price1 = float(price1)
                    baggage1 = int(baggage1)
                    route1 = int(route1)
                    comp1 = int(comp1)
                    cursor.callproc("UPDATE_FLIGHT_DETAILS", [flight_no1, departure, route1, price1, baggage1, comp1])
                    cursor.execute("commit")
                    flight_no.delete(0, tk.END)
                    Model_name.delete(0, tk.END)
                    Departure_time.delete(0, tk.END)
                    Route.delete(0, tk.END)
                    Price.delete(0, tk.END)
                    Baggage.delete(0, tk.END)
                    Firstclass.delete(0, tk.END)
                    Economy.delete(0, tk.END)
                    Business.delete(0, tk.END)
                    Premium.delete(0, tk.END)
                    Company.delete(0, tk.END)
                    view_flight()
                    messagebox.showinfo("Request successful", "Successfully updated flight.")    
                except:
                    messagebox.showwarning("Invalid Request", "Flight does not exists.")


    def delete_flight():
        flight_no1 = flight_no.get()
        if (flight_no1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have selected a flight.")
        else:
            args = cursor.callproc("CHECK_IF_FLIGHT_EXISTS", [flight_no1, None])
            if (args[-1] == 1):
                cursor.callproc("DELETE_FLIGHT", [flight_no1])
                cursor.execute("commit")
                flight_no.delete(0, tk.END)
                view_flight()
                messagebox.showinfo("Request successful", "Successfully deleted flight.")
            else:
                messagebox.showwarning("Invalid Request", "Flight does not exists.")

    def search_flight():
        flight_no1 = flight_no.get()
        model = Model_name.get()
        departure = Departure_time.get()
        route1 = Route.get()
        price1 = Price.get()
        baggage1 = Baggage.get()
        first1 = Firstclass.get()
        eco = Economy.get()
        business1 = Business.get()
        premium1 = Premium.get()
        comp1 = Company.get()
        if(flight_no1 == '' and model == '' and departure == '' and route1 == '' and price1 == '' and baggage1 == '' and first1 == '' and 
                eco == '' and business1 == '' and premium1 == '' and comp1 == ''):
            messagebox.showwarning("Invalid request", "Enter valid data you want to serach.")
        else:
            cursor.execute("SELECT *FROM FLIGHT WHERE FLIGHT_NO = %s OR MODEL_NAME = %s OR DEPARTURE_TIME = %s OR ROUTE_ID = %s OR PRICE = %s OR BAGGAGE_ALLOWANCE = %s OR NO_OF_FIRSTCLASS_SEATS = %s OR NO_OF_ECONOMY_SEATS = %s OR NO_OF_BUSINESS_SEATS = %s OR NO_OF_PREMIUM_SEATS = %s OR COMPANY_ID = %s;", [flight_no1, model, departure, route1, price1, baggage1, first1, eco, business1, premium1, comp1])
            records = cursor.fetchall()
            if(len(records) == 0):
                messagebox.showwarning("Invalid request", "No Records Found.")
            else:
                flight_no.delete(0, tk.END)
                Model_name.delete(0, tk.END)
                Departure_time.delete(0, tk.END)
                Route.delete(0, tk.END)
                Price.delete(0, tk.END)
                Baggage.delete(0, tk.END)
                Firstclass.delete(0, tk.END)
                Economy.delete(0, tk.END)
                Business.delete(0, tk.END)
                Premium.delete(0, tk.END)
                Company.delete(0, tk.END)
                flight_list.delete(0, tk.END)
                for rec in records:
                    flight_list.insert(tk.END, rec)


    flight = tk.Tk()
    flight.resizable(height = False, width = False)
    flight.title('Travel Management System')
    flight.geometry('900x500')

    # tk.Label(flight, text="flight", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(flight, text="Flight No").grid(column=0, row=0)
    tk.Label(flight, text="Model Name").grid(column=2, row=0)
    tk.Label(flight, text="Departure Time").grid(column=4, row=0)
    tk.Label(flight, text="Base Price").grid(column=0, row=1)
    tk.Label(flight, text="Baggage Allowance").grid(column=2, row=1)
    tk.Label(flight, text="Route ID").grid(column=4, row=1)
    tk.Label(flight, text="Company ID").grid(column=6, row=1)
    tk.Label(flight, text="First Class Seats").grid(column=0, row=2)
    tk.Label(flight, text="Economy Seats").grid(column=2, row=2)
    tk.Label(flight, text="Business Seats").grid(column=4, row=2)
    tk.Label(flight, text="Premium Seats").grid(column=6, row=2)
    
    

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

    Route = tk.ttk.Entry(flight)
    Route.grid(column=5, row=1)

    Company = tk.ttk.Entry(flight)
    Company.grid(column=7, row=1)

    Firstclass = tk.ttk.Entry(flight)
    Firstclass.grid(column=1, row=2)

    Economy = tk.ttk.Entry(flight)
    Economy.grid(column=3, row=2)

    Business = tk.ttk.Entry(flight)
    Business.grid(column=5, row=2)

    Premium = tk.ttk.Entry(flight)
    Premium.grid(column=7, row=2)


    flight_list = tk.Listbox(flight, height = 20, width = 78)
    flight_list.grid(row = 5, column = 0, columnspan = 5, rowspan = 5)

    flight_list.bind('<<ListboxSelect>>', get_selected_row)

    sb1= tk.Scrollbar(flight, width = 10)
    sb1.grid(row=5, column=4, columnspan = 1, rowspan = 5)

    sb2= tk.Scrollbar(flight, width = 10, orient = tk.HORIZONTAL)
    sb2.grid(row=10, column=1, columnspan = 3)

    flight_list.configure(yscrollcommand = sb1.set)
    sb1.configure(command = flight_list.yview)

    flight_list.configure(xscrollcommand = sb2.set)
    sb2.configure(command = flight_list.xview)


    tk.ttk.Button(flight, text="Insert", command=insert_flight, width = 12).grid(row= 5, column=6, columnspan = 2)
    tk.ttk.Button(flight, text="Update", command=update_flight, width = 12).grid(row= 6, column=6, columnspan = 2)
    tk.ttk.Button(flight, text="Delete", command=delete_flight, width = 12).grid(row= 7, column=6, columnspan = 2)
    tk.ttk.Button(flight, text="View All", command=view_flight, width = 12).grid(row= 8, column=6, columnspan = 2)
    tk.ttk.Button(flight, text="Search", command=search_flight, width = 12).grid(row= 9, column=6, columnspan = 2)

    cursor = con.cursor()     
    cursor.execute("SELECT ROUTE_ID, START_CITY, DEST_CITY FROM ROUTE;") 
    city_records = cursor.fetchall()


    route_id_path = tk.StringVar()
    route_options = ttk.Combobox(flight, width = 13, textvariable = route_id_path)
    route_options.grid(row=6, column=5)

    route_options['values'] = ['-----Route-----'] + [str(rec[0]) + '     ' + str(rec[1]) + '-' + str(rec[2]) for rec in city_records]
    route_options.current(0)



    cursor = con.cursor()     
    cursor.execute("SELECT COMPANY_ID, COMPANY_NAME FROM COMPANY;") 
    company_records = cursor.fetchall()

    comp = tk.StringVar()
    company_name = ttk.Combobox(flight, width = 13, textvariable = comp)
    company_name.grid(row=8, column=5)

    company_name['values'] = ['---Companies---'] + [str(rec[0]) + ' - ' + str(rec[1]) for rec in company_records]
    company_name.current(0)


    # tk.ttk.Button(flight, text="Submit").grid(column=0, row=13, columnspan=2)

    
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
