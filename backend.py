import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor() #create cursor within db
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book") #select all data from TABLE book
    rows=cur.fetchall()
    conn.close()
    return rows


#("UPDATE book SET title=?, author=?, year=?, WHERE ISBN =?",(title,author,year,isbn))

connect()
insert("the sea", "john tablet", 3342,32323)
print(view())
