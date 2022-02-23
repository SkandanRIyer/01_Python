import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps

    reps = 0
    window.after_cancel(timer)
    ti_labels.config(text="")
    t_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        t_label.config(text="Break", fg=RED)
        run_timer(long_break_sec)
    elif reps % 2 == 0:
        t_label.config(text="Break", fg=PINK)
        run_timer(short_break_sec)
    else:
        t_label.config(text="Work", fg=GREEN)
        run_timer(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def run_timer(count):
    global reps, timer

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, run_timer, count - 1)
    else:
        start_timer()
        ticks = ""
        if reps % 2 == 0:
            for _ in range(math.floor(reps / 2)):
                ticks += "✔"
            ti_labels.config(text=ticks, fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

t_label = Label()
t_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
t_label.grid(column=1, row=0)

b_start = Button(text="Start", highlightthickness=0, command=start_timer)
b_start.grid(column=0, row=2)

b_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
b_reset.grid(column=2, row=2)

ti_labels = Label()
ti_labels.grid(column=1, row=3)

window.mainloop()
