import tkinter

window = tkinter.Tk()
window.title("Python GUI")
window.minsize(500, 300)

my_label = tkinter.Label(text="Hello World", font=("Times", 25, "italic"))
my_label.pack(expand=True)














window.mainloop()