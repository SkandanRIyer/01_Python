from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(pass_entry.get())


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    if len(email) == 0:
        messagebox.showerror(title="Error!!!", message=f"Email is empty!")
    elif len(website) == 0:
        messagebox.showerror(title="Error!!!", message=f"Website is empty!")
    elif len(password) == 0:
        messagebox.showerror(title="Error!!!", message=f"Password is empty!")
    elif messagebox.askokcancel(title=f"Confirm details for {website}", message=f"These are the details:"
                                                                                f" \nEmail: {email} \n"
                                                                                f"Password: {password}\n"
                                                                                f"Press OK to save."):
        with open("data.txt", "a") as data:
            data.write(f"{website} | {email} | {password}\n")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)
        web_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

l_website = Label(text="Website")
l_website.grid(column=0, row=1)

l_email = Label(text="Email/Username")
l_email.grid(column=0, row=2)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3)

web_entry = Entry(width=36)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "rranga99@gmail.com")

pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
