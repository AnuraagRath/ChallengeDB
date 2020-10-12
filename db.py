from tkinter import *
import sqlite3


root = Tk()
root.title('RathBase')
root.geometry("430x550")
#root.configure(bg="skyblue")
#scrollbar = Scrollbar(root)
#scrollbar.grid(side=RIGHT, fill=Y)



tatl = Label(root, text="RathBASE_3.0", fg="purple", bg="yellow")
tatl.grid(row=0,column=0)

ttal = Label(root, text="ChallengeBase", fg="red", bg="light green")
ttal.grid(row=0,column=1)
# Databases

# Create a database or connect to one
conn = sqlite3.connect('daVinci_book.db')

# Create cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE daVinciDemons (
		first_name text,
		last_name text,
		categoryType text,
		projectTitle text,
		totalDays text,
		progressDays integer
		)""")
'''
# Create Update function to update a record
def update():
	# Create a database or connect to one
	conn = sqlite3.connect('student.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()

	c.execute("""UPDATE daVinciDemons SET
		first_name = :first,
		last_name = :last,
		categoryType = :categoryType,
		projectTitle = :projectTitle,
		totalDays = :totalDays,
		progressDays = :progressDays 

		WHERE oid = :oid""",
		{
		'first': f_name_editor.get(),
		'last': l_name_editor.get(),
		'categoryType': categoryType_editor.get(),
		'projectTitle': projectTitle_editor.get(),
		'totalDays': totalDays_editor.get(),
		'progressDays': progressDays_editor.get(),
		'oid': record_id
		})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	editor.destroy()
	root.deiconify()

# Create Edit function to update a record
def edit():
	root.withdraw
	global editor
	editor = Tk()
	editor.title('Update A Record')
	editor.geometry("420x320")
	# Create a database or connect to one
	conn = sqlite3.connect('student.db')
	# Create cursor
	c = conn.cursor()

	record_id = delete_box.get()
	# Query the database
	c.execute("SELECT * FROM daVinciDemons WHERE oid = " + record_id)
	records = c.fetchall()
	
	#Create Global Variables for text box names
	global f_name_editor
	global l_name_editor
	global categoryType_editor
	global projectTitle_editor
	global totalDays_editor
	global progressDays_editor

	# Create Text Boxes
	f_name_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	f_name_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
	l_name_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	l_name_editor.grid(row=2, column=1)
	categoryType_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	categoryType_editor.grid(row=3, column=1)
	projectTitle_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	projectTitle_editor.grid(row=4, column=1)
	totalDays_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	totalDays_editor.grid(row=5, column=1)
	progressDays_editor = Entry(editor, width=30, fg="yellow", bg="purple", borderwidth=10)
	progressDays_editor.grid(row=6, column=1)
	
	# Create Text Box Labels
	f_name_label = Label(editor, text="First Name", fg="red", borderwidth=10)
	f_name_label.grid(row=1, column=0, pady=(10, 0))
	l_name_label = Label(editor, text="Last Name", fg="red", borderwidth=10)
	l_name_label.grid(row=2, column=0)
	categoryType_label = Label(editor, text="categoryType", fg="red", borderwidth=10)
	categoryType_label.grid(row=3, column=0)
	projectTitle_label = Label(editor, text="projectTitle", fg="red", borderwidth=10)
	projectTitle_label.grid(row=4, column=0)
	totalDays_label = Label(editor, text="totalDays", fg="red", borderwidth=10)
	totalDays_label.grid(row=5, column=0)
	progressDays_label = Label(editor, text="progressDays", fg="red", borderwidth=10)
	progressDays_label.grid(row=6, column=0)

	# Loop thru results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		categoryType_editor.insert(0, record[2])
		projectTitle_editor.insert(0, record[3])
		totalDays_editor.insert(0, record[4])
		progressDays_editor.insert(0, record[5])

	
	# Create a Save Button To Save edited record
	edit_btn = Button(editor, text="Save Record", command=update, fg="blue", bg="violet")
	edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

	


# Create Function to Delete A Record
def delete():
	# Create a database or connect to one
	conn = sqlite3.connect('student.db')
	# Create cursor
	c = conn.cursor()

	# Delete a record
	c.execute("DELETE from daVinciDemons WHERE oid = " + delete_box.get())

	delete_box.delete(0, END)
	

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()



# Create Submit Function For database
def submit():
	# Create a database or connect to one
	conn = sqlite3.connect('student.db')
	# Create cursor
	c = conn.cursor()

	# Insert Into Table
	c.execute("INSERT INTO daVinciDemons VALUES (:f_name, :l_name, :categoryType, :projectTitle, :totalDays, :progressDays)",
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'categoryType': categoryType.get(),
				'projectTitle': projectTitle.get(),
				'totalDays': totalDays.get(),
				'progressDays': progressDays.get()
			})


	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

	# Clear The Text Boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	categoryType.delete(0, END)
	projectTitle.delete(0, END)
	totalDays.delete(0, END)
	progressDays.delete(0, END)

# Create Query Function
def query():
	# Create a database or connect to one
	conn = sqlite3.connect('student.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT  oid, * FROM daVinciDemons")
	records = c.fetchall()
	
	
	recordsWindow = Toplevel(root)
	recordsWindow.title('RECORDS')
	recordsWindow.config(background = 'red')

	
	# print(records)
	# Loop Thru Results
	print_records = ''
	for record in records:
		print_records += str(record) + "\n"

	query_label = Label(recordsWindow, text=print_records, bg='blue', fg='white')
	query_label.grid(row=13, column=0, columnspan=2)

	#Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()
	recordsWindow.mainloop()


# Create Text Boxes
f_name = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
f_name.grid(row=1, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
l_name.grid(row=2, column=1)
categoryType = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
categoryType.grid(row=3, column=1)
projectTitle = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
projectTitle.grid(row=4, column=1)
totalDays = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
totalDays.grid(row=5, column=1)
progressDays = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
progressDays.grid(row=6, column=1)
delete_box = Entry(root, width=30, fg="yellow", bg="purple", borderwidth=10)
delete_box.grid(row=10, column=1, pady=5)


# Create Text Box Labels
f_name_label = Label(root, text="First Name", fg="red", borderwidth=10)
f_name_label.grid(row=1, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name", fg="red", borderwidth=10)
l_name_label.grid(row=2, column=0)
categoryType_label = Label(root, text="Category", fg="red", borderwidth=10)
categoryType_label.grid(row=3, column=0)
projectTitle_label = Label(root, text="Project Title", fg="red", borderwidth=10)
projectTitle_label.grid(row=4, column=0)
totalDays_label = Label(root, text="Total Days", fg="red", borderwidth=10)
totalDays_label.grid(row=5, column=0)
progressDays_label = Label(root, text="Progress Days", fg="red", borderwidth=10)
progressDays_label.grid(row=6, column=0)
delete_box_label = Label(root, text="Select ID", fg="red", borderwidth=10)
delete_box_label.grid(row=10, column=0, pady=5)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit,  fg="blue", bg="violet", borderwidth=40)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query,  fg="blue", bg="red", borderwidth=4)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", command=delete,  fg="blue", bg="violet", borderwidth=4)
delete_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit,  fg="blue", bg="violet", borderwidth=4)
edit_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


#Commit Changes
conn.commit()

# Close Connection 
conn.close()

#scrollbar.config(command=query.grid)


root.mainloop()
