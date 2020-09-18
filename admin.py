import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter.font import Font
from tkinter import messagebox
import datetime
from CRUD import flight, company, city, route, admin_journey
import admin_update
import mysql.connector as mysql
from tkinter import messagebox

def admin_screen(admin_id, admin_name):

    def fetch_city():
        admin.destroy()
        city.crud_city()
        admin_screen(admin_id, admin_name)

    def fetch_route():
        admin.destroy()
        route.crud_route()
        admin_screen(admin_id, admin_name)


    def fetch_flight():
        admin.destroy()
        flight.crud_flight()
        admin_screen(admin_id, admin_name)


    def fetch_company():
        admin.destroy()
        company.crud_company()
        admin_screen(admin_id, admin_name)


    def fetch_journey():
        admin.destroy()
        admin_journey.crud_admin_journey()
        admin_screen(admin_id, admin_name)


    def view_data():
        admin.destroy()
        admin_update.update_user(admin_id)

    def delete_the_admin():
        if messagebox.askokcancel("Quit", "Are you sure?"):
            con = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="FMS"
                )
            cursor = con.cursor()
            cursor.callproc("DELETE_ADMIN_DETAILS", [admin_id])
            cursor.execute("commit")
            messagebox.showwarning("Request successful", "Your account has been successfully deleted.")
            admin.destroy()
            import login
            login.main_screen()

    def get_logout():
        admin.destroy()
        import login
        login.main_screen()

    admin = tk.Tk()
    admin.resizable(height = False, width = False)
    admin.title('Flight Management System')
    admin.geometry('720x420')
    adam = Font(family="ADAM.CG PRO", size=20)

    curr_date = datetime.date.today()
    curr_date = curr_date.strftime("%d-%m-%Y")

    logo = tk.PhotoImage(file='Images/admin_logo.png')
    photoimage = logo.subsample(3, 3)
    logo = tk.Label(admin,  image=photoimage)
    logo.place(x=80, y=35)

    label1 = tk.Label(admin, text="Admin Panel", font= adam)
    label1.place(x=310, y=65)
    label2 = tk.Label(admin, text="Welcome "+admin_name, font= adam)
    label2.place(x=285, y=125)
    label3 = tk.Label(admin, text=f"Today: {curr_date}")
    label3.place(x=605, y=10)


    City_button= tk.ttk.Button(admin, text="City", command=fetch_city)
    City_button.place(x=20, y=250, width = 100, height = 30)

    Route_button= tk.ttk.Button(admin, text="Route", command=fetch_route)
    Route_button.place(x=160, y=250, width = 100, height = 30)

    Flight_button= tk.ttk.Button(admin, text="Flight", command=fetch_flight)
    Flight_button.place(x=310, y=250, width = 100, height = 30)

    Company_button= tk.ttk.Button(admin, text="Company", command=fetch_company)
    Company_button.place(x=460, y=250, width = 100, height = 30)

    Journey_button = tk.ttk.Button(admin, text="Journey Details", command=fetch_journey)
    Journey_button.place(x=600, y=250, width = 100, height = 30)

    Update_button = tk.ttk.Button(admin, text="Update Details", command=view_data)
    Update_button.place(x=10, y=10, width = 100, height = 30)

    delete_admin = tk.ttk.Button(admin, text="Delete Account", command=delete_the_admin)
    delete_admin.place(x=10, y=50, width = 100, height = 30)

    logout = tk.ttk.Button(admin, text="Logout", command=get_logout)
    logout.place(x=10, y=90, width = 100, height = 30)


    # table_name = ['BUS', 'CAR', 'FLIGHT', 'CITY', 'ROUTE', 'AMENITIES', 'COMPANY', 'EMPLOYEE']
    # row_counter = 4
    # add_row = 0
    # i = -1
    # counter = 0
    # while(counter<8):
    #     i = (i+1)%4
    #     tk.Label(admin, text=table_name[counter], font=('Helvetica', '15')).grid(column=0+i, row=1+add_row)
    #     # tk.ttk.Button(admin, text="Create an Entry", command=partial(create_query, counter)).grid(column=0+i, row=2+add_row)
    #     # tk.ttk.Button(admin, text="Update an Entry", command=partial(update_query, counter)).grid(column=0+i, row=3+add_row)
    #     # tk.ttk.Button(admin, text="Delete an Entry", command=partial(delete_query, counter)).grid(column=0+i, row=4+add_row)
    #     row_counter-=1
    #     counter+=1

    #     if row_counter == 0:
    #         add_row = 4
    #         row_counter = 5

    # Makes the widgets responsive and centered
    # n_rows = 15
    # n_columns = 4
    # for i in range(n_rows):
    #     admin.grid_rowconfigure(i,  weight =1)
    # for i in range(n_columns):
    #     admin.grid_columnconfigure(i,  weight =1)

    admin.mainloop()

# admin_screen(1, 'admin')
