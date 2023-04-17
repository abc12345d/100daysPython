from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
SOURCE_LANGUAGE = 'French'
TARGET_LANGUAGE = 'English'
current_word_pair = None

# --------------- file handling----------------------#
try:
    data_file = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_file = pd.read_csv("./data/french_words.csv")
finally:
    data_file = data_file.to_dict('records')

# --------------- flip the flash card ---------------#
def flip():
    global current_word_pair

    canvas.itemconfig(canvas_image,image = back_image)
    canvas.itemconfig(language_text, text = TARGET_LANGUAGE,fill = 'white')
    canvas.itemconfig(word_text, text = current_word_pair[TARGET_LANGUAGE],fill = 'white')

# --------------- reset source text ------------#
def get_random_source_word():
    global current_word_pair, flip_timer

    window.after_cancel(flip_timer)
    current_word_pair = random.choice(data_file)
    flip_timer = window.after(3000,func= flip)
    return current_word_pair[SOURCE_LANGUAGE]

def reset_source_text():
    canvas.itemconfig(canvas_image,image = front_image)
    canvas.itemconfig(language_text, text = SOURCE_LANGUAGE,fill='black')
    canvas.itemconfig(word_text, text = get_random_source_word(),fill='black')

# --------------- remove word from words to learn ----------------#
def remove_word_pair():
    data_file.remove(current_word_pair)
    pd.DataFrame(data_file).to_csv('./data/words_to_learn.csv',index=False)

    reset_source_text()

# --------------- UI ----------------#
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800,height=526,highlightthickness=0,background=BACKGROUND_COLOR)
front_image = PhotoImage(file= './images/card_front.png')
back_image = PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400,263,image = front_image)
language_text = canvas.create_text(400,150,text=SOURCE_LANGUAGE,font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263,text=get_random_source_word(),font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

wrong_image = PhotoImage(file= './images/wrong.png')
wrong_button = Button(image= wrong_image,command = reset_source_text,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file= './images/right.png')
right_button = Button(image=right_image,command = remove_word_pair,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,highlightcolor=BACKGROUND_COLOR)
right_button.grid(row=1,column=1)

window.mainloop()
