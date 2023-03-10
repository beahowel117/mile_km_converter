from tkinter import *

window = Tk()
window.minsize(width=150, height=150)
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
FONT = ("Ink Free", 18, "bold")

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")


button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

miles_input = Entry(width=7, font=FONT)
miles_input.grid(column=1, row=0)

mile_label = Label(text="Mile", font=FONT)
km_label = Label(text="Km", font=FONT)
equal_to_label = Label(text="is equal to", font=FONT)
km_result_label = Label(text="0", font=FONT)
mile_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equal_to_label.grid(column=0, row=1)
km_result_label.grid(column=1, row=1)


window.mainloop()