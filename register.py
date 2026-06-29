from tkinter import ttk
from tkinter import Tk
from tkinter import messagebox as messbox
from createdb import add_users_into_databaise
from mainPage import main_window


root = Tk()
root.geometry("500x500")

login_entry = ttk.Entry(root)
password_entry = ttk.Entry(root, show="*")

def add_users():
    try:
        login = login_entry.get()
        password = password_entry.get()
        if (login and password):
            add_users_into_databaise(login,password)
            login_entry.delete(0, "end")
            password_entry.delete(0, "end")
            messbox.showinfo("Успешно", f"Привет{login}!\nТы зарегистрировался")

        
            root.destroy()
            main_window()
            insert_window()

    except Exception as ex:

        messbox.showerror("Ошибка!", f"Ошибка 404\n{ex}")


button = ttk.Button(root,text= "Зарегистрироватся", command=add_users)
button2 = ttk.Button(root, text="Вход", command=add_users)
login_entry.grid(row=0, column=3, pady=5)
password_entry.grid(row=1, column=3, pady=5)
button.grid(row=2, pady=5, column=3)
button2.grid(row=3, pady=5, column=3)

root.mainloop()