import tkinter as tk
from tkinter import ttk
def booking_run(source, dest, mode, date):
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

        tk.Label(booking, text="Seats Available: 69").grid(column=1, row=4+(i*4))
        n_seat_type = tk.StringVar()
        seat_type = ttk.Combobox(booking, width = 25, textvariable = n_seat_type)
        seat_type['values'] =             (
                                  '------Select seat type------',
                                  'Economy',
                                  'Business',
                                )
        seat_type.current(0)

        submit = tk.ttk.Button(booking, text="Select")
        seat_type.grid(column=0, row=4+(i*4))
        submit.grid(column=2, row=4+(i*4))
    n_rows = 20
    n_columns = 4
    for i in range(n_rows):
        booking.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        booking.grid_columnconfigure(i,  weight =1)

    heading.grid(column=1, row=0, columnspan=2)

    booking.mainloop()
