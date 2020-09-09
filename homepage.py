import tkinter as tk
from tkinter import ttk
import journey

def get_journey():
    journey.journey_screen()

def homepage_screen():
    homepage = tk.Tk()
    homepage.resizable(height = False, width = False)
    homepage.title('Travel Management System')
    homepage.geometry('500x300')

    tk.Label(homepage, text="Welcome user",font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(homepage, text="Options:",font=('Helvetica', '15')).grid(column=0, row=1, columnspan=2)

    tk.ttk.Button(homepage, text="Book a ticket", command=get_journey).grid(column=0, columnspan=2,row=2)
    tk.ttk.Button(homepage, text="Get Booking History").grid(column=0, columnspan=2,row=3)
    tk.ttk.Button(homepage, text="Edit Details").grid(column=0, columnspan=2,row=4)



    # Makes the widgets responsive and centered
    n_rows = 5
    n_columns = 2
    for i in range(n_rows):
        homepage.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        homepage.grid_columnconfigure(i,  weight =1)



    homepage.mainloop()
homepage_screen()
