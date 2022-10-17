import psycopg2
from tkinter import *
import sys

root = Tk()
root.geometry('400x200')

con = psycopg2.connect(
    host="localhost",
    database="ahd",
    user="ahd",
    password="hesthest")

cur = con.cursor()

def register():
    username = entry1.get()
    password = entry2.get()

    cur.execute('INSERT INTO "user" (username, password) VALUES ({0}, {1});'.format("'" + username + "'", "'" + password + "'"))
    con.commit()
    print("Done")

def login():
    username = entry3.get()
    password = entry4.get()


    cur.execute('SELECT COUNT(id) FROM "user" WHERE username = {0} AND password = {1};'.format("'" + username + "'", "'" + password + "'"))
    rows = cur.fetchall()

    if rows == [(1,)]:
        print("logged in")
    else:
        print("Incorrect credentials!")
        print(rows)


entry1 = Entry(root, width=20)
entry1.pack()

entry2 = Entry(root, width=20)
entry2.pack()

Button(root, text="Register", command=register).pack()

entry3 = Entry(root, width=20)
entry3.pack()

entry4 = Entry(root, width=20)
entry4.pack()

Button(root, text="Login", command=login).pack()


root.mainloop()

cur.execute('SELECT * FROM "user"')

rows = cur.fetchall()

for r in rows:
    print(f"id: {r[0]} username: {r[1]} password: {r[2]}")

cur.close()
con.close()
