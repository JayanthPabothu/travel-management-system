import tkinter as tk
from tkinter import ttk
import journey
from functools import partial
from tkinter.font import Font
import update_user

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def get_update(homepage, id):
    homepage.destroy()
    update_user.update_user(id)


def logout(homepage):
    homepage.destroy()
    import login
    login.main_screen()

def homepage_screen(user_id, user_email, user_name, credit_points):


    def get_journey():
        homepage.destroy()
        journey.journey_screen(user_id)


    homepage = tk.Tk()
    homepage.resizable(height = False, width = False)
    homepage.title('Flight Management System')
    homepage.geometry('720x420')
    background_h = tk.PhotoImage(file='Images/homepage.png')
    background_label_h = tk.Label(homepage,  image=background_h)
    background_label_h.place(x=0, y=0, relwidth=1, relheight=1)
    adam = Font(family="ADAM.CG PRO", size=20)


    heading = tk.Label(homepage, text="Welcome "+user_name,font=adam)
    heading.place(x=230, y=30)
    heading.configure(bg=_from_rgb((128, 159, 186)))

    credits = tk.Label(homepage, text="Credits: "+str(credit_points))
    credits.place(x=5, y=7)
    credits.configure(bg=_from_rgb((128, 159, 186)))

    tk.ttk.Button(homepage, text="Logout", command=partial(logout, homepage)).place(x=640, y=5)

    book = tk.Button(homepage, text="Book a ticket", command=get_journey)
    book.place(x=100, y=200)
    book.config(width=17, height=2)

    history = tk.Button(homepage, text="Get Booking History")
    history.place(x=500, y=200)
    history.config(width=17, height=2)
    #tk.ttk.Button(homepage, text="Edit Details", command=partial(update_user.update_user, user_id, homepage)).grid(column=0, columnspan=3,row=4)

    profile = tk.Button(homepage, text="Profile", command=partial(get_update, homepage, user_id))
    profile.place(x=305, y=360)
    profile.config(width=17, height=2)

    homepage.mainloop()
# homepage_screen(2, 'jaya@', 'Jayanth', 0)
