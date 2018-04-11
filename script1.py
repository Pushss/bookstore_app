from tkinter import * #import all from tkinter libery. allows use of b1.Button() instead of b1.tkinter.Button()

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
e1_value=StringVar() #declare string variable to store Entry() data
e1=Entry(window, textvariable=e1_value) #entry widget (editText)(textvariable = e1_value)
e1.grid(row=0,column=1) #postions entry widget on grid

e2_value=StringVar()
e2=Entry(window, textvariable=e2_value)
e2.grid(row=0,column=3)

e3_value=StringVar()
e3=Entry(window, textvariable=e3_value)
e3.grid(row=1,column=1)

e4_value=StringVar()
e4=Entry(window, textvariable=e4_value)
e4.grid(row=1,column=3) 


window.mainloop() #allows window to remain open permentaly keep this at end of code
