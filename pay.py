import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import mysql.connector as mysql
from mysql.connector import Error
from tkinter import messagebox

def pay_screen(flight_id, user_id, journey_id):

    def book_ticket():
        c1 = c.get()
        price = 0
        seat_num = 0
        seat_type = ""
        print(c1)
        print(seats_p.get())
        if (c1 == 1 and seats_fc.get() != ""):
            seat_num = seats_fc.get()
            seat_type = "FIRSTCLASS"
            price = price_fc_val

        elif (c1 == 2 and seats_e.get() != ""):
            seat_num = seats_e.get()
            seat_type = "ECONOMY"
            price = price_e_val

        elif (c1 == 3 and seats_b.get() != ""):
            seat_num = seats_b.get()
            seat_type = "BUSINESS"
            price = price_b_val

        elif (c1 == 4 and seats_p.get() != ""):
            seat_num = seats_p.get()
            seat_type = "PREMIUM"
            price = price_p_val
            print(seat_type)

        else:
            messagebox.showwarning("Invalid request", "Please choose a valid seat.")

        print(seat_type)
        cursor.callproc("INSERT_FLIGHT_BOOKING", [journey_id, user_id, price, seat_type, seat_num])
        cursor.execute("commit")
        messagebox.showinfo("Status", "Your ticket has been successfully booked!")

    con = mysql.connect(
        host="localhost",
        user="root",
        password="testpassword",
        database="FMS",
        port = 3306
        )
    cursor = con.cursor()

    cursor.execute("SELECT NO_OF_FIRSTCLASS_SEATS, NO_OF_ECONOMY_SEATS, NO_OF_BUSINESS_SEATS, NO_OF_PREMIUM_SEATS, PRICE FROM FLIGHT WHERE FLIGHT_NO=%s;", ['AI 111'])
    rec = cursor.fetchmany(size=1)
    fc_seats = [i for i in range(1, rec[0][0]+1)]
    e_seats = [i for i in range(1, rec[0][1]+1)]
    b_seats = [i for i in range(1, rec[0][2]+1)]
    p_seats = [i for i in range(1, rec[0][3]+1)]
    base_price = rec[0][4]

    cursor.execute("SELECT * FROM PRICE_FACTOR;")
    factors = cursor.fetchall()[0]


    cursor.execute("SELECT SEAT_NO FROM BOOKS_FLIGHT WHERE JOURNEY_ID=%s AND SEAT_TYPE=%s;", [journey_id, 'FIRSTCLASS'])
    fc = cursor.fetchall()
    if(len(fc)==0):
        fc=[0]
    else:
        fc = [int(i[0]) for i in fc]
    print(fc)
    cursor.execute("SELECT SEAT_NO FROM BOOKS_FLIGHT WHERE JOURNEY_ID=%s AND SEAT_TYPE=%s;", [journey_id, 'ECONOMY'])
    e = cursor.fetchall()
    if(len(e)==0):
        e=[0]
    else:
        e = [int(i[0]) for i in e]
    cursor.execute("SELECT SEAT_NO FROM BOOKS_FLIGHT WHERE JOURNEY_ID=%s AND SEAT_TYPE=%s;", [journey_id, 'BUSINESS'])
    b = cursor.fetchall()
    if(len(b)==0):
        b=[0]
    else:
        b = [int(i[0]) for i in b]
    cursor.execute("SELECT SEAT_NO FROM BOOKS_FLIGHT WHERE JOURNEY_ID=%s AND SEAT_TYPE=%s;", [journey_id, 'PREMIUM'])
    p = cursor.fetchall()
    if(len(p)==0):
        p=[0]
    else:
        p = [int(i[0]) for i in p]

    pay_window = tk.Toplevel()
    pay_window.resizable(height = False, width = False)
    pay_window.title('Flight Management System')
    pay_window.geometry('500x320')

    c = tk.IntVar()

    class1 = tk.Radiobutton(pay_window, text="First Class", variable=c, value=1)
    class2 = tk.Radiobutton(pay_window, text="Economy", variable=c, value=2)
    class3 = tk.Radiobutton(pay_window, text="Business", variable=c, value=3)
    class4 = tk.Radiobutton(pay_window, text="Premium", variable=c, value=4)

    class1.place(x=50, y=70)
    class2.place(x=160, y=70)
    class3.place(x=270, y=70)
    class4.place(x=380, y=70)

    #class1.configure(bg=_from_rgb((133, 237, 157)))
    #class2.configure(bg=_from_rgb((133, 237, 157)))
    #class3.configure(bg=_from_rgb((133, 237, 157)))
    #class4.configure(bg=_from_rgb((133, 237, 157)))

    seatnofc = tk.StringVar()
    seats_fc = ttk.Combobox(pay_window, height=5, width = 10, textvariable = seatnofc)
    seats_fc['values'] = list(set(fc_seats)-set(fc))
    seats_fc.place(x=50, y=110)

    seatnoe = tk.StringVar()
    seats_e = ttk.Combobox(pay_window, height=5, width = 10, textvariable = seatnoe)
    seats_e['values'] = list(set(e_seats)-set(e))
    seats_e.place(x=160, y=110)

    seatnob = tk.StringVar()
    seats_b = ttk.Combobox(pay_window, height=5, width = 10, textvariable = seatnob)
    seats_b['values'] = list(set(b_seats)-set(b))
    seats_b.place(x=270, y=110)


    seatnop = tk.StringVar()
    seats_p = ttk.Combobox(pay_window, height=5, width = 10, textvariable = seatnop)
    seats_p['values'] = list(set(p_seats)-set(p))
    seats_p.place(x=380, y=110)

    price = "Price:"
    price = tk.Label(pay_window, text=price)
    price.place(x=0 , y=150)
    #price.configure(bg=_from_rgb((133, 237, 157)))


    price_fc_val = str(base_price*factors[0])
    price_fc = tk.Label(pay_window, text=price_fc_val)
    price_fc.place(x=65 , y=150)
    #price_fc.configure(bg=_from_rgb((133, 237, 157)))

    price_e_val = str(base_price*factors[1])
    price_e = tk.Label(pay_window, text=price_e_val)
    price_e.place(x=175 , y=150)
    #price_e.configure(bg=_from_rgb((133, 237, 157)))

    price_b_val = str(base_price*factors[2])
    price_b = tk.Label(pay_window, text=price_b_val)
    price_b.place(x=285 , y=150)
    #price_b.configure(bg=_from_rgb((133, 237, 157)))

    price_p_val = str(base_price*factors[3])
    price_p= tk.Label(pay_window, text=price_p_val)
    price_p.place(x=395 , y=150)
    #price_p.configure(bg=_from_rgb((133, 237, 157)))

    tk.ttk.Button(pay_window, text="Pay", command=book_ticket).place(x=210, y=220)

    pay_window.mainloop()

# pay_screen('AI 0946', 1, 1)
