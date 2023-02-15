from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3

def call_record():
	call = Tk()
	call.title("Call Records")
	call.geometry("1300x800")



	#--------------FUNCTIONS---------------#

	def run_query(query, parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query, parameters)
		conn.commit()
		return query_result

	def view_record():
		record = tree.get_children()
		for element in record:
			tree.delete(element)
		query = "SELECT * FROM call"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000,text = data[0], values = data[1:])

	def validation():
		return len(entry_call.get())!=0, len(entry_callno.get())!=0, len(entry_reason.get())!=0, len(entry_calltime.get())!=0, len(entry_calldate.get())!=0, 

	def add_record():
		if validation():
			query = "INSERT INTO call VALUES(NULL,?,?,?,?,?)"
			parameters = (entry_call.get(),entry_callno.get(), entry_reason.get(),entry_calltime.get(),entry_calldate.get())
			run_query(query,parameters)
			display["text"] = "Record {} has been added".format(entry_call.get())
			
			entry_call.delete(0,END)
			entry_callno.delete(0,END)
			entry_reason.delete(0,END)
			entry_calltime.delete(0,END)

		else:
			display["text"] = "Please input all fields"
		view_record()


	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:

			display["text"] = "Please select a record to delete"
		query = "DELETE FROM call WHERE ID=?"
		number = tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		caller_text = tree.item(tree.selection())["values"][0]
		callno_text = tree.item(tree.selection())["values"][1]
		reason_text = tree.item(tree.selection())["values"][2]
		calltime_text = tree.item(tree.selection())["values"][3]
		calldate_text = tree.item(tree.selection())["values"][4]

		new_edit = Toplevel()
		new_edit.title("Edit Record")

		Label(new_edit, text = "Old(Name of Caller)").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = caller_text),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New(Name of Caller)").grid(row = 1, column = 0)
		new_caller = Entry(new_edit)
		new_caller.grid(row = 1, column = 1)

		Label(new_edit, text = "Old(Caller's Phone Number)").grid(row = 2, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = caller_text),state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text = "New(Caller's Phone Number)").grid(row = 3, column = 0)
		new_callerno = Entry(new_edit)
		new_callerno.grid(row = 3, column = 1)

		Label(new_edit, text = "Old(Reason for Call)").grid(row = 4, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = caller_text),state = "readonly").grid(row = 4, column = 1)
		Label(new_edit, text = "New(Reason for Call)").grid(row = 5, column = 0)
		new_reason = Entry(new_edit)
		new_reason.grid(row = 5, column = 1)

		Label(new_edit, text = "Old(Time of Call)").grid(row = 6, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = caller_text),state = "readonly").grid(row = 6, column = 1)
		Label(new_edit, text = "New(Time of Call)").grid(row = 7, column = 0)
		new_time = Entry(new_edit)
		new_time.grid(row = 7, column = 1)

		Label(new_edit, text = "Old(Date of Call)").grid(row = 8, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = caller_text),state = "readonly").grid(row = 8, column = 1)
		Label(new_edit, text = "New(Date of Call)").grid(row =  9, column = 0)
		new_date = DateEntry(new_edit)
		new_date.grid(row = 9, column = 1)
		Button(new_edit, text = "Save Changes",command = lambda:edit_record(new_caller.get(),caller_text,new_callerno.get(), callno_text, new_reason.get(),reason_text,new_time.get(), calltime_text,new_date.get(),calldate_text)).grid(row= 10, column = 1)


		new_edit.mainloop()


	def edit_record(new_caller,caller_text,new_callerno,callno_text,new_reason,reason_text,new_time,calltime_text,new_date,calldate_text):
		query = "UPDATE call SET name=?, phone=?,reason=?,timee=?,datee=? WHERE name=? AND phone=? AND reason=? AND timee=? AND datee=?"
		parameters = (new_caller, new_callerno, new_reason, new_time, new_date,caller_text,callno_text,reason_text,calltime_text,calldate_text)
		run_query(query,parameters)
		display["text"] = "Record {} as been updated to {}".format(caller_text,new_caller)
		view_record()

	#--------------IMAGES-------------------#
	
	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\call.png"))
	img_label = Label(call,image = img, height = 320)
	img_label.grid(row = 1, column = 1,pady = 5)


	#--------------FRAMES-------------------#

	frame = LabelFrame(call, width = 60, height = 30, padx = 20, pady = 10, bg = "#204524")
	frame.grid(row = 1, column = 0, padx = 20, pady = 6, sticky = W)

	#--------------LABELS-------------------#

	title_label = Label(call, text = "Call Records", font = "Impact 30 bold italic underline", fg = "#750d1b", padx = 10, pady = 10)
	title_label.grid(row = 0, column = 0)

	call_label = Label(frame, text = "Name of Caller", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524")
	call_label.grid(row = 1, column = 0)

	callno_label = Label(frame, text = "Caller's Phone Number", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524")
	callno_label.grid(row = 2, column = 0)

	reason_label = Label(frame, text = "Reason for Call", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524")
	reason_label.grid(row = 3, column = 0)

	time_label = Label(frame, text = "Time of Call", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524")
	time_label.grid(row = 4, column = 0)

	date_label = Label(frame, text = "Date", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524")
	date_label.grid(row = 5, column = 0)

	add_but = Button(frame,text = "Add New Record", cursor = "hand2", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 , bg = "#204524",command = add_record)
	add_but.grid(row = 6, column = 1, pady = 10)


	display = Label(frame, text = "",fg = "cyan",bg = "#204524")
	display.grid(row = 7, column = 1)

	#--------------ENTRIES------------------#

	caller_text = StringVar()
	entry_call = Entry(frame, textvariable = caller_text, width = 50, bd = 3)
	entry_call.grid(row = 1, column = 1)

	callno_text  = StringVar()
	entry_callno = Entry(frame, textvariable = callno_text, width = 50, bd = 3)
	entry_callno.grid(row = 2, column = 1)

	reason_text = StringVar()
	entry_reason = Entry(frame, textvariable = reason_text, width = 50, bd = 3)
	entry_reason.grid(row = 3, column = 1)

	calltime_text = StringVar()
	entry_calltime = Entry(frame, textvariable = calltime_text, width = 50, bd = 3)
	entry_calltime.grid(row = 4, column = 1)

	calldate_text = StringVar()
	entry_calldate = DateEntry(frame, textvariable = calldate_text, width = 47, bd = 3)
	entry_calldate.grid(row = 5, column = 1)


	#--------------TREEVIEW-----------------#

	tree = ttk.Treeview(call, height = 150, columns = ["","","","",""])
	tree.grid(row = 7, column = 0, columnspan = 2, padx = 10, pady = 10)

	style = ttk.Style()
	style.configure("Tree.Heading", font = "courier 12 bold italic")

	tree.heading("#0", text = "ID")
	tree.column("#0", width = 50)

	tree.heading("#1", text = "Name of Caller")
	tree.column("#1", width = 200)

	tree.heading("#2", text = "Phone number of Caller")
	tree.column("#2", width = 260)

	tree.heading("#3", text = "Reason for Call")
	tree.column("#3", width = 150)

	tree.heading("#4", text = "Time of Call")
	tree.column("#4", width = 150)

	tree.heading("#5", text = "Date")
	tree.column("#5", width = 100)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Helvetica 12 italic bold")
			
  

	#--------------MENUS--------------------#

	main_menu = Menu()
	submenu= Menu()

	main_menu.add_cascade(label = "File", menu = submenu)
	main_menu.add_cascade(label = "Add",command = add_record)
	main_menu.add_cascade(label = "Edit",command = edit_box)
	main_menu.add_cascade(label = "Delete",command = delete_record)
	main_menu.add_cascade(label = "Help")#command = helpp)
	main_menu.add_cascade(label = "Exit", command = call.destroy)

	submenu.add_command(label ="Add Record",command = add_record)
	submenu.add_command(label ="Edit Record",command = edit_box)
	submenu.add_command(label ="Delete Record",command = delete_record)
	submenu.add_separator()
	submenu.add_command(label ="Help")#command = helpp)
	submenu.add_command(label ="Exit", command = call.destroy)

	call.configure(menu = main_menu)
	view_record()

	#-------------TIME AND DATE-------------#

	def tick():
		d = datetime.datetime.now()
		mytime = time.strftime("%I : %M : %S%p")
		mydate = "{:%B %d %Y}".format(d)
		lblInfo.configure(text = mytime +"\t" + mydate)
		lblInfo.after(200,tick)
	lblInfo = Label(call, font = "calibri 13 bold italic", fg = "blue")
	lblInfo.grid(row = 0, column = 1, columnspan = 2)
	tick()












	call.mainloop()
call_record()