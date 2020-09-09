import tkinter as tk
from tkinter import ttk

def crud_company():
    company = tk.Tk()
    company.resizable(height = False, width = False)
    company.title('Travel Management System')
    company.geometry('720x500')

    tk.Label(company, text="Company", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(company, text="Company name").grid(column=0, row=1)
    tk.Label(company, text="Email id").grid(column=0, row=2)
    tk.Label(company, text="Contact details").grid(column=0, row=3)
    tk.Label(company, text="Street").grid(column=0, row=4)
    tk.Label(company, text="City").grid(column=0, row=5)
    tk.Label(company, text="Zip code").grid(column=0, row=6)



    tk.ttk.Entry(company).grid(column=1, row=1)
    tk.ttk.Entry(company).grid(column=1, row=2)
    tk.ttk.Entry(company).grid(column=1, row=3)
    tk.ttk.Entry(company).grid(column=1, row=4)
    tk.ttk.Entry(company).grid(column=1, row=5)
    tk.ttk.Entry(company).grid(column=1, row=6)


    tk.ttk.Button(company, text="Submit").grid(column=0, row=13, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        company.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        company.grid_columnconfigure(i,  weight =1)

    company.mainloop()
