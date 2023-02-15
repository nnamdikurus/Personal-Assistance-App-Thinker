from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3

def personal_assistant():
	pa = Tk()
	pa.geometry("1000x800")
	pa.configure(background = "#a2e0f5")
	pa.title("Personal Assistant Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM personal"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(pa_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO personal VALUES(NULL,?)"
			parameters = (pa_entry.get(),)#-----Just add a Comma for ony one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			pa_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM personal WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_pa = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel(pa)
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_pa),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_pa_entry = Entry(new_edit)
		new_pa_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",command = lambda:edit_record(new_pa_entry.get(),job_pa)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_pa_entry,job_pa):
		global new_edit
		query = "UPDATE personal SET job = ? WHERE job = ?"
		parameters = (new_pa_entry,job_pa)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_pa,new_pa_entry)

		view_record()

	#---------------LABELS------------------------

	pa_label = Label(pa, text = "Personal Assistant Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	pa_label.grid(row = 0, column = 0)

	frame = LabelFrame(pa, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	pa_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	pa_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	pa_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	pa_entry.grid(row = 1, column = 1, padx = 20)

	pa_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	pa_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(pa, column = ["",""], height = 20)
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
	lblInfo = Label(pa, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
	lblInfo.grid(row=5, column = 0, columnspan = 2)
	tick()



	#----------------Menu-----------------------#


	main_menu = Menu()
	sub_menu = Menu()

	main_menu.add_cascade(label = "File", menu = sub_menu)
	main_menu.add_cascade(label = "Add", command = add_record)
	main_menu.add_cascade(label = "Delete", command = delete_record)
	main_menu.add_cascade(label = "Edit", command = edit_box)
	main_menu.add_cascade(label = "Help")
	main_menu.add_cascade(label = "Exit", command = pa.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help")
	sub_menu.add_command(label = "Exit", command = pa.destroy)


	pa.configure(menu = main_menu)
	view_record()


	pa.mainloop()
personal_assistant()