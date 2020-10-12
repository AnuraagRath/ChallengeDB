from tkinter import *
import sqlite3

root = Tk()
root.title("db")

conn = sqlite3.connect("student.db")

c = conn.cursor()

c.execute("""CREATE TABLE daVinciDemons (
		first_name text,
		last_name text,
		categoryType text,
		projectTitle text,
		totalDays text,
		progressDays integer
        )""")


conn.commit()

conn.close()

root.mainloop()
