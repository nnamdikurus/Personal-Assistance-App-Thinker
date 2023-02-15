from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3

def social_media():
	sm = Tk()
	sm.geometry("1000x800")
	sm.configure(background = "#a2e0f5")
	sm.title("Social Media Personelle Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM social"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(sm_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO social VALUES(NULL,?)"
			parameters = (sm_entry.get(),)#-----Just add a Comma for ony one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			sm_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM social WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_sm = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_sm),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_sm_entry = Entry(new_edit)
		new_sm_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",command = lambda:edit_record(new_sm_entry.get(),job_sm)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_sm_entry,job_sm):
		global new_edit
		query = "UPDATE social SET job = ? WHERE job = ?"
		parameters = (new_sm_entry,job_sm)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_sm,new_sm_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	sm_label = Label(sm, text = "Customer Service Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	sm_label.grid(row = 0, column = 0)

	frame = LabelFrame(sm, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	sm_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	sm_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	sm_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	sm_entry.grid(row = 1, column = 1, padx = 20)

	sm_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	sm_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(sm, column = ["",""], height = 20)
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
	lblInfo = Label(sm, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = sm.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = sm.destroy)


	sm.configure(menu = main_menu)
	view_record()


	sm.mainloop()
social_media()