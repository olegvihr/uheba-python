# Знакомство с виджетами. Виджет Button

import tkinter as tk

count = 0

def sey_hello():
    print('Hello')

def add_label():
    label = tk.Label(win, text='new')
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f"Счетчик: {count}"



if __name__ == '__main__':
    win = tk.Tk()
    win.geometry(f"400x500+100+200")
    win.title("Мое первое графическое приложение")

    btn1 = tk.Button(win, text="Hello",
                     command=sey_hello
                     )
    btn2 = tk.Button(win, text="Add new label",
                     command=add_label
                     )
    btn3 = tk.Button(win, text="Add new label lambda ",
                     command=lambda: tk.Label(win, text='new lambda').pack(),
                     )
    btn4 = tk.Button(win, text=f"Счетчик: {count}",
                     command=counter,
                     activebackground='red',
                     bg='green',
                     state=tk.NORMAL,  # DISABLED
                     )

    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()

    win.mainloop()
