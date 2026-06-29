from tkinter import ttk
from tkinter import Tk

def insert_window():
    insert = Tk()

    insert.geometry("500x500")

    info_txt = ttk.Label(insert, text="ВХОД")

    info_txt.grid(row=0, column=0)

    insert.mainloop()