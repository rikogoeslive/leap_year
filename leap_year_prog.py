from tkinter import *

mainwindow = Tk()
mainwindow.title("Keliamųjų metų programėlė")
mainwindow.geometry("400x300")

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





