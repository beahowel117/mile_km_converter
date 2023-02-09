from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100)

def button_clicked():
    pass


button = Button(text="Calculate", command=button_clicked())
button.grid(column=1, row=2)

input = Entry(width=10)
input.grid(column=1, row=0)

mile_label = Label(text="Mile")
km_label = Label(text="Km")
equal_to_label = Label(text="is equal to")
mile_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equal_to_label.grid(column=0, row=1)


window.mainloop()