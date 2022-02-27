from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json


# ------------------------------Search an entry -----------------------------------#
def search_password():
    if len(web_entry.get()) == 0:
        messagebox.showerror(title="Invalid Website", message="Enter a website to search!!!")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="No Entry Found", message="No websites saved yet!!")
        else:
            try:
                web_data = data[web_entry.get()]
            except KeyError:
                messagebox.showinfo(title="No Entry Found", message=f"Details for website {web_entry.get()}"
                                                                    f" not saved yet!!")
            else:
                email = web_data["email"]
                password = web_data["password"]
                messagebox.showinfo(title=f"Details for {web_entry.get()}", message=f"\nEmail: {email} \n"
                                                                                    f"Password: {password}\n")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
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
    else:
        # messagebox.askokcancel(title=f"Confirm details for {website}", message=f"These are the details:"
        #                                                                         f" \nEmail: {email} \n"
        #                                                                         f"Password: {password}\n"
        #                                                                         f"Press OK to save."):
        data_dict = {website: {
            "email": email,
            "password": password
        }}
        try:
            with open("data.json", "r") as data_file:
                old_data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data_dict, data_file, indent=4)
        else:
            old_data.update(data_dict)
            with open("data.json", "w") as data_file:
                json.dump(old_data, data_file, indent=4)
        finally:
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

web_entry = Entry(width=18)
web_entry.grid(column=1, row=1)
web_entry.focus()

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "rranga99@gmail.com")

pass_entry = Entry(width=18)
pass_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search_password, width=13)
search_button.grid(column=2, row=1)

pass_button = Button(text="Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
