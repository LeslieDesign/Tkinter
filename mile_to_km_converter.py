from tkinter import *


def button_clicked():
    miles = float(input_miles.get())
    km = miles * 1.6
    kilometers.config(text=km)


window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)

#Label
instructions_label = Label(text="Enter the miles:", font=("Arial", 13, "bold"))
instructions_label.grid(column=1, row=0)

#Row 1:
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=1, sticky="w")
#miles_label.config(padx=5, pady=20)

input_miles = Entry(width=20)
print(input_miles.get())
input_miles.grid(column=1, row=1)

#Row 2:
is_equal_to = Label(text="Is equal to:", font=("Arial", 12))
is_equal_to.grid(column=0, row=2, sticky="e")
kilometers = Label(text=" ", font=("Arial", 12, "bold"))
kilometers.grid(column=1, row=2)
km_label = Label(text="Kilometers", font=("Arial", 12))
km_label.grid(column=2, row=2)

#Row 3:
#Button
button = Button(text="Calculate",
                font=("Arial", 12, "bold"),
                bg="green",
                fg="white",
                activebackground="black",
                activeforeground="white",
                command=button_clicked)
button.grid(column=1, row=4)
button.config(padx=10, pady=2)











window.mainloop()
