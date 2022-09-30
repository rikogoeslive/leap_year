from tkinter import *
import webbrowser

mainwindow = Tk()
mainwindow.title("Keliamųjų metų programėlė")
mainwindow.geometry("400x500+800+250")

meniu = Menu(mainwindow)
mainwindow.config(menu=meniu)
submenu = Menu(meniu, tearoff=0)

def howto():
    webbrowser.open("https://lt.wikipedia.org/wiki/Keliamieji_metai")

meniu.add_cascade(label="Parinktys:", menu=submenu)
submenu.add_cascade(label="Kaip tai apskaičiuoti ?!", command=howto)
submenu.add_separator()
submenu.add_cascade(label="Išeiti iš programos", command=quit)


def calculation():
    years = int(e_year.get())
    if (years % 400 == 0) or (years %100 != 0 and years %4 ==0): 
        l_result["text"] = f"{years} yra keliamieji metai!"
    else:
        l_result["text"] = f"{years} metai nėra keliamieji!"

def calculation_from_till():
    year_from = int(e_year_from.get())
    year_till = int(e_year_till.get())
    if year_from <= year_till:
        leap_years = [str(x) for x in range(year_from, year_till) if x % 4==0 and (x % 100 !=0 or x %400 ==0)]
        leap_years[-1] += "."
        l_result["text"] = (f"Štai sąrašas keliamųjų metų nuo {year_from} iki {year_till}:\n{(', '.join(leap_years))}")
    else:
        l_result["text"] = "Įvesti pirmieji metai negali būti didesni už antruosius <3!"
       

l_year = Label(mainwindow, text="Įveskite metus:")
e_year = Entry(mainwindow)
button = Button(mainwindow, text="Patvirtinti", command=calculation)
l_year_from = Label(mainwindow, text="Įveskite metus nuo:")
e_year_from = Entry(mainwindow)
l_year_till = Label(mainwindow, text="iki:")
e_year_till = Entry(mainwindow)
button2 = Button(mainwindow, text="Patvirtinti", command=calculation_from_till)
l_result = Label(mainwindow, text="", bd=5, relief=SUNKEN, anchor=W)


l_year.grid(row=0, column=0)
e_year.grid(row=0, column=1)
button.grid(row=0, column=2)
l_year_from.grid(row=1, column=0)
e_year_from.grid(row=1, column=1)
l_year_till.grid(row=1, column=2)
e_year_till.grid(row=1, column=3)
button2.grid(row=1, column=4)
l_result.grid(row=2, columnspan=5, sticky=W+E)


mainwindow.mainloop()





