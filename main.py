import tkinter as tk
from tkinter.ttk import *

window = tk.Tk()
window.resizable(height = False, width = False)
window.title('Travel Management System')
window.geometry('1080x720')
heading = tk.Label(window, text="Travel Management System", font=('Helvetica', '25'))

login_head = tk.Label(window, text="Login here", bg='grey',font=('Helvetica', '20'))
register_head = tk.Label(window, text="Register here", bg='grey',font=('Helvetica', '20'))

description = tk.Label(window, bg='grey', text="\n\n\n\n\n\n")


# ----------Creating labels---------
login_email = tk.Label(window, text="Enter your Email Id")
login_password = tk.Label(window, text="Enter your Password")

register_name = tk.Label(window, text="Enter your Name")
register_email = tk.Label(window, text="Enter your Email Id")
register_password = tk.Label(window, text="Enter your Password")
register_password_again =  tk.Label(window, text="Enter your Password again")
register_DOB = []
register_DOB.append(tk.Label(window, text="Enter yor Date of Birth(eg. 10 08 2020)"))
register_DOB.append(tk.Label(window, text="D:"))
register_DOB.append(tk.Label(window, text="M:"))
register_DOB.append(tk.Label(window, text="Y:"))
register_gender = tk.Label(window, text="Gender")
register_street=tk.Label(window, text="Street")
register_city = tk.Label(window, text="City")
register_zipcode = tk.Label(window, text="Zipcode")
register_contact = tk.Label(window, text="Contact number")

# ----------Creating entries----------
login_entry_email = tk.Entry()
login_entry_password = tk.Entry()

register_entry_name = tk.Entry()
register_entry_email = tk.Entry()
register_entry_password = tk.Entry()
register_entry_password_again = tk.Entry()
register_entry_street = tk.Entry()
register_entry_city = tk.Entry()
register_entry_zipcode = tk.Entry()
register_entry_contact = tk.Entry()
register_entry_day = tk.Entry(width=10)
register_entry_month = tk.Entry(width=10)
register_entry_year = tk.Entry(width=10)
g = tk.IntVar()

gender1 = tk.Radiobutton(window, text="M", variable=g, value=1)
gender2 = tk.Radiobutton(window, text="F", variable=g, value=2)
gender3 = tk.Radiobutton(window, text="T", variable=g, value=3)


login_button = Button(window, text="Login")
register_button = Button(window, text="Register")

# ----------Placing on grid-----------
heading.grid(columnspan=7)
description.grid(column=0, row=1,columnspan=7)
# login stuff
login_head.grid(column=0, row=2, columnspan=2)
register_head.grid(column=2, row=2, columnspan=4)
login_email.grid(column=0, row=3)
login_password.grid(column=0, row=4)
login_entry_email.grid(column=1, row=3)
login_entry_password.grid(column=1, row=4)
login_button.grid(column=0, row=5, columnspan=2)

# register labels
register_name.grid(column=2, row=3)
register_email.grid(column=2, row=4)
register_password.grid(column=2, row=5)
register_password_again.grid(column=2, row=6)
register_gender.grid(column=2, row=7)
register_street.grid(column=2, row=8)
register_city.grid(column=2, row=9)
register_zipcode.grid(column=2, row=10)
register_contact.grid(column=2, row=11)
register_DOB[0].grid(column=2, row=12)
register_DOB[1].grid(column=3, row=12)
register_DOB[2].grid(column=4, row=12)
register_DOB[3].grid(column=5, row=12)

# register entries
register_entry_name.grid(column=3, row=3, columnspan=3)
register_entry_email.grid(column=3, row=4, columnspan=3)
register_entry_password.grid(column=3, row=5, columnspan=3)
register_entry_password_again.grid(column=3, row=6, columnspan=3)
gender1.grid(column=3, row=7)
gender2.grid(column=4, row=7)
gender3.grid(column=5, row=7)
register_entry_street.grid(column=3, row=8, columnspan=3)
register_entry_city.grid(column=3, row=9, columnspan=3)
register_entry_zipcode.grid(column=3, row=10, columnspan=3)
register_entry_contact.grid(column=3, row=11, columnspan=3)
register_entry_day.grid(column=3, row=12)
register_entry_month.grid(column=4, row=12)
register_entry_year.grid(column=5, row=12)

register_button.grid(column=2, row=15, columnspan=2)




n_rows = 15
n_columns = 7
for i in range(n_rows):
    window.grid_rowconfigure(i,  weight =1)
for i in range(n_columns):
    window.grid_columnconfigure(i,  weight =1)

window.mainloop()
