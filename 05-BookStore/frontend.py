from tkinter import *
import backend as db

window = Tk()
window.title("Book Store")
window.resizable(True, False) 

def set_selected_row(event):
    if book_list.curselection():
        global selected_tuple
        index = book_list.curselection()[0]
        selected_tuple = book_list.get(index)

        title_enter.delete(0, END)
        title_enter.insert(END, selected_tuple[1])

        author_enter.delete(0, END)
        author_enter.insert(END,selected_tuple[2])

        publish_enter.delete(0, END)
        publish_enter.insert(END, selected_tuple[3])

        isbn_enter.delete(0, END)
        isbn_enter.insert(END,selected_tuple[4])

def view_command():
    book_list.delete(0, END)
    for row in db.view():
        book_list.insert(END, row)

def search_command():
    book_list.delete(0, END)
    for row in db.search(title_text.get(), 
                         author_text.get(), 
                         publish_text.get(), 
                         isbn_text.get()
    ):
        book_list.insert(END, row)

def add_command():
    db.insert(title_text.get(), 
              author_text.get(), 
              publish_text.get(), 
              isbn_text.get()
    )
    book_list.delete(0, END)
    book_list.insert(END, 
              title_text.get(), 
              author_text.get(), 
              publish_text.get(), 
              isbn_text.get()
    )
    
def update_command():
    db.update(
        selected_tuple[0], 
        title_text.get(), 
        author_text.get(), 
        publish_text.get(), 
        isbn_text.get()
    )
    view_command()

def delete_command():
    db.delete(selected_tuple[0])
    view_command()

def close_command():
    book_list.delete(0, END)
    for row in db.search(title_text.get(), 
                         author_text.get(), 
                         publish_text.get(), 
                         isbn_text.get()
    ):
        book_list.insert(END, row)

# Main frame
frame = Frame(window, padx=20, pady=20)
frame.grid(row=0, column=0, sticky="nsew")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Column weight in frame
frame.grid_columnconfigure(1, weight=1)  
frame.grid_columnconfigure(2, weight=0)  
frame.grid_columnconfigure(3, weight=0)  
frame.grid_columnconfigure(4, weight=0)

# Title
title_label = Label(frame, text="Title")
title_label.grid(row=0, column=0, padx=10, pady=5)

title_text = StringVar()
title_enter = Entry(frame, textvariable=title_text)
title_enter.grid(row=1, column=0, padx=10, pady=5)

# Author
author_label = Label(frame, text="Author")
author_label.grid(row=2, column=0, padx=10, pady=5)

author_text = StringVar()
author_enter = Entry(frame, textvariable=author_text)
author_enter.grid(row=3, column=0, padx=10, pady=5)

# Publish date
publish_label = Label(frame, text="Published")
publish_label.grid(row=4, column=0, padx=10, pady=5)

publish_text = StringVar()
publish_enter = Entry(frame, textvariable=publish_text)
publish_enter.grid(row=5, column=0, padx=10, pady=5)

# ISBN
isbn_label = Label(frame, text="ISBN")
isbn_label.grid(row=6, column=0, padx=10, pady=5)

isbn_text = StringVar()
isbn_enter = Entry(frame, textvariable=isbn_text)
isbn_enter.grid(row=7, column=0, padx=10, pady=5)

# Configurar el Listbox y Scrollbar para expandirse
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Book list
book_list = Listbox(frame, height=6, width=60)
book_list.grid(row=0, column=1, rowspan=8, columnspan=2, padx=10, pady=5, sticky="nsew")

scroll = Scrollbar(frame)
scroll.grid(row=0, column=3, rowspan=8, sticky="ns")
book_list.configure(yscrollcommand=scroll.set)
scroll.configure(command=book_list.yview)

book_list.bind('<<ListboxSelect>>', set_selected_row)

# View all button
view_all = Button(frame, text="View all", width=12, command=view_command)
view_all.grid(row=0, column=4, padx=10, pady=5)

# Search button
search = Button(frame, text="Search", width=12, command=search_command)
search.grid(row=1, column=4, padx=10, pady=5)

# Add button
add = Button(frame, text="Add item", width=12, command=add_command)
add.grid(row=2, column=4, padx=10, pady=5)

# Update button
update = Button(frame, text="Update selected", width=12, command=update_command)
update.grid(row=3, column=4, padx=10, pady=5)

# Delete button
delete = Button(frame, text="Delete selected", width=12, command=delete_command)
delete.grid(row=4, column=4, padx=10, pady=5)

# Close button
close = Button(frame, text="Close", width=12, command=close_command)
close.grid(row=5, column=4, padx=10, pady=5)

view_command()

window.mainloop()