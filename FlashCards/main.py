import stat
from tkinter import *
from tkinter import ttk
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

data_file = pandas.read_csv("data/french_words.csv")
cards = data_file.to_dict(orient="records")
current_card = random.choice(cards)

def reverse_card():
    global current_card
    current_card = random.choice(cards)
    canvas.itemconfig(title_id,text="French",fill="black")
    canvas.itemconfig(word_id, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image,image=front)
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    window.after(3000,flip_card)
    

def right_clicked():
    try:
        with open("data/known_words.json","r") as kelime:
            data = json.load(kelime)
            data.append(current_card)
        
    except FileNotFoundError:
        with open("data/known_words.json","w") as kelime:
            json.dump([current_card],kelime,indent=4)

    else:
        with open("data/known_words.json","w") as kelime:
            json.dump(data,kelime,indent=4)
    
    reverse_card()

def flip_card():
    canvas.itemconfig(word_id, text=current_card["English"], fill="white")
    canvas.itemconfig(title_id, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=back)
    button1.config(state=NORMAL)
    button2.config(state=NORMAL)

def listeyi_getir():
    list_window = Toplevel()
    list_window.title("Known Words")
    list_window.geometry("500x350")
    list_window.resizable(False, False)
    
    button3.config(state=DISABLED)

    style = ttk.Style()
    style.theme_use("default")
    
    style.configure("Treeview",background=BACKGROUND_COLOR,foreground="white",rowheight=30,fieldbackground=BACKGROUND_COLOR)
    style.configure("Treeview.Heading", background="white", font=('Arial', 10, 'bold'),foreground="black")

    columns = ("French", "English")
    tablo = ttk.Treeview(list_window, columns=columns, show="headings")

    tablo.heading("French", text="French")
    tablo.heading("English", text="English")

    tablo.column("French", width=150, anchor=CENTER)
    tablo.column("English", width=150, anchor=CENTER)

    scrollbar = ttk.Scrollbar(list_window, orient=VERTICAL, command=tablo.yview)
    tablo.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    tablo.pack(expand=True, fill="both")

    try:
        with open("data/known_words.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            
            for kelime in data:
                tablo.insert("", END, values=(kelime["French"], kelime["English"]))
                
    except FileNotFoundError:
        print("Henüz bilinen kelime dosyası oluşturulmamış.")

    def close_window():
        button3.config(state=NORMAL)
        list_window.destroy()

    list_window.protocol("WM_DELETE_WINDOW", close_window)


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)
window.after(3000,flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0,bg=BACKGROUND_COLOR)
front = PhotoImage(file=("images/card_front.png"))
back = PhotoImage(file=("images/card_back.png"))
canvas_image = canvas.create_image(400,263,image=front)
canvas.grid(row=0,column=0,columnspan=2)

title_id = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_id = canvas.create_text(400, 263, text=current_card["French"], font=("Ariel", 60, "bold"), fill="black")

wrong_image = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_image, highlightthickness=0,borderwidth=0,relief="flat",command=reverse_card,state=DISABLED)
button1.grid(row=1,column=0)

right_image = PhotoImage(file="images/right.png")
button2 = Button(image=right_image,highlightthickness=0,borderwidth=0,relief="flat",command=right_clicked,state=DISABLED)
button2.grid(row=1,column=1)

button3 = Button(text="Known Words",highlightthickness=0,background=BACKGROUND_COLOR,width=20,borderwidth=0,relief="flat",activebackground=BACKGROUND_COLOR,highlightbackground=BACKGROUND_COLOR,command=listeyi_getir,state=NORMAL)
button3.grid(row=2,column=0,columnspan=2)

window.mainloop()

