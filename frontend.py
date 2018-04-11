from tkinter import * #import all from tkinter libery. allows use of b1.Button() instead of b1.tkinter.Button()
import backend #import backend to use functions like backend.update()

window=Tk() #create window

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

#Group of Button() b1 to b6
#create button (places in window, text="String",command=call's)
b1=Button(window, text="View all",width=12) #command=backend.view_all)
#places the button on the window can define postion with .grid() or .pack()
#.grid(grid can have row=0, column=0 for easier placement, rowspan=number
b1.grid(row=2,column=3)

b2=Button(window, text="Search Entry",width=12) #,command=backend.search_entry)
b2.grid(row=3,column=3)

b3=Button(window, text="Add Entry",width=12) #,command=backend.add_entry)
b3.grid(row=4,column=3)

b4=Button(window, text="Update",width=12) #,command=backend.update)
b4.grid(row=5,column=3)

b5=Button(window, text="Delete",width=12) #,command=backend.delete)
b5.grid(row=6,column=3)

b6=Button(window, text="Close",width=12) #,command=backend.close)
b6.grid(row=7,column=3)

window.mainloop() #allows window to remain open permentaly keep this at end of code
