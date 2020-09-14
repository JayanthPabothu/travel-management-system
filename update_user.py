import tkinter as tk
from tkinter import ttk
from functools import partial
import mysql.connector as mysql
import datetime as dt
from tkinter import messagebox
from tkinter.font import Font

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def update_user(user_id):

    def update_data(user_id, update):
        name1 = entry_name1.get()
        email1 = entry_email.get()
        password1 = entry_password.get()
        DOB_day1 = entry_day.get()
        DOB_month1 = entry_month.get()
        DOB_year1 = entry_year.get()
        street1 = entry_street.get()
        city1 = entry_city.get()
        zipcode1 = entry_zipcode.get()
        phone1 = entry_contact.get()
        dob = str(DOB_year1)+'-'+str(DOB_month1)+'-'+str(DOB_day1)


        if(name1=='' or email1=='' or password1=='' or street1=='' or city1=='' or phone1=='' or DOB_day1=='' or DOB_month1 == '' or DOB_year1 == '' or zipcode1 == ''):
            messagebox.showwarning("Invalid request", "Please make sure you have filled all the fields.")
        else:

            con1 = mysql.connect(
                    host="localhost",
                    user="root",
                    password="testpassword",
                    database="FMS"
                    )
            cursor1 = con1.cursor()
            cursor1.execute("SELECT EXISTS(SELECT EMAIL_ID FROM CUSTOMER WHERE CUSTOMER_ID<>%s AND EMAIL_ID=%s);", [str(user_id), str(email1)])
            check = cursor1.fetchmany(size=1)
            if check[0][0] == 1:
                messagebox.showwarning("Invalid request", "Email ID has already been taken. Please select another email id.")
            else:
                args = cursor1.callproc("UPDATE_CUST_DETAILS", [int(user_id), str(name1), str(email1), str(password1), str(dob), str(street1), str(city1), int(zipcode1), int(phone1)])
                cursor1.execute("commit")
                messagebox.showinfo("Updation successful", "Your data has been successfully updated.")
                update.destroy()
                import login
                login.main_screen()
            cursor1.close()
            con1.close()


    update = tk.Tk()
    update.resizable(height = False, width = False)
    update.title('Flight Management System')
    update.geometry('720x420')
    adam = Font(family="ADAM.CG PRO", size=20)
    # heading = tk.Label(login, text="Travel Management System")
    # register_head = tk.Label(login, text="Register here", bg='grey',font=('Helvetica', '20'))

    background = tk.PhotoImage(file='Images/edit.png')
    background_label = tk.Label(update,  image=background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    con = mysql.connect(
            host="localhost",
            user="root",
            password="testpassword",
            database="FMS"
        )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID=%s", [int(user_id)])
    records = cursor.fetchmany(size=1)[0]

    name = tk.Label(update, text="Name:")
    name.place(x=500, y=50)
    name.configure(bg=_from_rgb((128, 159, 186)))

    email_id = tk.Label(update, text="Email Id:")
    email_id.place(x=500, y=80)
    email_id.configure(bg=_from_rgb((128, 159, 186)))

    password = tk.Label(update, text="Password:")
    password.place(x=500, y=110)
    password.configure(bg=_from_rgb((128, 159, 186)))

    register_DOB = tk.Label(update, text="DOB")
    register_DOB.place(x=500, y=140)
    register_DOB.configure(bg=_from_rgb((128, 159, 186)))

    day = tk.Label(update, text="D:")
    day.place(x=565, y=140)
    day.configure(bg=_from_rgb((128, 159, 186)))

    month = tk.Label(update, text="M:")
    month.place(x=610, y=140)
    month.configure(bg=_from_rgb((128, 159, 186)))

    year = tk.Label(update, text="Y:")
    year.place(x=663, y=140)
    year.configure(bg=_from_rgb((128, 159, 186)))

    street = tk.Label(update, text="Street:")
    street.place(x=500, y=170)
    street.configure(bg=_from_rgb((128, 159, 186)))

    city = tk.Label(update, text="City:")
    city.place(x=500, y=200)
    city.configure(bg=_from_rgb((128, 159, 186)))

    zipcode = tk.Label(update, text="Zipcode:")
    zipcode.place(x=500, y=230)
    zipcode.configure(bg=_from_rgb((128, 159, 186)))

    contact = tk.Label(update, text="Contact:")
    contact.place(x=500, y=260)
    contact.configure(bg=_from_rgb((128, 159, 186)))

    # Entries
    entry_name1 = tk.Entry(update)
    entry_name1.insert(0, records[1])
    entry_name1.place(x=580, y=50)

    entry_email = tk.Entry(update)
    entry_email.insert(0, records[2])
    entry_email.place(x=580, y=80)

    entry_password = tk.Entry(update)
    entry_password.insert(0, records[3])
    entry_password.place(x=580, y=110)

    entry_day = tk.Entry(update,width=4)
    entry_day.insert(0, records[5].strftime("%d"))
    entry_day.place(x=580, y=140)

    entry_month = tk.Entry(update,width=4)
    entry_month.insert(0, records[5].strftime("%m"))
    entry_month.place(x=630, y=140)

    entry_year = tk.Entry(update,width=6)
    entry_year.insert(0, records[5].strftime("%Y"))
    entry_year.place(x=678, y=140)

    entry_street = tk.Entry(update)
    entry_street.insert(0, records[6])
    entry_street.place(x=580, y=170)

    entry_city = tk.Entry(update)
    entry_city.insert(0, records[7])
    entry_city.place(x=580, y=200)

    entry_zipcode = tk.Entry(update)
    entry_zipcode.insert(0, records[8])
    entry_zipcode.place(x=580, y=230)

    entry_contact = tk.Entry(update)
    entry_contact.insert(0, records[9])
    entry_contact.place(x=580, y=260)


    update = tk.ttk.Button(update, text="Update values", command=partial(update_data, user_id, update))
    update.place(x=550, y=300)

    update.mainloop()

# update_user(2)
