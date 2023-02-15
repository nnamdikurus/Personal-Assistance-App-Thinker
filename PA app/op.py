from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3

def op_manager():
	op = Tk()
	op.geometry("1000x800")
	op.configure(background = "#a2e0f5")
	op.title("Business Development Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM op"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(op_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO op VALUES(NULL,?)"
			parameters = (op_entry.get(),)#-----Just add a Comma for only one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			op_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM op WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_op = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_op),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_op_entry = Entry(new_edit)
		new_op_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",command = lambda:edit_record(new_op_entry.get(),job_op)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_op_entry,job_op):
		global new_edit
		query = "UPDATE op SET job = ? WHERE job = ?"
		parameters = (new_op_entry,job_op)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_op,new_op_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	op_label = Label(op, text = "Operations Manager Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	op_label.grid(row = 0, column = 0)

	frame = LabelFrame(op, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	op_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	op_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	op_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	op_entry.grid(row = 1, column = 1, padx = 20)

	op_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	op_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(op, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")

	tree.heading("#0", text = "ID")
	tree.column("#0", width = 50)

	tree.heading("#1", text= "		Job Description")
	tree.column("#1", width = 500)

	#------------------TIME AND DATE-----------
	def tick():
		d = datetime.datetime.now()
		my_date = "{:%B %d %Y}".format(d)
		my_time = time.strftime("%I: %M: %S%p")
		lblInfo.config(text = my_time + "\t" + "\t" + my_date)
		lblInfo.after(300,tick)
	lblInfo = Label(op, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
	lblInfo.grid(row=5, column = 0, columnspan = 2)
	tick()



	#----------------Menu-----------------------#


	main_menu = Menu()
	sub_menu = Menu()

	main_menu.add_cascade(label = "File", menu = sub_menu)
	main_menu.add_cascade(label = "Add", command = add_record)
	main_menu.add_cascade(label = "Delete", command = delete_record)
	main_menu.add_cascade(label = "Edit", command = edit_box)
	main_menu.add_cascade(label = "Help", command = helpp)
	main_menu.add_cascade(label = "Exit", command = op.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = op.destroy)


	op.configure(menu = main_menu)
	view_record()


	op.mainloop()
op_manager()