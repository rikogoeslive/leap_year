from tkinter import *

mainwindow = Tk()
mainwindow.title("Keliamųjų metų programėlė")
mainwindow.geometry("400x300")

l_year = Label(mainwindow, text="Įveskite metus:")
e_year = Entry(mainwindow)
button = Button(mainwindow, text="Patvirtinti")

l_year.grid(row=0, column=0)
e_year.grid(row=0, column=1)
button.grid(row=0, column=2)





mainwindow.mainloop()