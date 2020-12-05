from tkinter import *
window = Tk()
window.title("Sample Tkinter Application")

lbl = Label(window, text="This is created using Python - Tkinter", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

window.mainloop()