from tkinter import *

mainwindow = Tk()
mainwindow.title("Keliamųjų metų programėlė")
mainwindow.geometry("400x300")

meniu = Menu(mainwindow)
mainwindow.config(menu=meniu)
submenu = Menu(meniu, tearoff=0)
submenu2 = Menu(meniu, tearoff=0)
submenu3 = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Parinktys:", menu=submenu)
submenu.add_cascade(label="Skaičiuoti nuo iki...")
submenu.add_cascade(label="Kaip tai apskaičiuoti ?!")
submenu.add_separator()
submenu.add_cascade(label="Išeiti iš programos")


def calculation():
    years = int(e_year.get())
    if (years % 400 == 0) or (years %100 != 0 and years %4 ==0): 
        l_result["text"] = f"{years} yra keliamieji metai!"
    else:
        l_result["text"] = f"{years} metai nėra keliamieji!"


l_year = Label(mainwindow, text="Įveskite metus:")
e_year = Entry(mainwindow)
button = Button(mainwindow, text="Patvirtinti", command=calculation)
l_result = Label(mainwindow, text="", bd=5, relief=SUNKEN, anchor="w")


l_year.grid(row=0, column=0)
e_year.grid(row=0, column=1)
button.grid(row=0, column=2)
l_result.grid(row=1, columnspan=5, sticky=W+E)


mainwindow.mainloop()





