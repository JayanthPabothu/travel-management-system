import tkinter as tk
from tkinter.ttk import *
import login

def about_screen():

    def on_closing():
        about.destroy()
        login.main_screen()

    about = tk.Tk()
    about.resizable(height = False, width = False)
    about.title('Flight Management System')
    about.geometry('720x420')
    background_a = tk.PhotoImage(file='Images/about1.png')
    background_label_a = tk.Label(about,  image=background_a)
    background_label_a.place(x=0, y=0, relwidth=1, relheight=1)

    about.protocol("WM_DELETE_WINDOW", on_closing)

    about.mainloop()
