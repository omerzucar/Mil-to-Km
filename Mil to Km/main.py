from tkinter import *

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.60934
    kilometer_result_label.config(text=f"{km:.2f}")

window = Tk()
window.title("Miles to Kilometers")
window.configure(background="white")
window.resizable(width=False, height=False)

miles_input = Entry(width=10)
# Girdi kutusunu ekranda konumlandırmak için:
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="Is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

km_label = Label(text="Kilometers")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()