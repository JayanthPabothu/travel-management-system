import tkinter as tk
from tkinter import ttk

booking = tk.Tk()
booking.resizable(height = False, width = False)
booking.title('Travel Management System')
booking.geometry('720x500')

heading = tk.Label(booking, text="Search results", font=('Helvetica', '25'))

result_box = []
no_of_results = 1
ini_col = 0
ini_row = 1
for i in range(0, no_of_results):

    tk.Label(booking, text="Air India").grid(column=0, row=(1+(i*4)))
    tk.Label(booking, text="Journey Begins").grid(column=0, row=2+(i*4))
    tk.Label(booking, text="Journey Ends").grid(column=2, row=2+(i*4))
    tk.Label(booking, text="Duration").grid(column=1, row=2+(i*4))
    tk.Label(booking, text="Cost").grid(column=3, row=2+(i*4))
    tk.Label(booking, text="00:00").grid(column=0, row=3+(i*4))
    tk.Label(booking, text="12:10").grid(column=2, row=3+(i*4))
    tk.Label(booking, text="12h 10m").grid(column=1, row=3+(i*4))
    tk.Label(booking, text="Rs.5000").grid(column=3, row=3+(i*4))
    n_seat = tk.StringVar()
    seats = ttk.Combobox(booking, width = 25, textvariable = n_seat)
    seats['values'] =               (
                              '-----Select a seat number----',
                              'A0',
                              'A1',
                              'B0',
                              'B1',
                            )
    seats.current(0)
    n_seat_type = tk.StringVar()
    seat_type = ttk.Combobox(booking, width = 25, textvariable = n_seat_type)
    seat_type['values'] =             (
                              '------Select seat type------',
                              'Economy',
                              'Business',
                            )
    seat_type.current(0)

    submit = tk.ttk.Button(booking, text="Submit")

    # # --------Placing on grid----------
    #
    # # Column 0
    # # company.grid(column=0, row=1)
    # journey_begins.grid(column=0, row=2)
    # journey_begins_value.grid(column=0, row=3)
    seat_type.grid(column=0, row=4+(i*4))
    #
    # # Column 1
    # duration.grid(column=1, row=2)
    # duration_value.grid(column=1, row=3)
    seats.grid(column=1, row=4+(i*4))
    #
    # # Column 2
    # journey_ends.grid(column=2, row=2)
    # journey_ends_value.grid(column=2, row=3)
    submit.grid(column=2, row=4+(i*4))
    #
    # # Column 3
    # amount.grid(column=3, row=2)
    # amount_value.grid(column=3, row=3)

# Makes the widgets rsponsive and centered
n_rows = 20
n_columns = 4
for i in range(n_rows):
    booking.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    booking.grid_columnconfigure(i,  weight =1)

heading.grid(column=1, row=0, columnspan=2)

booking.mainloop()
