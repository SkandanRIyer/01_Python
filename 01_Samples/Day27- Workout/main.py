from tkinter import *

window = Tk()
window.title("This is so cool using Python!!!")
window.minsize(width=600, height=600)

# label
cool_label = Label(text="I am a cool guy!!!", font=("Arial", 24, "italic"))
# cool_label.pack()
cool_label.config(text="I am a cool boy!!!")
# Enter the layout manager grid
cool_label.config(padx=50, pady=20)
cool_label.grid(column=0, row=0)


# button

def button_clicked():
    # cool_label.config(text="Woho...I am clicked....")
    cool_label.config(text=(wonder_input.get()))


awesome_button = Button(text="Calculate", command=button_clicked)
# awesome_button.pack()
# Enter the layout manager grid
awesome_button.grid(column=1, row=1)

# new button
super_button = Button(text="Racer", command=button_clicked)
# awesome_button.pack()
# Enter the layout manager grid
super_button.grid(column=2, row=0)
# Entry
wonder_input = Entry(width=20)
# wonder_input.pack()
# Enter the layout manager grid
wonder_input.grid(column=3, row=3)

# text
chill_text = Text(height=5, width=30)
chill_text.focus()
chill_text.insert(END, "Write your own history and be what you want to be>>>>>......>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                       ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(chill_text.get("1.0", "2.0"))
# # the new layout manager "place"
# chill_text.place(x=100, y=400)
# Enter the layout manager grid
# chill_text.grid(column=3, row=3)



window.mainloop()
