from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox as messbox
from createdb import add_users_into_databaise


root = Tk()
root.geometry("500x500")

login_entry = ttk.Entry(root)
password_entry = ttk.Entry(root, show="*")

def add_users():
    try:
        login = login_entry.get()
        password = password_entry.get()
        add_users_into_databaise(login,password)
        login_entry.delete(0, "end")
        password_entry.delete(0, "end")
        messbox.showinfo("Успешно", f"Привет{login}!\nТы зарегистрировался")

    except Exception as ex:

        messbox.showerror("Ошибка!", f"Ошибка 404\n{ex}")


button = ttk.Button(root,text= "Зарегистрироватся", command=add_users)
login_entry.grid(row=0, column=0, pady=5)
password_entry.grid(row=1, column=0, pady=5)
button.grid(row=2, pady=5, column=0)

root.mainloop()