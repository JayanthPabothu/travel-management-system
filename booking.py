import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def booking_screen():

    root = tk.Tk()
    root.geometry('720x420')
    root.resizable(height = False, width = False)
    container = tk.Frame(root, width=720, height=420, bg="blue")
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

    font10 = Font(family='Arial', size=10)
    font15 = Font(family='Arial', size=15)
    font20 = Font(family='Arial', size=20)
    font30 = Font(family='Arial', size=30, weight='bold')

    data_dict = {
        'flight_id':[0, 1, 2],
        'model_name':[0, 1, 2],
        'start_city':[],
        'dest_city':[],
        'start_time':[],
        'duration':[],
        'end_time':[],
        'comp_name':[],
        'start_airport':[],
        'dest_airport':[],
    }


    no_of_results = 5
    for i in range(no_of_results):

        tk.Label(scrollable_frame, text="Air India", font=font20).grid(column=0, row=0+(6*i), padx=70)

        tk.Label(scrollable_frame, text="Delhi", font=font15).grid(column=0, row=1+(6*i))
        tk.Label(scrollable_frame, text="12:00", font=font30).grid(column=0, row=2+(6*i))
        tk.Label(scrollable_frame, text="Indira Gandhi Airport", font=font10).grid(column=0, row=3+(6*i))

        tk.Label(scrollable_frame, text="02h 40m", font=font10).grid(column=2, row=1+(6*i), sticky="S")
        tk.Label(scrollable_frame, text="---------------->", font=font20).grid(column=2, row=2+(6*i))

        tk.Label(scrollable_frame, text="Boeing 777-300ER", font=font10).grid(column=4, row=0+(6*i), padx=70)
        tk.Label(scrollable_frame, text="Mumbai", font=font15).grid(column=4, row=1+(6*i))
        tk.Label(scrollable_frame, text="14:30", font=font30).grid(column=4, row=2+(6*i))
        tk.Label(scrollable_frame, text="Chhatrapati Shivaji Airport", font=font10).grid(column=4, row=3+(6*i))
        tk.Label(scrollable_frame, text="AI-201", font=font10).grid(column=2, row=3+(6*i), sticky="N")

        tk.ttk.Button(scrollable_frame, text="Book now").grid(column=2, row=4+(6*i), pady=(10, 70))
    # for i in range(0, no_of_results):
    #
    #     tk.Label(scrollable_frame, text="Air India").grid(column=0, row=(1+(i*4)))
    #     tk.Label(scrollable_frame, text="Journey Begins").grid(column=0, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Journey Ends").grid(column=2, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Duration").grid(column=1, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="Cost").grid(column=3, row=2+(i*4))
    #     tk.Label(scrollable_frame, text="00:00").grid(column=0, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="12:10").grid(column=2, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="12h 10m").grid(column=1, row=3+(i*4))
    #     tk.Label(scrollable_frame, text="Rs.5000").grid(column=3, row=3+(i*4))
    #
    #     tk.Label(scrollable_frame, text="Seats Available: 69").grid(column=1, row=4+(i*4))
    #     n_seat_type = tk.StringVar()
    #     seat_type = ttk.Combobox(scrollable_frame, width = 25, textvariable = n_seat_type)
    #     seat_type['values'] =             (
    #                               '------Select seat type------',
    #                               'Economy',
    #                               'Business',
    #                             )
    #     seat_type.current(0)
    #
    #     submit = tk.ttk.Button(scrollable_frame, text="Select")
    #     seat_type.grid(column=0, row=4+(i*4))
    #     submit.grid(column=2, row=4+(i*4))

    n_rows = 30
    n_columns = 10
    for i in range(n_rows):
        root.grid_rowconfigure(i,  weight =1)
    for i in range(n_columns):
        root.grid_columnconfigure(i,  weight =1)

    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()
booking_screen()
