import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}


def translate_card(french_word):
    canvas.itemconfig(canvas_image, image=back_photo)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=french_word["English"], fill="white")


def next_card():
    global selected_word

    selected_word = random.choice(french_list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=selected_word["French"], fill="black")
    run_timer(3)


def run_timer(count):
    global selected_word
    if count > 0:
        window.after(1000, run_timer, count - 1)
    else:
        translate_card(selected_word)


def learnt_card():
    french_list.remove(selected_word)
    df = pandas.DataFrame(french_list)
    print("Creating file....")
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, highlightthickness=0)
front_photo = PhotoImage(file="./images/card_front.png")
back_photo = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_photo)
canvas.config(bg=BACKGROUND_COLOR)
title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

photo_w = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=photo_w, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

photo_r = PhotoImage(file="images/right.png")
right_button = Button(image=photo_r, highlightthickness=0, command=learnt_card)
right_button.grid(column=1, row=1)

# ===========================Pick french words from file================================#
try:
    file_data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    file_data = pandas.read_csv("./data/french_words.csv")
finally:
    french_list = file_data.to_dict(orient="records")
# Show the first card
next_card()
run_timer(3)

window.mainloop()
