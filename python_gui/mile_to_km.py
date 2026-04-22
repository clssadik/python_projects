from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def button_clicked():
    miles = round(float(input.get()),2)
    result.config(text=round(miles*1.609344))

input = Entry(width=7, background="white", fg="black")
input.grid(row=0, column=1)

text = Label(text="Miles")
text.grid(row=0, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

result = Label(text = 0)
result.grid(row=1, column=1)

text2 = Label(text="Km")
text2.grid(row=1, column=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)




























window.mainloop()