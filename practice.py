import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('720x420')
container = ttk.Frame(root, width=720, height=420)
canvas = tk.Canvas(container, width=700, height=400)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)
result_box = []
no_of_results = 10
ini_col = 0
ini_row = 1
for i in range(0, no_of_results):

    tk.Label(scrollable_frame, text="Air India").grid(column=0, row=(1+(i*4)))
    tk.Label(scrollable_frame, text="Journey Begins").grid(column=0, row=2+(i*4))
    tk.Label(scrollable_frame, text="Journey Ends").grid(column=2, row=2+(i*4))
    tk.Label(scrollable_frame, text="Duration").grid(column=1, row=2+(i*4))
    tk.Label(scrollable_frame, text="Cost").grid(column=3, row=2+(i*4))
    tk.Label(scrollable_frame, text="00:00").grid(column=0, row=3+(i*4))
    tk.Label(scrollable_frame, text="12:10").grid(column=2, row=3+(i*4))
    tk.Label(scrollable_frame, text="12h 10m").grid(column=1, row=3+(i*4))
    tk.Label(scrollable_frame, text="Rs.5000").grid(column=3, row=3+(i*4))

    tk.Label(scrollable_frame, text="Seats Available: 69").grid(column=1, row=4+(i*4))
    n_seat_type = tk.StringVar()
    seat_type = ttk.Combobox(scrollable_frame, width = 25, textvariable = n_seat_type)
    seat_type['values'] =             (
                              '------Select seat type------',
                              'Economy',
                              'Business',
                            )
    seat_type.current(0)

    submit = tk.ttk.Button(scrollable_frame, text="Select")
    seat_type.grid(column=0, row=4+(i*4))
    submit.grid(column=2, row=4+(i*4))
# for i in range(50):
#     ttk.Label(scrollable_frame, text="Sample scrolling label").grid()
    # Makes the widgets rsponsive and centered
    n_rows = 30
    n_columns = 3
    for i in range(n_rows):
        root.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        root.grid_columnconfigure(i,  weight =1)

container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
