# Знакомство с виджетамию Виджет Label

import tkinter as tk

if __name__ == '__main__':
    win = tk.Tk()
    win.geometry(f"300x400+100+200")
    win.title("Мое первое графическое приложение")

    label_1 = tk.Label(win, text='''Hello!
world!''',
                       bg='red',
                       fg='white',
                       font=('Arial', 15, 'bold'),
                       padx=20,
                       pady=40,
                       width=20,
                       height=10,
                       anchor='sw',
                       relief=tk.RAISED,
                       bd=10,
                       justify=tk.RIGHT,
                       )
    label_1.pack()

    win.mainloop()