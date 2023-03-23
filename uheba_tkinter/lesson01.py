# Введение в tkinter. Главное окно

import tkinter as tk


if __name__ == '__main__':
    win = tk.Tk()
    h = 500
    w = 600
    photo = tk.PhotoImage(file='fun.png')
    win.iconphoto(False, photo)
    win.config(bg='#7a19bf')
    win.title("Мое первое графическое приложение")
    win.geometry(f"{h}x{w}+100+200")
    win.minsize(300, 400)
    win.maxsize(700, 800)
    win.resizable(True, True)
    win.mainloop()
