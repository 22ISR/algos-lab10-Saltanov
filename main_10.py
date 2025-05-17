from tkinter import *
from tkinter import ttk
root = Tk()
listbox = Listbox(root, width=30, height=5)
root.title("METANIT.COM")


listbox = Listbox(root, width =30, height = 5)
listbox.pack(pady=10)

def add():
    add_language = entry.get()
    listbox.insert(END, add_language)

entry = ttk.Entry()
entry.pack()
ttk.Button(text="Добавить", command=add).pack()


def delete_selected():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected[0])

delete_button = Button(root, text="Удалить", command=delete_selected)
delete_button.pack()

def clear_selected():
    listbox.delete(0, END)

clear_button = Button(root, text="Очистить всё", command=clear_selected)
clear_button.pack()

root.mainloop()