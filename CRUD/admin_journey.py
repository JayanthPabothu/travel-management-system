import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

admin_journey = tk.Tk()
admin_journey.resizable(height = False, width = False)
admin_journey.title('Travel Management System')
admin_journey.geometry('800x600')

#tk.Label(admin_journey, text="admin_journey", font=('Helvetica', '25')).grid(column=0, row=0, columnspan=2)
tk.Label(admin_journey, text="Journey Date").grid(row = 0, column = 0)
tk.Label(admin_journey, text="Status").grid(row = 1, column = 0)
tk.Label(admin_journey, text="Flight No").grid(row = 0, column = 3)
tk.ttk.Button(admin_journey, text="Search",  width = 12).grid(row= 1, column=3)



journey_date = tk.ttk.Entry(admin_journey)
journey_date.grid(row = 0, column = 1)
status = tk.ttk.Entry(admin_journey)
status.grid(row = 1, column = 1)
flight_no = tk.ttk.Entry(admin_journey)
flight_no.grid(row = 0, column =4)



admin_journey_list = tk.Listbox(admin_journey, height = 17, width = 50)
admin_journey_list.grid(row = 3, column = 0, columnspan = 2, rowspan = 4)


# admin_journey_list.bind('<<ListboxSelect>>', get_selected_row)

sb1= tk.Scrollbar(admin_journey, width = 10)
sb1.grid(row=3, column=1, columnspan = 3, rowspan = 6)

admin_journey_list.configure(yscrollcommand = sb1.set)
sb1.configure(command = admin_journey_list.yview)


admin_journey_list1 = tk.Listbox(admin_journey, height = 17, width = 50)
admin_journey_list1.grid(row = 3, column = 2, columnspan = 4, rowspan = 4)

sb1= tk.Scrollbar(admin_journey, width = 10)
sb1.grid(row=3, column=5, columnspan =5 , rowspan = 6)

admin_journey_list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = admin_journey_list1.yview)






tk.ttk.Button(admin_journey, text="Insert",  width = 12).grid(row= 7, column=0)
tk.ttk.Button(admin_journey, text="Update",  width = 12).grid(row= 7, column=1)
tk.ttk.Button(admin_journey, text="Delete", width = 12).grid(row= 7, column=3)
tk.ttk.Button(admin_journey, text="View All",  width = 12).grid(row= 7, column=4)


# Makes the widgets responsive and centered
n_rows = 12
n_columns = 6
for i in range(n_rows):
    admin_journey.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    admin_journey.grid_columnconfigure(i,  weight =1)

admin_journey.mainloop()
# crud_admin_journey()
