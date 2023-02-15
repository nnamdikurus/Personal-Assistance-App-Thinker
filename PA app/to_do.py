from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import datetime
import time
import sqlite3

def todolist():
	global tree
	todo = Tk()
	todo.title("To - do List")
	todo.geometry("1200x800")
	todo.configure(background = "#514d63")

	#------------------FUNCTIONS-----------------

	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)#------Put the query there and change to this------------
		conn.commit()
		return query_result

	def view_record():
		#record = tree.get_children()
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM todo"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000,text = data[0], values = data[1:])

	def validation():
		return len(date_text.get())!=0 and len(day_text.get())!=0 and len(todo_text.get())!=0 and len(status_text.get())!=0


	def add_record():
		pop = messagebox.askquestion("Add New Entry","Do you want to Add New Entry?")
		if pop == "yes":
			if validation():
				query = "INSERT INTO todo VALUES(?,?,?,?)"
				parameters = (date_entry.get(),day_text.get(),todo_entry.get(),status_text.get())
				run_query(query,parameters)
				display["text"] = "Record {} has been added".format(todo_entry.get())

				date_entry.delete(0,END)
				todo_entry.delete(0,END)

			else:
				display["text"] = "Fields not completed. Please fill all entries"
			view_record()

	def delete_record():
		pop = messagebox.askquestion("Delete Record","Do you want to delete this record? This action cannot be reversed")
		if pop == "yes":
			try:
				tree.item(tree.selection())["values"][1]

			except IndexError as e:
			
				display["text"] = "Please select a record to delete"
			number = tree.item(tree.selection())["text"]
			query = "DELETE FROM todo WHERE datee =?"

			run_query(query,(number,))
			display["text"] = "Record {} has been deleted".format(number)
			view_record()



	def edit_box():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"] = "Please select record to edit"
			return
		date_text = tree.item(tree.selection())["values"][0]
		#day_text = tree.item(tree.selection())["values"][3]
		todo_text = tree.item(tree.selection())["values"][1]
		status_text = tree.item(tree.selection())["values"][2]

		new_edit = Toplevel(todo)
		new_edit.title("Edit Record")

		Label(new_edit, text = "Old Date").grid(row=0,column=0)
		Entry(new_edit, state="readonly").grid(row=0,column=1)
		Label(new_edit, text = "New Date").grid(row=1,column=0)
		new_date = DateEntry(new_edit)
		new_date.grid(row = 1, column =1)

		Label(new_edit, text = "Old Day").grid(row = 2,column = 0)
		Entry(new_edit,textvariable=StringVar(new_edit,value=date_text),state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text="New Day").grid(row = 3, column = 0)
		new_day = Entry(new_edit)
		new_day.grid(row=3,column = 1)

		Label(new_edit, text = "Old To -Do List").grid(row=4,column=0)
		Entry(new_edit,textvariable=StringVar(new_edit, value=todo_text),state="readonly").grid(row=4,column=1)
		Label(new_edit, text = "New To -Do List").grid(row=5,column=0)
		new_todo = Entry(new_edit)
		new_todo.grid(row = 5, column =1)

		Label(new_edit, text = "Old Status").grid(row = 6,column = 0)
		Entry(new_edit,textvariable=StringVar(new_edit, value=status_text),state = "readonly").grid(row = 6, column = 1)
		Label(new_edit, text="New Status").grid(row = 7, column = 0)
		new_status = Entry(new_edit)
		new_status.grid(row=7,column = 1)

		Button(new_edit, text = "Save Changes", command = lambda:edit_record(new_date.get(),date_text,new_day.get(),day_text,new_todo.get(),todo_text,new_status.get(),status_text)).grid(row = 8, column = 1, sticky = W)

		new_edit.mainloop()
		
	def edit_record(new_date,date_text,new_day,day_text,new_todo,todo_text,new_status,status_text):
		query = "UPDATE todo SET datee=?, day=?,to_do=?,status=? WHERE datee=? AND day=? AND to_do=? AND status=?"
		parameters = (new_date,new_day,new_todo,new_status,date_text,day_text,todo_text,status_text)
		run_query(query,parameters)
		display["text"] = "{} was changed to {}".format(date_text,new_date)
		view_record()


	def helpp():
		messagebox.showinfo("Log", "Report Sent")

	def exit():
		pop = messagebox.askquestion("Exit Window", "Do you want to exit window")
		if pop == "yes":
			todo.destroy()
	#-------------Image------------------

	img = PhotoImage(file = "C:\\Icons\\todo1.png")
	img_label = Label(todo, image = img, height = 350, width = 500)
	img_label.grid(row = 0, column = 0, padx = 10, pady = 20)

	#--------------FRAMES----------------------

	frame = LabelFrame(todo, width = 50, text = "Add To-do List", bg = "#dbb986", padx = 20, font = "arial 10 bold",fg = "blue")
	frame.grid(row = 0, column = 1, sticky = N, pady = 20, padx = 20)

	#------------LABELS--------------

	date_label = Label(frame, text = "Date", font = "Arial 15 bold italic", fg = "black", bg = "#dbb986")
	date_label.grid(row = 0, column = 1, padx = 10, pady = 20, sticky = N)

	date_label = Label(frame, text = "Day", font = "Arial 15 bold italic", fg = "black", bg = "#dbb986")
	date_label.grid(row = 1, column = 1, padx = 10, pady = 20, sticky = N)

	todo_label = Label(frame, text = "To - do List", font = "Arial 15 bold italic", fg = "black", bg = "#dbb986")
	todo_label.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = N)

	todo_label = Label(frame, text = "Status", font = "Arial 15 bold italic", fg = "black", bg = "#dbb986")
	todo_label.grid(row = 3, column = 1, padx = 10, pady = 20, sticky = N)

	#-------------------ENTRIES------------------

	date_text = StringVar()
	date_entry = DateEntry(frame, textvariable = date_text, width = 20)
	date_entry.grid(row = 0, column = 2)

	day_text = StringVar()
	days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
	days_entry = OptionMenu(frame, day_text,*days)
	days_entry.grid(row = 1, column = 2)

	todo_text = StringVar()
	todo_entry = Entry(frame, textvariable = todo_text, width = 40)
	todo_entry.grid(row = 2, column = 2, padx = 10)

	status_text = StringVar()
	status_entry = OptionMenu(frame, status_text, "Pending","Completed")
	status_entry.grid(row = 3, column = 2)

	#---------------------BUTTONS---------------

	add_but = Button(frame, text = "Add Record", bg = "#dbb986", font = "Arial 10 bold italic", fg = "black",command = add_record)
	add_but.grid(row = 4, column = 2, pady = 10)

	#-------------------POP-UP DISPLAY----------------

	display = Label(frame,text = "", fg = "green",bg = "#dbb986")
	display.grid(row = 5, column = 2)

	#--------------------TREEVIEW----------------------

	tree = ttk.Treeview(todo, height = 20, column = ["","","",""])
	tree.grid(row = 6, column = 0, columnspan = 4, padx = 20)

	#----------------TREEVIEW HEADERS AND COLUMNS-----------
	
	style = ttk.Style()
	style.configure("Treeview.Heading", font= ("Arial 13 bold italic"))
	tree.heading("#0", text = "Date")
	tree.column("#0", width = 70)

	tree.heading("#1", text = "Day")
	tree.column("#1", width = 80)

	tree.heading("#2", text = "To - do List")
	tree.column("#2", width = 250)

	tree.heading("#3", text = "Status")
	tree.column("#3", width = 80)

	#-----------------MENU AND SUBMENUS---------------
	chooser = Menu()
	itemone = Menu()
	chooser.add_cascade(label = "File", menu = itemone)
	chooser.add_cascade(label = "Add",command = add_record)
	chooser.add_cascade(label = "Delete", command = delete_record)
	chooser.add_cascade(label = "Edit", command = edit_box)
	chooser.add_cascade(label = "Help", command = helpp)
	chooser.add_cascade(label = "Exit", command = exit)

	itemone.add_command(label = "Add Record",command = add_record)
	itemone.add_command(label = "Delete Record", command = delete_record)
	itemone.add_command(label = "Edit Record", command = edit_box)
	itemone.add_separator()
	itemone.add_command(label = "Help", command = helpp)
	itemone.add_command(label = "Exit", command = exit)


	todo.config(menu = chooser)
	view_record()



	todo.mainloop()
todolist()