from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import filedialog
from ttkthemes import themed_tk
import datetime
import time
import sqlite3



def call_record():
	call = Toplevel(root)
	call.geometry("1300x1300+0+0")
	#call.configure(background = "")
	call.title("Call Records")
	canvas = Canvas(call, width = 1800, height = 1200)
	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\clock.png"))
	canvas.create_image(0,0,anchor = NW, image = img)
	#canvas.grid(row = 0, column = 0)

	
				#FUNCTIONS

	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result

	def view_record():
		record = tree.get_children()
		for element in record:
			tree.delete(element)
		query = "SELECT * FROM call"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000, text = data[0], values = data[1:])

	def validation():
		return len(entry_call.get())!=0, len(entry_callno.get())!=0,  len(entry_reason.get())!=0, len(entry_calltime.get())!=0, len(entry_calldate.get())!=0

	def add_record():
		if validation():
			query = "INSERT INTO call VALUES(NULL,?,?,?,?,?)"
			parameters = (entry_call.get(),entry_callno.get(),entry_reason.get(),entry_calltime.get(),entry_calldate.get())
			run_query(query,parameters)
			display["text"] = "Record {} has been added".format(entry_call.get())
			
			entry_call.delete(0,END)
			entry_callno.delete(0,END)
			entry_reason.delete(0,END)
			entry_calltime.delete(0,END)
			entry_calldate.delete(0,END)

		else:
			display["text"] = "Please fill all entries"
		view_record()



	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"] = "Please select a record to delete"

		query = "DELETE FROM call WHERE ID = ?"
		number = tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		try:
			tree.item(tree.selection())["values"][0]
		except:
			display["text"] = "Please select a record to edit"
		caller_text = tree.item(tree.selection())["values"][0]
		callno_text = tree.item(tree.selection())["values"][1]
		reason_text = tree.item(tree.selection())["values"][2]
		time_text = tree.item(tree.selection())["values"][4]	
		date_text = tree.item(tree.selection())["values"][3]

		new_edit = Toplevel()
		new_edit.title("Edit Record")

		Label(new_edit, text = "Old(Name of Caller)").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, caller_text), state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New(Name of Caller)").grid(row = 1, column = 0)
		new_caller = Entry(new_edit)
		new_caller.grid(row = 1, column = 1)

		Label(new_edit, text = "Old(Caller number)").grid(row = 2, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, callno_text), state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text = "New(Caller number)").grid(row = 3, column = 0)
		new_callno = Entry(new_edit)
		new_callno.grid(row = 3, column = 1)

		Label(new_edit, text = "Old(Reason for Call)").grid(row = 4, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, reason_text), state = "readonly").grid(row = 4, column = 1)
		Label(new_edit, text = "New(Reason for Call)").grid(row = 5, column = 0)
		new_reason = Entry(new_edit)
		new_reason.grid(row = 5, column = 1)

		Label(new_edit, text = "Old(Time for Meeting)").grid(row = 6, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, time_text), state = "readonly").grid(row = 6, column = 1)
		Label(new_edit, text = "New(Time for Meeting)").grid(row = 7, column = 0)
		new_time = Entry(new_edit)
		new_time.grid(row = 7, column = 1)

		Label(new_edit, text = "Old(Time for Meeting)").grid(row = 8, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, date_text), state = "readonly").grid(row = 8, column = 1)
		Label(new_edit, text = "New(Time for Meeting)").grid(row = 9, column = 0)
		new_date = DateEntry(new_edit)
		new_date.grid(row = 9, column = 1)
		
		new_but = Button(new_edit, text = "Save Changes", cursor = "hand2",command = lambda:edit_record(new_caller.get(), caller_text, new_callno.get(),callno_text,new_reason.get(), reason_text,new_time.get(),time_text,new_date.get(),date_text))
		new_but.grid(row = 12, column = 1)

		new_edit.mainloop()

	def edit_record(new_caller,caller_text,new_callno,callno_text,new_reason,reason_text,new_time ,time_text,new_date,date_text):
		query = "UPDATE call SET name = ?, phone = ?, reason = ?, timee = ?, datee = ? WHERE  name = ? AND  phone = ? AND  reason = ? AND  timee = ? AND  datee = ?"
		parameters = (new_caller,new_callno,new_reason,new_time,new_date,caller_text,callno_text,reason_text,time_text,date_text)
		run_query(query,parameters)
		display["text"] = "Record {} has been changed to {}".format(caller_text,new_caller)

		view_record()

	def helpp():
		messagebox.showinfo("Help!!!","This is Dean Winchester, and I need your help. Linwood Memorial Hospital")

				#FRAME

	frame = LabelFrame(call, width = 60, height = 30, padx = 20, pady = 5, bg = "#204524")
	frame.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = W)

				#IMAGE

	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\call.png"))
	img_label = Label(call,image = img, height = 320)
	img_label.grid(row = 1, column = 1,pady = 5)



				#LABELS

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


				#ENTRY

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
	entry_calldate = DateEntry(frame, textvariable = calldate_text, width = 35, bd = 3)
	entry_calldate.grid(row = 5, column = 1)

				#BUTTONS

	but_add = Button(frame, text = "Add Call Record", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10 ,bg = "#204524", bd = 3, command = add_record)
	but_add.grid(row = 6, column = 1, pady = 12)

	display = Label(frame, text = "", fg = "blue",font = "Times 15 bold italic",bg = "#204524")
	display.grid(row = 7, column = 1)


	but_edit = Button(frame, text = "Edit Call Record", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524" , command = edit_box)
	but_edit.grid(row = 6, column = 0, pady = 5)

	but_del = Button(frame, text = "Delete Call Record", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524" , command = delete_record)
	but_del.grid(row = 6, column = 2, pady = 5)

	close_window = Button(call, text = "Close Window", font = "Times 15 bold italic", fg = "white", bg = "red", padx = 10, pady = 5 , command = call.destroy)
	close_window.grid(row = 8, column = 0,padx =(450,0), pady = 5)


	tree = ttk.Treeview(call, height = 14, column = ["","","",""])
	tree.grid(row = 7, column = 0, columnspan = 4)

	#----------------TREEVIEW HEADERS AND COLUMNS-----------
	
	style = ttk.Style()
	
	style.configure("Treeview.Heading", font= ("Arial 11 bold italic"))
	style.configure("Treeview", font= ("Arial 10 bold italic"))

	tree.heading("#0", text = "Caller")
	tree.column("#0", width = 170)

	tree.heading("#1", text = "Caller Number")
	tree.column("#1", width = 180)

	tree.heading("#2", text = "Reason for Call")
	tree.column("#2", width = 250)

	tree.heading("#3", text = "Time")
	tree.column("#3", width = 180)


	tree.heading("#4", text = "Date")
	tree.column("#4", width = 180)

	view_record()



	call.mainloop()





def minutes():
	minn = Toplevel(root)
	minn.geometry("1400x1000")
	minn.title("Minutes of Meeting")
	minn.configure(background = "#8499ba")


			#FUNCTIONS

	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		top_entry.delete(0,END)
		top_entry.insert(END,selected_tuple[1])

		create_entry.delete(0,END)
		create_entry.insert(END,selected_tuple[2])

		date_entry.delete(0,END)
		date_entry.insert(END,selected_tuple[3])

		time_entry.delete(0,END)
		time_entry.insert(END,selected_tuple[4])

		#textbox.delete(0,END)
		#textbox.insert(END,selected_tuple[5])

	def view_command():
		listbox.delete(0,END)
		for row in min_back.view():
			listbox.insert(END,row)

	def insert_command():
		min_back.insert(top_text.get(),create_text.get(),date_text.get(),time_text.get(),textbox.get())
		listbox.delete(0,END)
		listbox.insert(END,(top_text.get(),create_text.get(),date_text.get(),time_text.get(),min_text))
		
	def update_command():
		min_back.update(selected_tuple[0], top_text.get(),create_text.get(),date_text.get(),time_text.get(),min_text)

	def delete_command():
		min_back.delete(selected_tuple[0])

	def clear_entry():
		top_entry.delete(0,END)
		create_entry.delete(0,END)
		date_entry.delete(0,END)
		time_entry.delete(0,END)
		textbox.delete(0,END)


				#FRAME

	frame = LabelFrame(minn, width = 25, relief = SUNKEN, bg = "#8499ba", pady = 20, padx = 20, bd = 5)
	frame.grid(row = 1, column = 0, rowspan = 2)

	frame1 = LabelFrame(minn, width = 25, relief = SUNKEN, bg = "#8499ba", pady = 20, padx = 20, bd = 5)
	frame1.grid(row = 1, column = 1)


				#LABELS

	title_label = Label(minn, text = "Managing Minutes of Meetings", padx = 15, pady = 10, bg = "#8499ba", fg = "#4c188c", width = 30, font = "Garamond 25 bold italic underline")
	title_label.grid(row = 0, column = 0)


	topic_label= Label(frame, text = "Topic of Meeting", padx = 10, pady = 10, bg = "#8499ba", fg = "#b32282", width = 15, font = "Garamond 15 bold italic")
	topic_label.grid(row = 2, column = 0, sticky = W)

	created_label = Label(frame, text = "Created by", bg = "#8499ba", fg = "#b32282", width = 15, font = "Garamond 15 bold italic")
	created_label.grid(row = 3, column = 0, sticky = W)

	date_label = Label(frame, text = "Date", bg = "#8499ba", fg = "#b32282", width = 15, font = "Garamond 15 bold italic")
	date_label.grid(row = 4, column = 0, sticky = W)

	time_label = Label(frame, text = "Time", bg = "#8499ba", fg = "#b32282", width = 15, font = "Garamond 15 bold italic")
	time_label.grid(row = 5, column = 0, sticky = W)

	minutes_label = Label(frame, text = "Minutes of Meeting", padx = 25, pady = 10, bg = "#8499ba", fg = "#b32282", width = 15, font = "Garamond 15 bold italic")
	minutes_label.grid(row = 1, column = 0, sticky = W)


			#BUTTONS

	but_addmin = Button(frame, text = "Add Minutes Details", bd = 3, bg = "#38b9c2", fg = "#b32282",width = 20, font = "Garamond 11 bold italic", command = insert_command)
	but_addmin.grid(row = 6, column = 1, pady = 10)

	but_viewmin = Button(frame1, text = "View Minutes Details", bd = 3, bg = "#38b9c2", fg = "#b32282",width = 20, font = "Garamond 11 bold italic", command =  view_command)
	but_viewmin.grid(row = 1, column = 3, sticky = W, padx = 30, pady = 15)

	but_updatemin  = Button(frame1, text = "Edit Minutes Details", bd = 3, bg = "#38b9c2", fg = "#b32282",width = 20, font = "Garamond 11 bold italic", command = update_command)
	but_updatemin.grid(row = 2, column = 3, sticky = W, padx = 30, pady = 15)

	but_deletemin = Button(frame1, text = "Delete Minutes Details", bd = 3, bg = "#38b9c2", fg = "#b32282",width = 20, font = "Garamond 11 bold italic", command = delete_command)
	but_deletemin.grid(row = 3, column = 3, sticky = W, padx = 30, pady = 15)

	but_clearentry = Button(frame1, text = "Clear Entry Details", bd = 4, bg = "#38b9c2", fg = "#b32282",width = 20, font = "Garamond 11 bold italic", command = clear_entry)
	but_clearentry.grid(row = 4, column = 3, sticky = W, padx = 30, pady = 15)

	but_close = Button(minn, text = "Close Window", bd = 4, bg = "red", fg = "black",width = 20, font = "Garamond 11 bold italic", command = minn.destroy)
	but_close.grid(row = 8, column = 1, sticky = W, padx = 10, pady = 25)

					#ENTRY

	top_text = StringVar()
	top_entry = Entry(frame, textvariable = top_text, width = 50, bd = 4)
	top_entry.grid(row = 2, column = 1, sticky = N, pady = 10)

	create_text = StringVar()
	create_entry = Entry(frame, textvariable = create_text, width = 50, bd = 4)
	create_entry.grid(row = 3, column = 1, sticky = N, pady = 10)

	date_text = StringVar()
	date_entry = Entry(frame, textvariable = date_text, width = 50, bd = 4)
	date_entry.grid(row = 4, column = 1, sticky = N, pady = 10)

	time_text = StringVar()
	time_entry = Entry(frame, textvariable = time_text, width = 50, bd = 4)
	time_entry.grid(row = 5, column = 1, sticky = N, pady = 10)

	textbox = Text(frame, width = 40, height = 22, bd = 4)
	textbox.grid(row = 1, column = 1, sticky = N, padx = 2)

	listbox = Listbox(minn,width = 100, height = 20, bd = 8)
	listbox.grid(row = 2, column = 1, pady = 15, padx = 30)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)

	minn.mainloop()




def meeting_schedule():
	ms = Toplevel(root)
	ms.title("Meeting Schedule")
	ms.geometry("1300x800+0+0")
	ms.configure(background = "#8499ba")



	#------------------FUNCTIONS---------------------#

	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result

	def view_record():
		record = tree.get_children()
		for element in record:
			tree.delete(element)
		query = "SELECT * FROM meeting"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000, text = data[0], values = data[1:])

	def validation():
		return len(meet_entry.get())!=0, len(meet_entry1.get())!=0,  len(reason_entry.get())!=0, len(date_entry.get())!=0,  len(time_entry.get())!=0,  len(status_entry.get())!=0

	def add_record():
		if validation():
			query = "INSERT INTO meeting VALUES(NULL,?,?,?,?,?,?)"
			parameters = (meet_entry.get(),meet_entry1.get(),reason_entry.get(),date_entry.get(),time_entry.get(),status_entry.get())
			run_query(query,parameters)
			display["text"] = "Record {} has been added".format(meet_entry.get())
			
			meet_entry.delete(0,END)
			meet_entry1.delete(0,END)
			reason_entry.delete(0,END)
			time_entry.delete(0,END)
			status_entry.delete(0,END)

		else:
			display["text"] = "Please fill all entries"
		view_record()



	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"] = "Please select a record to delete"

		query = "DELETE FROM meeting WHERE ID = ?"
		number = tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		try:
			tree.item(tree.selection())["values"][0]
		except:
			display["text"] = "Please select a record to edit"
		meet_text = tree.item(tree.selection())["values"][0]
		meet_text1 = tree.item(tree.selection())["values"][1]
		reason_text = tree.item(tree.selection())["values"][2]
		date_text = tree.item(tree.selection())["values"][3]
		time_text = tree.item(tree.selection())["values"][4]
		status_text = tree.item(tree.selection())["values"][5]

		new_edit = Toplevel(ms)
		new_edit.title("Edit Record")

		Label(new_edit, text = "Old(Book Meeting For)").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, meet_text), state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New(Book Meeting For)").grid(row = 1, column = 0)
		new_bf = Entry(new_edit)
		new_bf.grid(row = 1, column = 1)

		Label(new_edit, text = "Old(Book Meeting By)").grid(row = 2, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, meet_text1), state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text = "New(Book Meeting By)").grid(row = 3, column = 0)
		new_bb = Entry(new_edit)
		new_bb.grid(row = 3, column = 1)

		Label(new_edit, text = "Old(Reason for Meeting)").grid(row = 4, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, reason_text), state = "readonly").grid(row = 4, column = 1)
		Label(new_edit, text = "New(Reason for Meeting)").grid(row = 5, column = 0)
		new_reason = Entry(new_edit)
		new_reason.grid(row = 5, column = 1)

		Label(new_edit, text = "Old(Date for Meeting)").grid(row = 6, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, date_text), state = "readonly").grid(row = 6, column = 1)
		Label(new_edit, text = "New(Date for Meeting)").grid(row = 7, column = 0)
		new_date = DateEntry(new_edit)
		new_date.grid(row = 7, column = 1)

		Label(new_edit, text = "Old(Time for Meeting)").grid(row = 8, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, time_text), state = "readonly").grid(row = 8, column = 1)
		Label(new_edit, text = "New(Time for Meeting)").grid(row = 9, column = 0)
		new_time = Entry(new_edit)
		new_time.grid(row = 9, column = 1)

		Label(new_edit, text = "Old(Status)").grid(row = 10, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, meet_text), state = "readonly").grid(row = 10, column = 1)
		Label(new_edit, text = "New(Status)").grid(row = 11, column = 0)
		
		new_status = ttk.Combobox(new_edit)
		new_status.config(values = ("Completed","Pending","Rescheduled","Cancelled"))
		new_status.grid(row = 11, column = 1)

		new_but = Button(new_edit, text = "Save Changes", cursor = "hand2",command = lambda:edit_record(new_bf.get(), meet_text, new_bb.get(),meet_text1,new_reason.get(), reason_text,new_date.get(),date_text,new_time.get(),time_text,new_status.get(),status_text))
		new_but.grid(row = 12, column = 1)

		new_edit.mainloop()

	def edit_record(new_bf,meet_text,new_bb,meet_text1,new_reason,reason_text,new_date,date_text,new_time,time_text,new_status,status_text):
		query = "UPDATE meeting SET mf = ?, mb = ?, reason = ?, datee = ?, timee = ?, status = ? WHERE  mf = ? AND  mb = ? AND  reason = ? AND  datee = ? AND  timee = ? AND  status = ?"
		parameters = (new_bf,new_bb,new_reason,new_date,new_time,new_status,meet_text,meet_text1,reason_text,date_text,time_text,status_text)
		run_query(query,parameters)
		display["text"] = "Record {} has been changed to {}".format(meet_text,new_bf)

		view_record()

	def helpp():
		messagebox.showinfo("Help!!!","This is Dean Winchester, and I need your help. Linwood Memorial Hospital")



	#-------------------IMAGES-----------------#

	img = PhotoImage(file = "C:\\Icons\\meet1.png")
	img_lab = Label(ms, image = img)
	img_lab.grid(row = 1, column = 1, padx = (40,0))

	#--------------------FRAMES-------------------#

	frame_label = LabelFrame(ms, padx = 15, pady = 10, bg = "#7f9494", width = 20, height= 20, relief = SUNKEN)
	frame_label.grid(row = 1, column = 0, columnspan = 1, padx = 20)

	#----------------LABELS-------------------------#

	meet_label = Label(ms, text = "Meeting Schedule", font = "Rockwell 30 bold italic underline", bg = "#8499ba", fg = "#9c3030", padx = 10, pady = 10 )
	meet_label.grid(row = 0, column = 0)

	meet_label_for = Label(frame_label, text = "Book Meeting For", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_for.grid(row = 1, column = 0)

	meet_label_by = Label(frame_label, text = "Meeting Booked By", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_by.grid(row = 2, column = 0)

	meet_label_reason = Label(frame_label, text = "Reason for Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_reason.grid(row = 3, column = 0)

	meet_label_time = Label(frame_label, text = "Date For Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_time.grid(row = 4, column = 0)

	meet_label_date = Label(frame_label, text = "Time For Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_date.grid(row = 5, column = 0)

	meet_label_status = Label(frame_label, text = "Status of Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_status.grid(row = 6, column = 0)

	but_add = Button(frame_label, text = "Add Schedule", bd = 3, cursor = "hand2",bg = "#38b9c2", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic", command = add_record)
	but_add.grid(row = 7, column = 1, padx = 10, pady = 10)

	display = Label(frame_label, text = "", fg = "green", bg = "#7f9494", font = "candara 13 bold italic")
	display.grid(row = 8, column = 1)
	#---------------ENTRIES----------------------------

	meet_text = StringVar()
	meet_entry = Entry(frame_label, textvariable = meet_text, width = 50, bd = 3)
	meet_entry.grid(row = 1, column = 1)

	meet_text1 = StringVar()
	meet_entry1 = Entry(frame_label, textvariable = meet_text1, width = 50, bd = 3)
	meet_entry1.grid(row = 2, column = 1)

	reason_text = StringVar()
	reason_entry = Entry(frame_label, textvariable = reason_text, width = 50, bd = 3)
	reason_entry.grid(row = 3, column = 1)

	time_text = StringVar()
	time_entry = Entry(frame_label, textvariable = time_text, width = 50, bd = 3)
	time_entry.grid(row = 4, column = 1)

	date_text = StringVar()
	date_entry = DateEntry(frame_label, textvariable = date_text, width = 48, bd = 3)
	date_entry.grid(row = 5, column = 1)

	status_text = StringVar()
	status_entry = ttk.Combobox(frame_label, textvariable = status_text, width = 48)
	status_entry.config(values = ("Completed","Pending","Cancelled","Rescheduled"))
	status_entry.grid(row = 6, column = 1)

	#---------------TREEVIEW----------------------------#
	
	tree = ttk.Treeview(ms, height = 120, columns = ["","","","","","",])
	tree.grid(row = 7, column = 0, columnspan = 2, pady = 30)
	tree.heading("#0", text = "ID")
	tree.column("#0", width = 50)

	tree.heading("#1", text = "Book Meeting For")
	tree.column("#1", width = 250)

	tree.heading("#2", text = "Meeting Booked By")
	tree.column("#2", width = 250)

	tree.heading("#3", text = "Reason for Meeting")
	tree.column("#3", width = 200)

	tree.heading("#4", text = "Date")
	tree.column("#4", width = 80)

	tree.heading("#5", text = "Time")
	tree.column("#5", width = 80)

	tree.heading("#6", text = "Status")
	tree.column("#6", width = 100)	
	view_record()
	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Tahoma 11 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))


	#--------------MENUS AND SUBMENU--------------------#

	main_menu = Menu()
	submenu = Menu()

	main_menu.add_cascade(label = "File", menu = submenu)
	main_menu.add_cascade(label = "Add", command = add_record)
	main_menu.add_cascade(label = "Edit", command = edit_box)
	main_menu.add_cascade(label = "Delete", command = delete_record)
	main_menu.add_cascade(label = "Help", command = helpp)
	main_menu.add_cascade(label = "Exit", command = ms.destroy)

	submenu.add_command(label = "Add Record", command = add_record)
	submenu.add_command(label = "Edit Record", command = edit_box)
	submenu.add_command(label = "Delete Record", command = delete_record)
	submenu.add_separator()	
	submenu.add_command(label = "Help", command = helpp)
	submenu.add_command(label = "Exit", command = ms.destroy)



	ms.configure(menu = main_menu)

	#------------------TIME AND DATE---------------------#

	def tick():
		d = datetime.datetime.now()
		mydate = "{:%B %d %Y}".format(d)
		mytime = time.strftime("%I: %M: %S%p")

		lblInfo.config(text = mytime + "\t" + mydate)
		lblInfo.after(300,tick)
	lblInfo = Label(ms, font = "Serif 15 bold italic", fg = "brown", bg = "#8499ba", bd = 4)
	lblInfo.grid(row = 0, column = 1, sticky = NE, columnspan = 2, pady = 5)

	tick()






	ms.mainloop()


def job_description():
	global jd
	jd = Toplevel(root)
	jd.geometry("1400x1500")
	jd.configure(background = "#a2e0f5")
	jd.title("Staff Job Description")


			#IMAGE

	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\pa3.png"))
	img_label1 = Label(jd, image = img, width = 700, height = 550)
	img_label1.grid(row = 2, column = 2)


	frame = LabelFrame(jd, padx = 15, pady = 45,width = 40, height= 50, bg = "#a2e0f5", relief = SUNKEN)
	frame.grid(row = 2, column = 0, rowspan = 5, columnspan = 2, padx = 10, pady = 10)

			#LABELS

	jd_head_label = Label(jd, text = "Staff Job Description", font = "Perpetua 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10 )
	jd_head_label.grid(row = 0, column = 2)

	jd_label = Label(jd, text = "Positions occupied in the company are:", fg = "#ba1c1c", bg = "#a2e0f5", font = "Candara 20 bold italic")
	jd_label.grid(row = 1, column = 2, pady = 20)

	jd_pa = Button (frame, text = "Personal assistant", cursor = "hand2",relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#132363", width = 25, font = "Florence 18 bold italic", command = personal_assistant)
	jd_pa.grid(row = 2, column = 0, pady = 2)

	jd_acc = Button (frame, text = " Accountant", cursor = "hand2",relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic", command  = accountant)
	jd_acc.grid(row = 3, column = 0, pady = 2)

	jd_rec = Button (frame, text = "Receptionist", cursor = "hand2",relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic", command = receptionist)
	jd_rec.grid(row = 4, column = 0, pady = 2)

	jd_cus = Button (frame, text = "Customer Service",cursor = "hand2", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic", command = customer_service)
	jd_cus.grid(row = 5, column = 0, pady = 2)

	jd_sm = Button (frame, text = "Social Media Personnel", cursor = "hand2",relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#ed0020",width = 25, font = "Florence 18 bold italic",command = social_media)
	jd_sm.grid(row = 6, column = 0, pady = 2)

	jd_hr = Button (frame, text = "Human Resource", relief = FLAT, cursor = "hand2",bd = 3, bg = "#a2e0f5", fg = "#132363",width = 25, font = "Florence 18 bold italic",command = human_resource)
	jd_hr.grid(row = 7, column = 0, pady = 2)

	jd_bd = Button (frame, text = "Business Development Officer", cursor = "hand2",relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic", command = bus_development)
	jd_bd.grid(row = 8, column = 0, pady = 2)

	jd_op = Button (frame, text = "Operations Manager", relief = FLAT, cursor = "hand2",bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic", command = op_manager)
	jd_op.grid(row = 9, column = 0, pady = 2)

	jd_sec = Button (frame, text = "Security Personnel", relief = FLAT, cursor = "hand2",bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic", command = security)
	jd_sec.grid(row = 10, column = 0, pady = 2)

	jd_close = Button(jd, text = "Close Window", relief = RAISED, bd = 3, cursor = "hand2",bg = "red", fg = "white",width = 15, font = "Florence 15 bold italic", command = jd.destroy)
	jd_close.grid(row = 11, column = 2)

	jd.mainloop()


def security():
	sec = Toplevel(jd)
	sec.geometry("1000x800")
	sec.configure(background = "#a2e0f5")
	sec.title("Business Development Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM sec"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(sec_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO sec VALUES(NULL,?)"
			parameters = (sec_entry.get(),)#-----Just add a Comma for only one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			sec_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM sec WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_sec = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_sec),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_sec_entry = Entry(new_edit)
		new_sec_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_sec_entry.get(),job_sec)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_sec_entry,job_sec):
		global new_edit
		query = "UPDATE sec SET job = ? WHERE job = ?"
		parameters = (new_sec_entry,job_sec)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_sec,new_sec_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	sec_label = Label(sec, text = "Security Personelle Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	sec_label.grid(row = 0, column = 0)

	frame = LabelFrame(sec, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	sec_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	sec_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	sec_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	sec_entry.grid(row = 1, column = 1, padx = 20)

	sec_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	sec_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(sec, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(sec, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = sec.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = sec.destroy)


	sec.configure(menu = main_menu)
	view_record()


	sec.mainloop()




def op_manager():
	op = Toplevel(jd)
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

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_op_entry.get(),job_op)).grid(row = 2, column = 1)
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
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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



def bus_development():
	bd = Toplevel(jd)
	bd.geometry("1000x800")
	bd.configure(background = "#a2e0f5")
	bd.title("Business Development Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM bd"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(bd_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO bd VALUES(NULL,?)"
			parameters = (bd_entry.get(),)#-----Just add a Comma for only one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			bd_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM bd WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_bd = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_bd),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_bd_entry = Entry(new_edit)
		new_bd_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_bd_entry.get(),job_bd)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_bd_entry,job_bd):
		global new_edit
		query = "UPDATE bd SET job = ? WHERE job = ?"
		parameters = (new_bd_entry,job_bd)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_bd,new_bd_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	bd_label = Label(bd, text = "Business Development Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	bd_label.grid(row = 0, column = 0)

	frame = LabelFrame(bd, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	bd_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	bd_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	bd_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	bd_entry.grid(row = 1, column = 1, padx = 20)

	bd_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	bd_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(bd, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(bd, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = bd.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = bd.destroy)


	bd.configure(menu = main_menu)
	view_record()


	bd.mainloop()



def human_resource():
	hr = Toplevel(jd)
	hr.geometry("1000x800")
	hr.configure(background = "#a2e0f5")
	hr.title("Human Resources Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM hr"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(hr_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO hr VALUES(NULL,?)"
			parameters = (hr_entry.get(),)#-----Just add a Comma for only one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			hr_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM hr WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_hr = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_hr),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_hr_entry = Entry(new_edit)
		new_hr_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_hr_entry.get(),job_hr)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_hr_entry,job_hr):
		global new_edit
		query = "UPDATE hr SET job = ? WHERE job = ?"
		parameters = (new_hr_entry,job_hr)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_hr,new_hr_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	hr_label = Label(hr, text = "Human Resources Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	hr_label.grid(row = 0, column = 0)

	frame = LabelFrame(hr, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	hr_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	hr_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	hr_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	hr_entry.grid(row = 1, column = 1, padx = 20)

	hr_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	hr_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(hr, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(hr, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = hr.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = hr.destroy)


	hr.configure(menu = main_menu)
	view_record()


	hr.mainloop()


def social_media():
	sm = Toplevel(jd)
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

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_sm_entry.get(),job_sm)).grid(row = 2, column = 1)
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

	sm_label = Label(sm, text = "Social Media Personelle Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
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
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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



def customer_service():
	cus = Toplevel(jd)
	cus.geometry("1000x800")
	cus.configure(background = "#a2e0f5")
	cus.title("Customer Service Job Description")
	
	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM customer"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(cus_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO customer VALUES(NULL,?)"
			parameters = (cus_entry.get(),)#-----Just add a Comma for ony one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			cus_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM customer WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_cus = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel()
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_cus),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_cus_entry = Entry(new_edit)
		new_cus_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_cus_entry.get(),job_cus)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_cus_entry,job_cus):
		global new_edit
		query = "UPDATE customer SET job = ? WHERE job = ?"
		parameters = (new_cus_entry,job_cus)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_cus,new_cus_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	cus_label = Label(cus, text = "Customer Service Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	cus_label.grid(row = 0, column = 0)

	frame = LabelFrame(cus, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	cus_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	cus_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	cus_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	cus_entry.grid(row = 1, column = 1, padx = 20)

	cus_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	cus_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(cus, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(cus, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = cus.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = cus.destroy)


	cus.configure(menu = main_menu)
	view_record()


	cus.mainloop()



def receptionist():
	rec = Toplevel(jd)
	rec.geometry("1000x800")
	rec.configure(background = "#a2e0f5")
	rec.title("Recetionist Job Description")
	
	def run_query(query, parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query, parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM reception"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(rec_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO reception VALUES(NULL,?)"
			parameters = (rec_entry.get(),)#-----Just add a Comma for ony one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			rec_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM reception WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_rec = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel(rec)
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_rec),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_rec_entry = Entry(new_edit)
		new_rec_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_rec_entry.get(),job_rec)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_rec_entry,job_rec):
		global new_edit
		query = "UPDATE reception SET job = ? WHERE job = ?"
		parameters = (new_rec_entry,job_rec)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_rec,new_rec_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	rec_label = Label(rec, text = "Receptionist Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	rec_label.grid(row = 0, column = 0)

	frame = LabelFrame(rec, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	rec_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	rec_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	rec_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	rec_entry.grid(row = 1, column = 1, padx = 20)

	rec_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	rec_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(rec, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(rec, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = rec.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help")
	sub_menu.add_command(label = "Exit", command = rec.destroy)


	rec.configure(menu = main_menu)
	view_record()


	rec.mainloop()



def accountant():
	acc = Toplevel(jd)
	acc.geometry("1000x800")
	acc.configure(background = "#a2e0f5")
	acc.title("Accountant Job Description")
	
	def run_query(query, parameters = ()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query, parameters)
		conn.commit()
		return query_result


	def view_record():
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM account"
		connect = run_query(query)
		for data in connect:
			tree.insert("", 10000, text = data[0], values = data[1:])

	def validation():
		return len(acc_entry.get())!=0

	def add_record(): 
		if validation():
			query = "INSERT INTO account VALUES(NULL,?)"
			parameters = (acc_entry.get(),)#-----Just add a Comma for ony one entry
			run_query(query,parameters)
			display["text"] = "New Job Role has been added"

			acc_entry.delete(0,END)

		else:
			display["text"] = "Please fill in the field"
		view_record()

	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"]="Select a record to delete"
	
		query = "DELETE FROM account WHERE ID=?"
		number= tree.item(tree.selection())["text"]
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()

	def edit_box():
		tree.item(tree.selection())["values"][0]
		job_acc = tree.item(tree.selection())["values"][0]


		new_edit = Toplevel(acc)
		new_edit.title("Edit New Record")
		new_edit.geometry("600x300")

		Label(new_edit, text = "Old Job Description").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = job_acc),state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Job Description").grid(row = 1, column = 0)
		new_acc_entry = Entry(new_edit)
		new_acc_entry.grid(row = 1, column = 1)

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_acc_entry.get(),job_acc)).grid(row = 2, column = 1)
		new_edit.mainloop()


	def edit_record(new_acc_entry,job_acc):
		global new_edit
		query = "UPDATE account SET job = ? WHERE job = ?"
		parameters = (new_acc_entry,job_acc)
		run_query(query,parameters)
		display["text"] = "Record {} has been updated to {}".format(job_acc,new_acc_entry)

		view_record()


	def helpp():
		messagebox.showinfo("Hey!!!", "This is Dean Winchester, and I need your help")

	#---------------LABELS------------------------

	acc_label = Label(acc, text = "Accountant Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	acc_label.grid(row = 0, column = 0)

	frame = LabelFrame(acc, bd = 3, relief = RIDGE, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic",)
	frame.grid(row = 1, column = 0, padx = 20, pady = 20)

	acc_jd = Label(frame, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#cc3333", fg = "dark blue", pady = 10)
	acc_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

	entry_text = StringVar()
	acc_entry = Entry(frame, textvariable = entry_text, width = 70, bd = 4)
	acc_entry.grid(row = 1, column = 1, padx = 20)

	acc_add = Button(frame, text = "Add Job Description", cursor = "hand2", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = add_record)
	acc_add.grid(row = 2, column = 1, pady = 20)

	display = Label(frame, text = "", fg = "light green",bg = "#cc3333", font = "calibri 10 bold italic")
	display.grid(row = 3, column =1)

	#------------------TREEVIEW-----------------------#

	tree = ttk.Treeview(acc, column = ["",""], height = 20)
	tree.grid(row = 3, column = 0, padx = 30, pady = 20)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = "Garamond 12 bold italic")
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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
	lblInfo = Label(acc, font = "Helvetica 15 italic bold", fg = "green", bg = "#a2e0f5")
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
	main_menu.add_cascade(label = "Exit", command = acc.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help")
	sub_menu.add_command(label = "Exit", command = acc.destroy)


	acc.configure(menu = main_menu)
	view_record()


	acc.mainloop()


def personal_assistant():
	pa = Toplevel(jd)
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

		Button(new_edit, text = "Save Changes",cursor = "hand2",command = lambda:edit_record(new_pa_entry.get(),job_pa)).grid(row = 2, column = 1)
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
	style.configure("Treeview", font= ("Arial 8 bold italic"))

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

def presentation():
	pres = Toplevel(root)
	pres.title("Presentations")
	pres.geometry("1200x800+0+0")
	pres.config(background = "#4d5d75")

	#---------------FUNCTIONS----------------------#

	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result

	def view_record():
		record = tree.get_children()
		for element in record:
			tree.delete(element)
		query = "SELECT * FROM pres"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000, text = data[0], values= data[1:])

	def validation():
		return len(entry_pres.get())!=0 and len(entry_create.get())!=0 and len(entry_date.get())!=0 and len(entry_time.get())!=0 and len(entry_status.get())!=0

	def add_record():
		if validation():
			query = "INSERT INTO pres VALUES(NULL,?,?,?,?,?)"
			parameters = (entry_pres.get(), entry_create.get(),entry_date.get(), entry_time.get(), entry_status.get())
			run_query(query,parameters)
			display["text"] = "Record {} has been added".format(entry_pres.get())

			entry_pres.delete(0,END)
			entry_create.delete(0,END)
			entry_time.delete(0,END)

		else:
			display["text"] = "Please enter all fields"
		view_record()


	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
			query = "DELETE FROM pres where ID=?"
			number = tree.item(tree.selection())["text"]
			run_query(query,(number,))
			display["text"] = "Record {} has been deleted".format(number)
		
		except IndexError as e:
			display["text"] = "Please select a record to delete"
		view_record()


	def edit_box():
		tree.item(tree.selection())["values"][0]
		pres_text = tree.item(tree.selection())["values"][0]
		create_text = tree.item(tree.selection())["values"][1]
		date_text = tree.item(tree.selection())["values"][2]
		time_text = tree.item(tree.selection())["values"][3]
		status_text = tree.item(tree.selection())["values"][4]

		new_edit = Toplevel()
		new_edit.title("Edit Records")

		Label(new_edit, text = "Old Presetation Topic").grid(row = 0, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = pres_text), state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Presetation Topic").grid(row = 1, column = 0)
		new_pres = Entry(new_edit)
		new_pres.grid(row = 1, column = 1)

		Label(new_edit, text = "Created by (Old)").grid(row = 2, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = create_text), state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text = "Created By (New)").grid(row = 3, column = 0)
		new_created = Entry(new_edit)
		new_created.grid(row = 3, column = 1)

		Label(new_edit, text = "Old Date").grid(row = 4, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = date_text), state = "readonly").grid(row = 4, column = 1)
		Label(new_edit, text = "New Date").grid(row = 5, column = 0)
		new_date = DateEntry(new_edit)
		new_date.grid(row = 5, column = 1)

		Label(new_edit, text = "Old Time").grid(row = 6, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = time_text), state = "readonly").grid(row = 6, column = 1)
		Label(new_edit, text = "New Time").grid(row = 7, column = 0)
		new_time = Entry(new_edit)
		new_time.grid(row = 7, column = 1)

		Label(new_edit, text = "Old Status").grid(row = 8, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit, value = status_text), state = "readonly").grid(row = 8, column = 1)
		Label(new_edit, text = "New Status").grid(row = 9, column = 0)
		combo = ttk.Combobox(new_edit)
		combo.config(values = ("Presented","Pending","Cancelled","Rescheduled"))
		combo.grid(row = 9, column = 1)

		butt = Button(new_edit, text= "Save Changes", cursor = "hand2",command = lambda:edit_record(new_pres.get(),pres_text,new_created.get(), create_text,new_date.get(), date_text,new_time.get(), time_text,combo.get(), status_text))
		butt.grid(row = 10, column = 1)

		new_edit.mainloop()

	def edit_record(new_pres,pres_text,new_created,create_text,new_date,date_text,new_time,time_text,combo,status_text):
		query = "UPDATE pres SET presentation = ?, created = ?, datee = ?, timee = ?, status = ? WHERE presentation = ? AND created = ? AND datee = ? AND timee = ? AND status = ?"
		parameters = (new_pres, new_created, new_date, new_time, combo,pres_text, create_text, date_text, time_text, status_text)
		run_query(query,parameters)
		new_edit.destroy()
		display["text"] = "Record {} has been updated to {}".format(pres_text, new_pres)
		view_record()

	def helpp():
		messagebox.showinfo("Hey!!!","Look at my junk")



	#----------------FRAMES--------------------

	frame = LabelFrame(pres, bd = 4, bg = "#BDBDBD",relief = SUNKEN, padx = 20, pady = 20)
	frame.grid(row = 0, column = 1, sticky = NW, padx = 20, pady = 20)

	#-------------------DISPLAY------------------
	display = Label(frame, text = "", bg = "#BDBDBD",fg = "blue", font = "Arial 10 bold italic")
	display.grid(row= 7, column = 2)
	#------------------IMAGE--------------------
	img = PhotoImage(file = "C:\\Icons\\pres.png")
	img_label = Label(pres, image = img, width = 500)
	img_label.grid(row = 0, column = 0, padx = 30)



	#=================LABELS===================

	top_label = Label(pres, text= "Power Point Presentation Gallery",  font = "Courier 20 bold italic underline", bg = "#4d5d75", fg = "#b5f7e0", pady = 10)
	top_label.grid(row = 0, column = 0, sticky = N, pady =3)

	label_pres = Label(frame, text = "Presentation Topic", font = "Garamond 15 bold italic")
	label_pres.grid(row = 1, column = 1, padx = 20, pady = 20)

	label_create = Label(frame, text = "Created by", font = "Garamond 15 bold italic")
	label_create.grid(row = 2, column = 1, padx = 20, pady = 20)

	label_date = Label(frame, text = "Date of Presentation", font = "Garamond 15 bold italic")
	label_date.grid(row = 3, column = 1, padx = 20, pady = 20)

	label_time = Label(frame, text = "Time of Presentation", font = "Garamond 15 bold italic")
	label_time.grid(row = 4, column = 1, padx = 20, pady = 20)

	label_status = Label(frame, text = "Status", font = "Garamond 15 bold italic")
	label_status.grid(row = 5, column = 1, padx = 20, pady = 20)

	add_butt = Button(frame, cursor = "hand2", text = "Add Record",font = "Garamond 15 bold italic", command = add_record)
	add_butt.grid(row = 6, column = 2)

	#=================ENTRIES===================

	pres_text = StringVar()
	entry_pres = Entry(frame, textvariable = pres_text, width = 50, bd = 3)
	entry_pres.grid(row = 1, column = 2)

	create_text = StringVar()
	entry_create = Entry(frame, textvariable = create_text, width = 50, bd = 3)
	entry_create.grid(row = 2, column = 2)

	date_text = StringVar()
	entry_date = DateEntry(frame, cursor = "hand2",textvariable = date_text, width = 47, bd = 3)
	entry_date.grid(row = 3, column = 2)

	time_text = StringVar()
	entry_time = Entry(frame, textvariable = time_text, width = 50, bd = 3)
	entry_time.grid(row = 4, column = 2)

	status_text = StringVar()
	entry_status = ttk.Combobox(frame,cursor = "hand2",textvariable = status_text, width = 47)
	entry_status.config(value = ("Presented","Pending","Cancelled","Rescheduled"))
	entry_status.grid(row = 5, column = 2)


	#-----------------TREEVIEW------------------------------
	style = ttk.Style()
	style.configure("Treeview.Heading", font = ("Garamond 13 bold italic"))
	style.configure("Treeview", font= ("Arial 8 bold italic"))

	tree = ttk.Treeview(pres, column = ["","","","",""], height = 20)
	tree.grid(row = 4, column = 0, columnspan = 2, padx = 30, pady = 5, sticky = W)

	tree.heading("#0", text = "ID")
	tree.column("#0", width = 40)

	tree.heading("#1", text = "Presentation Topic")
	tree.column("#1", width = 220)

	tree.heading("#2", text = "Created By")
	tree.column("#2", width = 150)

	tree.heading("#3", text = "Date Presented")
	tree.column("#3", width = 130)

	tree.heading("#4", text = "Time")
	tree.column("#4", width = 80)

	tree.heading("#5", text = "Status")
	tree.column("#5", width = 100)
	view_record()

	main_menu = Menu()
	sub_menu = Menu()

	main_menu.add_cascade(label = "File", menu = sub_menu)
	main_menu.add_cascade(label = "Add", command = add_record)
	main_menu.add_cascade(label = "Delete", command = delete_record)
	main_menu.add_cascade(label = "Edit", command = edit_box)
	main_menu.add_cascade(label = "Help", command = helpp)
	main_menu.add_cascade(label = "Exit", command = pres.destroy)

	sub_menu.add_command(label = "Add Record", command = add_record)
	sub_menu.add_command(label = "Delete Record", command = delete_record)
	sub_menu.add_command(label = "Edit Record", command = edit_box)
	sub_menu.add_command(label = "Help", command = helpp)
	sub_menu.add_command(label = "Exit", command = pres.destroy)

	pres.config(menu = main_menu)

	pres.mainloop()



def reminder():
	rem = Toplevel(root)
	rem.title("Reminders")
	rem.geometry("1150x800+0+0")
	rem.configure(background = "#d4b09b")


	#------------FUNCTIONS-----------------#

	def run_query(query,parameters=()):
		conn = sqlite3.connect("pass.db")
		cur = conn.cursor()
		query_result = cur.execute(query,parameters)
		conn.commit()
		return query_result

	def view_record():
		record = tree.get_children()
		for element in tree.get_children():
			tree.delete(element)
		query = "SELECT * FROM reminder"
		connect = run_query(query)
		for data in connect:
			tree.insert("",10000,text = data[0], values =data[1:])


	def validation():
		return len(date_entry.get())!=0 and len(rem_entry.get())!=0 and len(time_entry.get())!=0


	def add_record():
		if validation():
			query = "INSERT INTO reminder VALUES(NULL,?,?,?)"
			parameters = (date_entry.get(),rem_entry.get(),time_entry.get())
			run_query(query,parameters)
			display["text"] = "{} has been added to the record".format(rem_text.get())
			
			date_entry.delete(0,END)
			rem_entry.delete(0,END)
			time_entry.delete(0,END)

		else:
			display["text"] = "Please enter all fields"
		
		view_record()


	def delete_record():
		try:
			tree.item(tree.selection())["values"][1]
		except IndexError as e:
			display["text"] = "Select a record to delete"
		
		query = "DELETE FROM reminder WHERE ID=?"
		number = tree.item(tree.selection())["text"]	
		run_query(query,(number,))
		display["text"] = "Record {} has been deleted".format(number)
		view_record()


	def edit_box():
		global new_edit
		tree.item(tree.selection())["values"][0]
		e_date = tree.item(tree.selection())["values"][0]
		e_rem = tree.item(tree.selection())["values"][1]
		e_time = tree.item(tree.selection())["values"][2]

		new_edit = Toplevel(rem)
		new_edit.title("Edit Record")

		Label(new_edit, text = "Old Date").grid(row = 0, column = 0)
		Entry(new_edit, state = "readonly").grid(row = 0, column = 1)
		Label(new_edit, text = "New Date").grid(row = 1, column = 0)
		newdate_entry = DateEntry(new_edit)
		newdate_entry.grid(row = 1, column = 1)

		Label(new_edit, text = "Old Reminder").grid(row = 2, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = e_rem),state = "readonly").grid(row = 2, column = 1)
		Label(new_edit, text = "New Reminder").grid(row = 3, column = 0)
		newrem_entry = Entry(new_edit) 
		newrem_entry.grid(row = 3, column = 1)

		Label(new_edit, text = "Old Time").grid(row = 4, column = 0)
		Entry(new_edit, textvariable = StringVar(new_edit,value = e_time),state = "readonly").grid(row = 4, column = 1)
		Label(new_edit, text = "New Time").grid(row = 5, column = 0)
		newtime_entry = Entry(new_edit)
		newtime_entry.grid(row = 5, column = 1)

		butt=Button(new_edit, text = "Save Changes", cursor = "hand2",command = lambda:edit_record(newdate_entry.get(),e_date,newrem_entry.get(),e_rem,newtime_entry.get(),e_time))
		butt.grid(row = 6, column = 1)
		new_edit.mainloop()

	def edit_record(newdate_entry,e_date,newrem_entry,e_rem,newtime_entry,e_time):
		global new_edit
		query = "UPDATE reminder SET datee = ?, reminder = ?,time = ? WHERE datee =? AND reminder=? AND time = ?"
		parameters = (newdate_entry,newrem_entry, newtime_entry,e_date,e_rem,e_time)
		run_query(query,parameters)
		new_edit.destroy()
		display["text"] = "Record {} has been updated to {}".format(e_rem,newrem_entry)
		view_record()

	def help():
		messagebox.showinfo("Help","This is Dean Winchester and I need your help")

	#-----------FRAMES----------------#

	frame = LabelFrame(rem, bg = "#37dedb", bd = 3,padx = 20, pady = 50)
	frame.grid(row = 1, column = 0, sticky = N, padx = 40, pady = 20)


	#-----------IMAGES-----------------#

	img = PhotoImage(file = "C:\\Icons\\rem.png")
	img_label = Label(rem, image = img, height = 220)
	img_label.grid(row = 0, column = 0, padx = 20, pady = 20)

	img1 = PhotoImage(file = "C:\\Icons\\rem1.png")
	img1_label = Label(rem, image = img1, height = 220)
	img1_label.grid(row = 0, column = 1, padx = 20, pady = 20, sticky=E)

	#----------LABELS----------------------------

	date_label = Label(frame, text = "Date",padx = 20, pady = 10, font = "Garamond 15 bold italic", bg = "#37dedb")
	date_label.grid(row = 0, column = 1, sticky = N)

	rem_label = Label(frame, text = "Reminder",padx = 20, pady = 10,font = "Garamond 15 bold italic", bg = "#37dedb")
	rem_label.grid(row = 1, column = 1, sticky = N)

	time_label = Label(frame, text = "Time",padx = 20, pady = 10,font = "Garamond 15 bold italic", bg = "#37dedb")
	time_label.grid(row = 2, column = 1, sticky = N)


	#----------ENTRIES----------------------------#

	date_text = StringVar()
	date_entry = DateEntry(frame, textvariable = date_text)
	date_entry.grid(row = 0, column = 2,padx = 20, pady = 10)

	rem_text = StringVar()
	rem_entry = Entry(frame, textvariable = rem_text, width = 40)
	rem_entry.grid(row = 1, column = 2,padx = 20, pady = 10)

	time_text = StringVar()
	time_entry = Entry(frame, textvariable = time_text)
	time_entry.grid(row = 2, column = 2,padx = 20, pady = 10)


	add_but = Button(frame, cursor = "hand2",text = "Add Reminder",font = "Garamond 15 bold italic", bg = "#37dedb", command = add_record)
	add_but.grid(row = 3, column = 2,padx = 20, pady = 20)

	display = Label(frame, text = "", fg = "blue", bg = "#37dedb",font = "Garamond 13 bold italic")
	display.grid(row = 5, column = 2)

	#-----------------TREEVIEW------------------------#

	tree = ttk.Treeview(rem, height = 16, column = ["","",""])
	tree.grid(row = 1, column = 1, columnspan = 3, sticky = W)

	style = ttk.Style()
	style.configure("Treeview.Heading", font = ("Garamond 13 bold italic"))
	style.configure("Treeview", font= ("Arial 8 bold italic"))

	tree.heading("#0", text = "ID")
	tree.column("#0", width = 80)

	tree.heading("#1", text = "Date")
	tree.column("#1", width = 120)

	tree.heading("#2", text = "Reminder")
	tree.column("#2", width = 200)

	tree.heading("#3", text = "Time")
	tree.column("#3", width = 120)

	#-----------------MENUS AND SUBMENUS--------------

	chooser = Menu()
	itemone = Menu()

	chooser.add_cascade(label = "File",menu = itemone)
	chooser.add_cascade(label = "Add", command = add_record)
	chooser.add_cascade(label = "Delete", command = delete_record)
	chooser.add_cascade(label = "Edit", command = edit_box)
	chooser.add_cascade(label = "Help", command = help)
	chooser.add_cascade(label = "Exit", command = rem.destroy)

	itemone.add_command(label = "Add Reminder", command = add_record)
	itemone.add_command(label = "Delete Reminder", command = delete_record)
	itemone.add_command(label = "Edit Reminder", command = edit_box)
	itemone.add_command(label = "Help", command = help)
	itemone.add_command(label = "Exit", command = rem.destroy)

	rem.config(menu = chooser)
	view_record()

	#--------------------TIME AND DATE----------------#
	def tick():
		d = datetime.datetime.now()
		mydate = "{:%B %d %Y}".format(d)
		mytime = time.strftime("%I:%M:%S%p")
		lblInfo.config(text = (mytime +"\t" + "\t" + mydate))
		lblInfo.after(200,tick)
	lblInfo = Label(rem, font = "arial 20 bold", fg = "dark blue", bg = "#d4b09b")
	lblInfo.grid(row = 6, column = 0, columnspan = 3, pady = 25)
	tick()


	rem.mainloop()






def todolist():
	global tree
	todo = Toplevel(root)
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

		Button(new_edit, text = "Save Changes",cursor = "hand2", command = lambda:edit_record(new_date.get(),date_text,new_day.get(),day_text,new_todo.get(),todo_text,new_status.get(),status_text)).grid(row = 8, column = 1, sticky = W)

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

	add_but = Button(frame, text = "Add Record", cursor = "hand2",bg = "#dbb986", font = "Arial 10 bold italic", fg = "black",command = add_record)
	add_but.grid(row = 4, column = 2, pady = 10)

	#-------------------POP-UP DISPLAY----------------

	display = Label(frame,text = "", fg = "green",bg = "#dbb986")
	display.grid(row = 5, column = 2)

	#--------------------TREEVIEW----------------------

	tree = ttk.Treeview(todo, height = 17, column = ["","","",""])
	tree.grid(row = 6, column = 0, columnspan = 4, padx = 20)

	#----------------TREEVIEW HEADERS AND COLUMNS-----------
	
	style = ttk.Style()
	style.configure("Treeview.Heading", font= ("Arial 13 bold italic"))
	style.configure("Treeview", font= ("Arial 8 bold italic"))

	tree.heading("#0", text = "ID")
	tree.column("#0", width = 50)

	tree.heading("#1", text = "Date")
	tree.column("#1", width = 70)

	tree.heading("#2", text = "Day")
	tree.column("#2", width = 80)

	tree.heading("#3", text = "To - do List")
	tree.column("#3", width = 350)

	tree.heading("#4", text = "Status")
	tree.column("#4", width = 100)

	#-----------------MENU AND SUBMENUS---------------
	chooser = Menu()
	itemone = Menu()
	chooser.add_cascade(label = "File", menu = itemone)
	chooser.add_cascade(label = "Add",command = add_record)
	chooser.add_cascade(label = "Delete", command = delete_record)
	chooser.add_cascade(label = "Edit", command = edit_box)
	chooser.add_separator()
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

def pa_window():
	global root
	root = Tk()
	root.geometry("1150x700")
	root.title("Personal Assistant Delloitte")
	root.configure(background = "#a7cfad")


							#FONTS
	label_fonts = font.Font(family = "Helveta", slant = 'italic', weight = 'bold', size = 20)

							#FRAMES

	frame = tk.LabelFrame(root, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 1, column = 0, rowspan = 5, columnspan = 2, padx = 10, pady = 10)

	frame1 = tk.LabelFrame(root, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame1.grid(row = 1, column = 3, rowspan = 5)
		

							#IMAGE

	b_image = ImageTk.PhotoImage(Image.open("C:\\Icons\\ppa.png"))
	b_image_label = Label(image = b_image, width = 300, height = 200)
	b_image_label.grid(row = 1, column = 2)


	bi_image = ImageTk.PhotoImage(Image.open("C:\\Icons\\pa5.png"))
	bi_image_label = Label(image = bi_image, width = 300, height = 200)
	bi_image_label.grid(row = 1, column = 4, padx = 60, pady = 20)


	
							#LABELS

	intro_label = Label(root, text = "Personal Assistant Tool - Kit", fg= "#c75071", bg = "#a7cfad", font = "Verdana 25 bold italic")
	intro_label.grid(row = 0, column = 2)

							#LEFT FRAME

	but_todolist = Button(frame, text = "To-do List", cursor = "hand2",font = "Rockwell 13 bold italic", width = "20", height = "2", command = todolist)
	but_todolist.grid(row = 1, column = 0, padx = 10, pady = 10)

	but_reminders = Button(frame, text = "Reminders", cursor = "hand2",width = "20", height = "2", font = "Rockwell 13 bold italic", command = reminder)
	but_reminders.grid(row = 2, column = 0, padx = 10, pady = 10)

	but_presentations = Button(frame, text = "Presentations", cursor = "hand2",width = "20", height = "2", font = "Rockwell 13 bold italic", command = presentation)
	but_presentations.grid(row = 3, column = 0, pady = 10)

	but_jd = Button(frame, text = "Staff Job Descriptions", cursor = "hand2",width = "20", height = "2", font = "Rockwell 13 bold italic", command = job_description)
	but_jd.grid(row = 4, column = 0, pady = 10)


							#RIGHT FRAME

	but_meeting = Button(frame1, text = "Meeting Schedule", cursor = "hand2", width = "20", height = "2", font = "Rockwell 13 bold italic", command = meeting_schedule)
	but_meeting.grid(row = 1, column = 3, padx = 10, pady = 10)

	but_min_meeting = Button(frame1, text = "Minutes of Meeting", cursor = "hand2",width = "20", height = "2", font = "Rockwell 13 bold italic",command = minutes)
	but_min_meeting.grid(row = 2, column = 3, padx = 10, pady = 10)

	but_calls = Button(frame1, text = "Call Records", width = "20", cursor = "hand2",height = "2", font = "Rockwell 13 bold italic", command=call_record)
	but_calls.grid(row = 3, column = 3, padx = 10, pady = 10)

	but_org_chart = Button(frame1, text = "Organizational Chart", state = "disabled", width = "20", height = "2", font = "Rockwell 13 bold italic")
	but_org_chart.grid(row = 4, column = 3, padx = 10, pady = 10)

	exit_but = Button(root, text = "Exit Window", cursor = "hand2",command = root.destroy, width = 20, bg = "red", font = "Rockwell 13 bold italic")
	exit_but.grid(row = 6, column = 2, padx = (10,0), pady = (10,0))
	root.mainloop()




	
pa_window()