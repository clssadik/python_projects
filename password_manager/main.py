from tkinter import Entry
from tkinter import Label
from tkinter import * 



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

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

email_username_data = Entry(width=35,background="white",fg="black")
email_username_data.grid(row=2,column=1,columnspan=2)

password_data = Entry(width=20,background="white",fg="black")
password_data.grid(row=3,column=1)

generate = Button(text="Generate Password",background="white",width=11)
generate.grid(row=3,column=2)

add = Button(width=33, text="Add")
add.grid(row=4,column=1,columnspan=2)



window.mainloop()