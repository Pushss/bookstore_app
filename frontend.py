from tkinter import * #import all from tkinter libery. allows use of b1.Button() instead of b1.tkinter.Button()
import backend #import backend to use functions like backend.update()

def get_selected_row(event): #finds index of selected item in Listbox
    global selected_tuple
    index=list1.curselection()[0] #finds index of tuple
    selected_tuple=list1.get(index) #stores selected list item
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search_entry(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),int(year_text.get()),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    view_command()

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

window=Tk() #create window

window.wm_title("BookStore") #set window title

#Group of Label() l1 to l4 postioned with grid(location placed with param's)
l1=Label(window, text="Title: ") #Label (call to window, display text "Title:")
l1.grid(row=0,column=0) #postions Label widget on grid

l2=Label(window, text="Author: ")
l2.grid(row=0,column=2)

l3=Label(window, text="Year: ")
l3.grid(row=1,column=0)

l4=Label(window, text="ISBN: ")
l4.grid(row=1,column=2)

#Group of Entry() e1 to e4 postioned with grid(location placed with param's)
title_text=StringVar() #declare string variable to store Entry() data
e1=Entry(window, textvariable=title_text) #entry widget (editText)(textvariable = title_text)
e1.grid(row=0,column=1) #postions entry widget on grid

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1,column=3)

#Listbox window to display data
list1=Listbox(window,height=6,width=35) #Listbox widget
list1.grid(row=2,column=0,rowspan=6,columnspan=2) #postions text widget on grid

#Creating scrollbar indepent from listbox but will link sb1 to list1
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#link sb1 to list1
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

#Group of Button() b1 to b6
#create button (places in window, text="String",command=call's)
b1=Button(window, text="View all",width=12, command=view_command)
#places the button on the window can define postion with .grid() or .pack()
#.grid(grid can have row=0, column=0 for easier placement, rowspan=number
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window, text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window, text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop() #allows window to remain open permentaly keep this at end of code
