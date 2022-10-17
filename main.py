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
    username = entry1.get()
    password = entry2.get()

    try:
        cur.execute('IF EXISTS (SELECT * FROM "user" WHERE username = {} and password = {});'.format("'" + username + "'", "'" + password + "'"))
        succesful = True
    except:
        print("Invalid credentials!")
        sys.exit()
    if succesful:
        print("logged in")

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
