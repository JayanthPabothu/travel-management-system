import tkinter as tk
from tkinter import ttk
from functools import partial
from CRUD import flight, company

def create_query(num):
    print(table_name[num]+" Create")
    if (num == 2):
        flight.run()
    elif (num == 6):
        company.crud_company()

def update_query(num):
    print(table_name[num]+" Update")

def delete_query(num):
    print(table_name[num]+" Delete")

admin = tk.Tk()
admin.resizable(height = False, width = False)
admin.title('Travel Management System')
admin.geometry('720x500')


tk.Label(admin, text="Admin Panel", font=('Helvetica', '25')).grid(column=1, row=0, columnspan=2)


table_name = ['BUS', 'CAR', 'FLIGHT', 'CITY', 'ROUTE', 'AMENITIES', 'COMPANY', 'EMPLOYEE']
row_counter = 4
add_row = 0
i = -1
counter = 0
while(counter<8):
    i = (i+1)%4
    tk.Label(admin, text=table_name[counter], font=('Helvetica', '15')).grid(column=0+i, row=1+add_row)
    tk.ttk.Button(admin, text="Create an Entry", command=partial(create_query, counter)).grid(column=0+i, row=2+add_row)
    tk.ttk.Button(admin, text="Update an Entry", command=partial(update_query, counter)).grid(column=0+i, row=3+add_row)
    tk.ttk.Button(admin, text="Delete an Entry", command=partial(delete_query, counter)).grid(column=0+i, row=4+add_row)
    row_counter-=1
    counter+=1

    if row_counter == 0:
        add_row = 4
        row_counter = 5

# Makes the widgets responsive and centered
n_rows = 15
n_columns = 4
for i in range(n_rows):
    admin.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    admin.grid_columnconfigure(i,  weight =1)

admin.mainloop()
