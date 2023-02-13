BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

import pandas as pd

import random

current_card = {} 
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_image,image=my_image_front)
    flip_timer = window.after(3000, func = flip_card)
    

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_image, image=my_image_back)
    
def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)




canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


my_image_front = PhotoImage(file="images/card_front.png")#path/to/image_file.png")
my_image_back = PhotoImage(file="images/card_back.png")

canvas_image=canvas.create_image(400,263,image=my_image_front)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))






my_image_right = PhotoImage(file="images/right.png")#path/to/image_file.png")
right_button = Button(image=my_image_right, highlightthickness=0,bg=BACKGROUND_COLOR,command=is_known)
right_button.grid(row=1,column=0)

my_image_wrong = PhotoImage(file="images/wrong.png")#path/to/image_file.png")
wrong_button = Button(image=my_image_wrong, highlightthickness=0,bg=BACKGROUND_COLOR,command=next_card)
wrong_button.grid(row=1,column=1)


next_card()


"""
1. When the user presses on the ✅ button, it means that they know the current word on the flashcard and that word should be removed from the list of words that might come up.

e.g. If french_words.csv had only 3 records:

chaque,each
parlé,speak
arrivé,come
After the user has seen parlé,speak  it should be removed from the list of words that can come up again.

2. The updated data should be saved to a new file called words_to_learn.csv

e.g. words_to_learn.csv

chaque,each
arrivé,come
3. The next time the program is run, it should check if there is a words_to_learn.csv file. If it exists, the program should use those words to put on the flashcards. If the words_to_learn.csv does not exist (i.e., the first time the program is run), then it should use the words in the french_words.csv

We want our flashcard program to only test us on things we don't know. So if the user presses the ✅ button, that means the current card should not come up again.

e.g.


HINTS:

1. The remove() method can remove elements from a list. e.g. https://www.w3schools.com/python/ref_list_remove.asp

2. You can create a new csv file from a dictionary using DataFrame.to_csv() e.g. https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html

3. If you don't want to create an index for the new csv, you can set the index parameter to False. e.g.

data.to_csv("filename.csv", index=False)

"""
window.mainloop()

