from tkinter import *

window = Tk()

button1 = Button(window, text="Execute")
button1.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=0, column=1)

text = Text(window, height=1, width=20)
text.grid(row=0, column=2)

text.insert("1.0", "Texto de ejemplo")

window.mainloop()