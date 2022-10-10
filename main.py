from tkinter import *
from turtle import st

window = Tk()
window.title("Temperature Converter")
window.geometry("400x50")
window.minsize(580, 50)
window.maxsize(700, 80)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1, minsize=250)
window.columnconfigure(1, weight=1, minsize=80)
window.columnconfigure(2, weight=1, minsize=250)



def convert():
    celsius = (float(Ent_temp.get()) - 32) * (5 / 9)
    Label_result["text"] = f"{round(celsius, 2)}"


Ent_temp = Entry(master=window, borderwidth=5)
Ent_temp.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

Label_F = Label(Ent_temp , text="\N{DEGREE FAHRENHEIT}", bg="white")
Label_F.pack(side=RIGHT, padx=5, pady=5)

Button_1 = Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=convert, padx=20, pady=20, bg="green", fg="white", height=1)
Button_1.grid(row=0, column=1, padx=5, pady=5, sticky="we")

Label_result = Label(master=window, fg="black", bg="white", padx=150)
Label_result.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

Label_C = Label(Label_result , text="\N{DEGREE CELSIUS}", bg="white")
Label_C.pack(side=RIGHT)

window.mainloop()
