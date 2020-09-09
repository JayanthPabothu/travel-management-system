import tkinter as tk
from tkinter import ttk

def crud_employee():

    employee = tk.Tk()
    employee.resizable(height = False, width = False)
    employee.title('Travel Management System')
    employee.geometry('720x500')

    tk.Label(employee, text="Employee", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
    tk.Label(employee, text="Emp Name").grid(column=0, row=1)
    tk.Label(employee, text="Gender").grid(column=0, row=2)
    tk.Label(employee, text="Salary").grid(column=0, row=3)
    tk.Label(employee, text="Aadhar no").grid(column=0, row=4)
    tk.Label(employee, text="Contact details").grid(column=0, row=5)
    tk.Label(employee, text="DOB").grid(column=0, row=6)
    tk.Label(employee, text="Street").grid(column=0, row=7)
    tk.Label(employee, text="City").grid(column=0, row=8)
    tk.Label(employee, text="Zipcode").grid(column=0, row=9)
    tk.Label(employee, text="Emp role").grid(column=0, row=10)
    tk.Label(employee, text="Mgr_id").grid(column=0, row=11)
    tk.Label(employee, text="Vechile_id").grid(column=0, row=12)
    tk.Label(employee, text="Company_id").grid(column=0, row=13)



    tk.ttk.Entry(employee).grid(column=1, row=1)
    tk.ttk.Entry(employee).grid(column=1, row=2)
    tk.ttk.Entry(employee).grid(column=1, row=3)
    tk.ttk.Entry(employee).grid(column=1, row=4)
    tk.ttk.Entry(employee).grid(column=1, row=5)
    tk.ttk.Entry(employee).grid(column=1, row=6)
    tk.ttk.Entry(employee).grid(column=1, row=7)
    tk.ttk.Entry(employee).grid(column=1, row=8)
    tk.ttk.Entry(employee).grid(column=1, row=9)
    tk.ttk.Entry(employee).grid(column=1, row=10)
    tk.ttk.Entry(employee).grid(column=1, row=11)
    tk.ttk.Entry(employee).grid(column=1, row=12)
    tk.ttk.Entry(employee).grid(column=1, row=13)


    tk.ttk.Button(employee, text="Submit").grid(column=0, row=24, columnspan=2)

    # Makes the widgets responsive and centered
    n_rows = 20
    n_columns = 2
    for i in range(n_rows):
        employee.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        employee.grid_columnconfigure(i,  weight =1)

    employee.mainloop()
