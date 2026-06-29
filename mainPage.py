from tkinter import ttk
from tkinter import Tk

def main_window():
    main = Tk()

    main.geometry("500x500")

    info_txt = ttk.Label(main, text="Добро пожаловать на борт!")

    info_txt.grid(row=0, column=0)

    main.mainloop()