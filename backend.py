import sqlite3

class Database:
    def __init__(self, db): #executed at application launch
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor() #create cursor within db
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT,title text,author text,year integer,isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()
        self.view()

    def view(self):
        self.cur.execute("SELECT * FROM book") #select all data from TABLE book
        rows=self.cur.fetchall()
        return rows

    def search_entry(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn =?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self): #executed at app close
        self.conn.close() #closes connection to DB

#insert("the Search","john snow",1998,342342)
#insert("the earth","william wallace",1992,234232)
#insert("the spirit","henrik larsson",2010,342342)
#print(search_entry(year='3342'))
