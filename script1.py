from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=lst1.curselection()[0]
        selected_tuple=lst1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])

        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])

        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])

        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass
    

def view_command():
    lst1.delete(0,END)
    for row in backend.view():
        lst1.insert(END, row)

def search_command():
    lst1.delete(0,END)
    for row in backend.search(tittle_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        lst1.insert(END, row)

def add_command():
    backend.insert(tittle_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    lst1.delete(0, END)
    lst1.insert(END, (tittle_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0], tittle_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    print(backend.update(selected_tuple[0], tittle_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
window = Tk()

l1 = Label(window, text ="Tittle")
l1.grid(row= 0, column= 0)

l2 = Label(window, text ="Author")
l2.grid(row= 0, column= 2)

l3 = Label(window, text ="Year")
l3.grid(row= 1, column= 0)

l4 = Label(window, text ="ISBN")
l4.grid(row= 1, column= 2)

tittle_text = StringVar()
e1 = Entry(window, textvariable = tittle_text)
e1.grid(row= 0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable = author_text)
e2.grid(row= 0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable = year_text)
e3.grid(row= 1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable = isbn_text)
e4.grid(row= 1, column=3)

lst1 = Listbox(window,height = 6, width = 32)
lst1.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)

sb1= Scrollbar(window)
sb1.grid(row=2, column=2, rowspan = 6)

lst1.configure(yscrollcommand=sb1.set)
sb1.configure(command= lst1.yview)

lst1.bind('<<ListboxSelect>>', get_selected_row)


b1 = Button(window, text = "View All", width = 12, command = view_command)
b1.grid(row=2, column= 3)

b2 = Button(window, text = "Search Entry", width = 12, command = search_command)
b2.grid(row=3, column= 3)

b3 = Button(window, text = "Add Entry", width = 12, command = add_command)
b3.grid(row=4, column= 3)

b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row=5, column= 3)

b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row=6, column= 3)

b6 = Button(window, text = "Close", width = 12, command = window.destroy)
b6.grid(row=7, column= 3)

window.mainloop()