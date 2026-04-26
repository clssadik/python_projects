import pyperclip
from tkinter import Entry
from tkinter import Label
from tkinter import * 
from tkinter import messagebox
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # new_list = [n for n in list]

    password_letter = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)

    password_data.delete(0,END)
    password_data.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_data.get()
    email = email_username_data.get()
    password = password_data.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Warning",message="Please fill in the required fields!")

    else:  
        is_okay = messagebox.askokcancel(title=website,message=f"Email : {email}\nPassword : {password}\nWould you like to save it?")
        if is_okay:
            with open("password_manager.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")

    website_data.delete(0,END)
    password_data.delete(0,END)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_data = Entry(width=35,background="white",fg="black")
website_data.grid(row=1,column=1,columnspan=2)
website_data.focus()

email_username_data = Entry(width=35,background="white",fg="black")
email_username_data.insert(0,"cillsadik@gmail.com")
email_username_data.grid(row=2,column=1,columnspan=2)

password_data = Entry(width=20,background="white",fg="black")
password_data.grid(row=3,column=1)

generate = Button(text="Generate Password",background="white",width=11,command=password_generator)
generate.grid(row=3,column=2)

add = Button(width=33, text="Add",command=save_data)
add.grid(row=4,column=1,columnspan=2)



window.mainloop()