import tkinter as tk
from tkinter import ttk
import journey
from functools import partial
import update_user


def get_journey():
    journey.journey_screen()

def logout(homepage):
    homepage.destroy()
    import main

def homepage_screen(user_id, user_name, credit_points):
    homepage = tk.Tk()
    homepage.resizable(height = False, width = False)
    homepage.title('Travel Management System')
    homepage.geometry('600x400')

    tk.Label(homepage, text="Welcome "+user_name,font=('Helvetica', '25')).grid(column=0, row=0, columnspan=3)
    tk.Label(homepage, text="Options:",font=('Helvetica', '15')).grid(column=0, row=1, columnspan=3)
    tk.Label(homepage, text="Credits earned: "+str(credit_points)).grid(column=2, row=0, padx=10)

    tk.ttk.Button(homepage, text="Book a ticket", command=get_journey).grid(column=0, columnspan=3,row=2)
    tk.ttk.Button(homepage, text="Get Booking History").grid(column=0, columnspan=3,row=3)
    tk.ttk.Button(homepage, text="Edit Details", command=partial(update_user.update_user, user_id, homepage)).grid(column=0, columnspan=3,row=4)
    tk.ttk.Button(homepage, text="Logout", command=partial(logout, homepage)).grid(column=0, row=5, columnspan=3)


    # Makes the widgets responsive and centered
    n_rows = 6
    n_columns = 2
    for i in range(n_rows):
        homepage.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        homepage.grid_columnconfigure(i,  weight =1)



    homepage.mainloop()
