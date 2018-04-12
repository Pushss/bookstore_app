from tkinter import * #import all from tkinter libery. allows use of b1.Button() instead of b1.tkinter.Button()
from backend import Database #import db to use functions like db.update()

db=Database("books.db")

class Window(object):
    def __init__(self,window):
        self.window = window #Creates window

        self.window.wm_title("BookStore") #sets window title

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
        self.title_text=StringVar() #declare string variable to store Entry() data
        self.e1=Entry(window, textvariable=self.title_text) #entry widget (editText)(textvariable = title_text)
        self.e1.grid(row=0,column=1) #postions entry widget on grid

        self.author_text=StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text=StringVar()
        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        #Listbox window to display data
        self.list1=Listbox(window,height=6,width=35) #Listbox widget
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2) #postions text widget on grid

        #Creating scrollbar indepent from listbox but will link sb1 to list1
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        #link sb1 to list1
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        #Group of Button() b1 to b6
        #create button (places in window, text="String",command=call's)
        b1=Button(window, text="View all",width=12, command=self.view_command)
        #places the button on the window can define postion with .grid() or .pack()
        #.grid(grid can have row=0, column=0 for easier placement, rowspan=number
        b1.grid(row=2,column=3)

        b2=Button(window, text="Search Entry",width=12,command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window, text="Add Entry",width=12,command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window, text="Update",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window, text="Delete",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window, text="Close",width=12,command=window.destroy)
        b6.grid(row=7,column=3)

        window.mainloop() #allows window to remain open permentaly keep this at end of code

    def get_selected_row(self,event): #finds index of selected item in Listbox
        try:
            index=self.list1.curselection()[0] #finds index of tuple
            self.selected_tuple=self.list1.get(index) #stores selected list item
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in db.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in db.search_entry(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()):
            self.list1.insert(END,row)

    def add_command(self):
        db.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get()))

    def update_command(self):
        db.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        self.view_command()

    def delete_command(self):
        db.delete(self.selected_tuple[0])
        self.view_command()

window=Tk()
Window(window)
window.mainloop()
