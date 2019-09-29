
import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library (id INTEGER PRIMARYKEY,ISBN integer,author text,title text)")
    conn.commit()
    conn.close()


def insert(id,ISBN,author,title):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO library VALUES (?,?,?,?)",(id,ISBN,author,title))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM library")
    rows = cur.fetchall()
    return rows


def search(ISBN="",author="",title=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library WHERE ISBN=? OR author=? OR title=? ",(ISBN,author,title))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(ISBN,author,title,id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE library SET ISBN=?,author=?,title=? WHERE id=?",(ISBN,author,title,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?", (id,))
    conn.commit()
    conn.close()

connect()
#insert(152345,"pramod2","wisdomQ")
#update(78,"babu","golmal",7)
delete(491)
print(view())