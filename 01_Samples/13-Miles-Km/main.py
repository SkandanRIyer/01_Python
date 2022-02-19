from tkinter import *

window = Tk()
window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)


def calculate_km():
    km = round(float(v_text.get()) * 1.609, 2)
    l_km_val.config(text=f"{km}")


def close():
    window.destroy()


# create the labels
l_miles = Label(text="Miles")
l_miles.grid(column=2, row=0)

l_equals = Label(text="is equal to")
l_equals.grid(column=0, row=1)

l_km = Label(text="Km")
l_km.grid(column=2, row=1)

l_km_val = Label(text="0")
l_km_val.grid(column=1, row=1)

# create the text box
v_text = Entry(width=5)
v_text.insert(END, string="0")
v_text.grid(column=1, row=0)

# create the button
c_button = Button(text="Calculate", command=calculate_km)
c_button.grid(column=1, row=2)
c_button.config(padx=2, pady=2)

# close button
close_button = Button(text="Cancel", command=close)
close_button.grid(column=2, row=2)
close_button.config(padx=2, pady=2)





window.mainloop()