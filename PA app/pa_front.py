from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox
from tkcalendar import *



def call_record():
	call = Toplevel(root)
	call.geometry("1300x1300")
	#call.configure(background = "")
	call.title("Call Records")
	canvas = Canvas(call, width = 1800, height = 1200)
	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\clock.png"))
	canvas.create_image(0,0,anchor = NW, image = img)
	#canvas.grid(row = 0, column = 0)
	import call_back

	
				#FUNCTIONS

	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		entry_call.delete(0,END)
		entry_call.insert(END,selected_tuple[1])

		entry_callno.delete(0,END)
		entry_callno.insert(END,selected_tuple[2])

		entry_reason.delete(0,END)
		entry_reason.insert(END,selected_tuple[3])

		entry_calltime.delete(0,END)
		entry_calltime.insert(END,selected_tuple[4])

		entry_calldate.delete(0,END)
		entry_calldate.insert(END,selected_tuple[5])


	def view_command():
		listbox.delete(0,END)
		for row in call_back.view_call():
			listbox.insert(END,row)

	def insert_command():
		call_back.insert_call(caller_text.get(),callno_text.get(),reason_text.get(),calltime_text.get(),calldate_text.get())
		listbox.delete(0,END)
		listbox.insert(END,(caller_text.get(),callno_text.get(),reason_text.get(),calltime_text.get(),calldate_text.get()))
		view_command()
		display["text"] = "Record has been added"


	def update_command():
		call_back.update_call(selected_tuple[0],caller_text.get(),callno_text.get(),reason_text.get(),calltime_text.get(),calldate_text.get())
		view_command()
		display["text"] = "Record has been updated"


	def delete_command():
		call_back.delete_call(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_command()

	def clear():
		entry_call.delete(0,END)
		entry_callno.delete(0,END)
		entry_reason.delete(0,END)
		entry_calltime.delete(0,END)
		entry_calldate.delete(0,END)

				#FRAME

	frame = LabelFrame(call, width = 60, height = 30, padx = 20, pady = 10, bg = "#204524")
	frame.grid(row = 1, column = 0, padx = 20, pady = 6, sticky = W)

	frame1 = LabelFrame(call, width = 60, height = 20, padx = 20, pady = 20, fg = "#204524", bg = "cyan")
	frame1.grid(row = 2, column = 0, sticky = W, padx = 20, pady = 20)

				#IMAGE

	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\call.png"))
	img_label = Label(call,image = img, height = 320)
	img_label.grid(row = 1, column = 1,pady = 5)

	img1 = ImageTk.PhotoImage(Image.open("C:\\Icons\\forward1.png"))
	img_label1 = Label(call,image = img1)
	img_label1.grid(row = 2, column = 0, sticky = W, padx = (320,0))



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
	entry_calldate = DateEntry(frame, textvariable = calldate_text, width = 50, bd = 3)
	entry_calldate.grid(row = 5, column = 1)

				#BUTTONS

	but_add = Button(frame, text = "Add Call Record", font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10  ,bg = "#204524", bd = 3, command = insert_command)
	but_add.grid(row = 6, column = 1, pady = 12)

	display = Label(frame, text = "", fg = "blue",font = "Times 15 bold italic")
	display.grid(row = 7, column = 1)



	but_view = Button(frame1, text = "View Call Records", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524", command = view_command)
	but_view.grid(row = 8, column = 0, pady = 5)

	but_edit = Button(frame1, text = "Edit Call Record", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524" , command = update_command)
	but_edit.grid(row = 9, column = 0, pady = 5)

	but_del = Button(frame1, text = "Delete Call Record", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524" , command = delete_command)
	but_del.grid(row = 10, column = 0, pady = 5)

	clear_entry = Button(frame1, text = "Clear Entry", width = 15, font = "Times 15 bold italic", fg = "cyan", padx = 10, pady = 10, bg= "#204524" , command = clear)
	clear_entry.grid(row = 11, column = 0, pady = 5)

	close_window = Button(call, text = "Close Window", font = "Times 15 bold italic", fg = "white", bg = "red", padx = 10, pady = 10 , command = call.destroy)
	close_window.grid(row = 8, column = 0,padx =(450,0), pady = 10)


	listbox = Listbox(call, width = 85, height = 20, bd= 5)
	listbox.grid(row = 2, column = 1, sticky=W, pady = 5)
	view_command()

	listbox.bind("<<ListboxSelect>>",get_selected_rows)

	call.mainloop()


def minutes():
	minn = Toplevel(root)
	minn.geometry("1400x1000")
	minn.title("Minutes of Meeting")
	minn.configure(background = "#8499ba")
	import min_back


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
		view_command()
		display["text"] = "Record has been added"

		
	def update_command():
		min_back.update(selected_tuple[0], top_text.get(),create_text.get(),date_text.get(),time_text.get(),min_text)
		view_command()
		display["text"] = "Record has been updated"


	def delete_command():
		min_back.delete(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_command()

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
	date_entry = DateEntry(frame, textvariable = date_text, width = 50, bd = 4)
	date_entry.grid(row = 4, column = 1, sticky = N, pady = 10)

	time_text = StringVar()
	time_entry = Entry(frame, textvariable = time_text, width = 50, bd = 4)
	time_entry.grid(row = 5, column = 1, sticky = N, pady = 10)

	textbox = Text(frame, width = 40, height = 22, bd = 4)
	textbox.grid(row = 1, column = 1, sticky = N, padx = 2)

	listbox = Listbox(minn,width = 100, height = 20, bd = 8)
	listbox.grid(row = 2, column = 1, pady = 15, padx = 30)
	view_command()
	listbox.bind("<<ListboxSelect>>", get_selected_rows)

	minn.mainloop()




def meeting_schedule():
	ms = Toplevel(root)
	ms.geometry("1400x1000")
	ms.title("Meeting Schedule")
	ms.configure(background = "#8499ba")
	import meet_back

			#FUNCTIONS

	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)
		meet_entry.delete(0,END)
		meet_entry.insert(END,selected_tuple[1])

		meet_entry1.delete(0,END)
		meet_entry1.insert(END,selected_tuple[2])

		reason_entry.delete(0,END)
		reason_entry.insert(END,selected_tuple[3])

		time_entry.delete(0,END)
		time_entry.insert(END,selected_tuple[4])

		date_entry.delete(0,END)
		date_entry.insert(END,selected_tuple[5])



	def view_command():
		listbox.delete(0,END)
		for row in meet_back.view_ms():
			listbox.insert(END,row)

	def insert_command():
		meet_back.insert_ms(meet_text.get(),meet_text1.get(),reason_text.get(),time_text.get(),date_text.get())
		listbox.delete(0,END)
		listbox.insert(END,(meet_text.get(),meet_text1.get(),reason_text.get(),time_text.get(),date_text.get()))
		view_command()
		display["text"] = "Record has been added"

	def update():
		meet_back.update_ms(selected_tuple[0], meet_text.get(), meet_text1.get(), reason_text.get(), time_text.get(), date_text.get())
		view_command()
		display["text"] = "Record has been updated"

	def delete_command():
		meet_back.delete_ms(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_command()

	def clear_entry():
		meet_entry.delete(0,END)
		meet_entry1.delete(0,END)
		reason_entry.delete(0,END)
		time_entry.delete(0,END)
		date_entry.delete(0,END)


						#FRAMES

	frame_label = LabelFrame(ms, padx = 15, pady = 10, bg = "#7f9494", width = 20, height= 20, relief = SUNKEN)
	frame_label.grid(row = 1, column = 0, columnspan = 1)

	frame_but = LabelFrame(ms, padx = 15, pady = 10, bg = "#7f9494", width = 20, height= 20, relief = SUNKEN)
	frame_but.grid(row = 8, column = 0, columnspan = 1, sticky = W)


						#IMAGE

	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\meet1.png"))
	img_lab = Label(ms, image = img)
	img_lab.grid(row = 1, column = 1, padx = (40,0))


						#LABELS

	meet_label = Label(ms, text = "Meeting Schedule", font = "Rockwell 30 bold italic underline", bg = "#8499ba", fg = "#9c3030", padx = 10, pady = 10 )
	meet_label.grid(row = 0, column = 0)

	meet_label_for = Label(frame_label, text = "Book Meeting For", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_for.grid(row = 1, column = 0)

	meet_label_by = Label(frame_label, text = "Meeting Booked By", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_by.grid(row = 2, column = 0)

	meet_label_reason = Label(frame_label, text = "Reason for Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_reason.grid(row = 3, column = 0)

	meet_label_time = Label(frame_label, text = "Time For Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_time.grid(row = 4, column = 0)

	meet_label_date = Label(frame_label, text = "Date For Meeting", font = "Rockwell 15 bold italic", bg = "#7f9494", fg = "#9c3030", padx = 10, pady = 10)
	meet_label_date.grid(row = 5, column = 0)

	manage_label = Label(ms, text = "Manage Meeting Schedule", font = "Rockwell 30 bold italic underline", bg = "#8499ba", fg = "#9c3030", padx = 10, pady = 10)
	manage_label.grid(row = 7, column = 0)

				#ENTRY

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
	date_entry = DateEntry(frame_label, textvariable = date_text, width = 50, bd = 3)
	date_entry.grid(row = 5, column = 1)



			#BUTTONS

	but_add = Button(frame_label, text = "Add Schedule", bd = 3, bg = "#38b9c2", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic", command = insert_command)
	but_add.grid(row = 6, column = 1, padx = 10, pady = 10)

	display = Label(frame_label, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 7, column = 1)


	but_view = Button(frame_but, text = "View Schedules", bd = 3, bg = "#7f9494", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic", command = view_command)
	but_view.grid(row = 8, column = 1, padx = 10, pady = 10)

	but_edit = Button(frame_but, text = "Modify Schedule", bd = 3, bg = "#7f9494", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic",command = update)
	but_edit.grid(row = 9, column = 1, padx = 10, pady = 10)

	but_del = Button(frame_but, text = "Delete Schedule", bd = 3, bg = "#7f9494", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic", command =  delete_command)
	but_del.grid(row = 10, column = 1, padx = 10, pady = 10)

	but_clear = Button(frame_but, text = "Clear Entries", bd = 3, bg = "#7f9494", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic", command = clear_entry)
	but_clear.grid(row = 11, column = 1, padx = 10, pady = 10)

	but_close = Button(ms, text = "Close Window", bd = 3, bg = "#38b9c2", fg = "#9c3030",width = 13, font = "Rockwell 12 bold italic", command = ms.destroy)
	but_close.grid(row = 8, column = 2, sticky = SW)


				#LISTBOX

	listbox = Listbox(ms, width = 100, height = 20, bd = 8)
	listbox.grid(row = 8, column = 1, sticky = W)
	view_command()

	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	ms.mainloop()



					#JOB DESCRIPTION

def job_description():
	global jd
	jd = Toplevel(root)
	jd.geometry("1400x1500")
	jd.configure(background = "#a2e0f5")
	jd.title("Staff Job Description")
	import jd_back


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

	jd_pa = Button (frame, text = "Personal assistant", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#132363", width = 25, font = "Florence 18 bold italic", command = personal_assistant)
	jd_pa.grid(row = 2, column = 0, pady = 2)

	jd_acc = Button (frame, text = " Accountant", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic", command = accountant)
	jd_acc.grid(row = 3, column = 0, pady = 2)

	jd_rec = Button (frame, text = "Receptionist", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic", command = receptionist)
	jd_rec.grid(row = 4, column = 0, pady = 2)

	jd_cus = Button (frame, text = "Customer Service", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic", command = customer_service)
	jd_cus.grid(row = 5, column = 0, pady = 2)

	jd_sm = Button (frame, text = "Social Media Personnel", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#ed0020",width = 25, font = "Florence 18 bold italic", command = social_media)
	jd_sm.grid(row = 6, column = 0, pady = 2)

	jd_hr = Button (frame, text = "Human Resource", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#132363",width = 25, font = "Florence 18 bold italic", command = human_resource)
	jd_hr.grid(row = 7, column = 0, pady = 2)

	jd_bd = Button (frame, text = "Business Development Officer", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic", command = business_development)
	jd_bd.grid(row = 8, column = 0, pady = 2)

	jd_op = Button (frame, text = "Operations Manager", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic", command = operations_manager)
	jd_op.grid(row = 9, column = 0, pady = 2)

	jd_sec = Button (frame, text = "Security Personnel", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic", command = security)
	jd_sec.grid(row = 10, column = 0, pady = 2)

	jd_close = Button(jd, text = "Close Window", relief = RAISED, bd = 3, bg = "red", fg = "white",width = 15, font = "Florence 15 bold italic", command = jd.destroy)
	jd_close.grid(row = 11, column = 2)

	jd.mainloop()


						#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#PERSONAL ASSISTANT

def personal_assistant():
	global jd
	pa = Toplevel(jd)
	pa.geometry("1400x1500")
	pa.configure(background = "#a2e0f5")
	pa.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		pa_entry.delete(0,END)
		pa_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_pa():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_pa(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		insert_jd()
		display["text"] = "Record has been added"


	def delete_jd():
		jd_back.delete_pa(selected_tuple[0])
		display["text"] = "Record has been deleted"

		insert_jd()

	def update_jd():
		jd_back.update_pa(selected_tuple[0], entry_text.get())
		insert_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		pa_entry.delete(0,END)


			#LABELS
	pa_label = Label(pa, text = "Personal Assistant Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	pa_label.grid(row = 0, column = 1)

	pa_jd = Label(pa, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	pa_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	pa_entry = Entry(pa, textvariable = entry_text, width = 70, bd = 4)
	pa_entry.grid(row = 1, column = 1)

	pa_add = Button(pa, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	pa_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(pa, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	pa_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	pa_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	pa_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	pa_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	pa_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	pa_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	pa_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	pa_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	pa_close = Button(pa, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	pa_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(pa)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(pa, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, pady = 30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	pa.mainloop()



				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#ACCOUNTANT

def accountant():
	global jd
	acc = Toplevel(jd)
	acc.geometry("1400x1500")
	acc.configure(background = "#a2e0f5")
	acc.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		acc_entry.delete(0,END)
		acc_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_acc():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_acc(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		display["text"] = "Record has been added"

	def delete_jd():
		jd_back.delete_acc(selected_tuple[0])
		display["text"] = "Record has been deleted"
		insert_jd()

	def update_jd():
		jd_back.update_acc(selected_tuple[0], entry_text.get())
		insert_jd()
		display["text"] = "Record has been added"

	def clear_entry():
		pa_entry.delete(0,END)


			#LABELS
	acc_label = Label(acc, text = "Accountant Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	acc_label.grid(row = 0, column = 1)

	acc_jd = Label(acc, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	acc_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	acc_entry = Entry(acc, textvariable = entry_text, width = 70, bd = 4)
	acc_entry.grid(row = 1, column = 1)

	acc_add = Button(acc, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	acc_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(acc, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	acc_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	acc_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	acc_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	acc_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	acc_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	acc_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	acc_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	acc_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	acc_close = Button(acc, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	acc_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(acc)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(acc, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx = 30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	acc.mainloop()



				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#RECEPTIONIST

def receptionist():
	global jd
	rec = Toplevel(jd)
	rec.geometry("1400x1500")
	rec.configure(background = "#a2e0f5")
	rec.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		rec_entry.delete(0,END)
		rec_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_rec():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_rec(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"

	def delete_jd():
		jd_back.delete_rec(selected_tuple[0])
		display["text"] = "Record has been deleted"
		view_jd()

	def update_jd():
		jd_back.update_rec(selected_tuple[0], entry_text.get())
		insert_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		rec_entry.delete(0,END)


			#LABELS
	rec_label = Label(rec, text = "Receptionist Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	rec_label.grid(row = 0, column = 1)

	rec_jd = Label(rec, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	rec_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	rec_entry = Entry(rec, textvariable = entry_text, width = 70, bd = 4)
	rec_entry.grid(row = 1, column = 1)

	rec_add = Button(rec, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	rec_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(rec, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	rec_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	rec_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	rec_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	rec_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	rec_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	rec_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	rec_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	rec_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	rec_close = Button(rec, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	rec_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(rec)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(rec, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx = 30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	rec.mainloop()




				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#CUSTOMER SERVICE

def customer_service():
	global jd
	cus = Toplevel(jd)
	cus.geometry("1400x1500")
	cus.configure(background = "#a2e0f5")
	cus.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		cus_entry.delete(0,END)
		cus_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_cus():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_cus(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"

	def delete_jd():
		jd_back.delete_cus(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_jd()

	def update_jd():
		jd_back.update_cus(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		cus_entry.delete(0,END)


			#LABELS
	cus_label = Label(cus, text = "Customer Care Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	cus_label.grid(row = 0, column = 1)

	cus_jd = Label(cus, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	cus_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	cus_entry = Entry(cus, textvariable = entry_text, width = 70, bd = 4)
	cus_entry.grid(row = 1, column = 1)

	cus_add = Button(cus, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	cus_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(cus, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	cus_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	cus_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	cus_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	cus_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	cus_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	cus_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	cus_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	cus_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	cus_close = Button(cus, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	cus_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(cus)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(cus, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx = 30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	cus.mainloop()





				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#SOCIAL MEDIA

def social_media():
	global jd
	sm = Toplevel(jd)
	sm.geometry("1400x1500")
	sm.configure(background = "#a2e0f5")
	sm.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		sm_entry.delete(0,END)
		sm_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_sm():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_sm(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"


	def delete_jd():
		jd_back.delete_sm(selected_tuple[0])
		display["text"] = "Record has been deleted"
		view_jd()

	def update_jd():
		jd_back.update_sm(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"


	def clear_entry():
		sm_entry.delete(0,END)


			#LABELS

	sm_label = Label(sm, text = "Social Media Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	sm_label.grid(row = 0, column = 1)

	sm_jd = Label(sm, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	sm_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	sm_entry = Entry(sm, textvariable = entry_text, width = 70, bd = 4)
	sm_entry.grid(row = 1, column = 1)

	sm_add = Button(sm, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	sm_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(sm, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	sm_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	sm_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	sm_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	sm_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	sm_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	sm_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	sm_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	sm_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	sm_close = Button(sm, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	sm_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(sm)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(sm, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx=30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	sm.mainloop()






				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#HUMAN RESOURCE

def human_resource():
	global jd
	hr = Toplevel(jd)
	hr.geometry("1400x1500")
	hr.configure(background = "#a2e0f5")
	hr.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		hr_entry.delete(0,END)
		hr_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_hr():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_hr(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"


	def delete_jd():
		jd_back.delete_hr(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_jd()

	def update_jd():
		jd_back.update_hr(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"


	def clear_entry():
		hr_entry.delete(0,END)


			#LABELS
	hr_label = Label(hr, text = "Human Resource Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	hr_label.grid(row = 0, column = 1)

	hr_jd = Label(hr, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	hr_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	hr_entry = Entry(hr, textvariable = entry_text, width = 70, bd = 4)
	hr_entry.grid(row = 1, column = 1)

	hr_add = Button(hr, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	hr_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(hr, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	hr_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	hr_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	hr_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	hr_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	hr_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	hr_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	hr_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	hr_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	hr_close = Button(hr, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	hr_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(hr)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(hr, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx=30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	hr.mainloop()


				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#BUSINESS DEVELOPMENT

def business_development():
	global jd
	bd = Toplevel(jd)
	bd.geometry("1400x1500")
	bd.configure(background = "#a2e0f5")
	bd.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		bd_entry.delete(0,END)
		bd_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_bd():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_bd(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"


	def delete_jd():
		jd_back.delete_bd(selected_tuple[0])
		display["text"] = "Record has been deleted"
		view_jd()

	def update_jd():
		jd_back.update_bd(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		bd_entry.delete(0,END)


			#LABELS
	bd_label = Label(bd, text = "Business Development Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	bd_label.grid(row = 0, column = 1)

	bd_jd = Label(bd, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	bd_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	bd_entry = Entry(bd, textvariable = entry_text, width = 70, bd = 4)
	bd_entry.grid(row = 1, column = 1)

	bd_add = Button(bd, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	bd_add.grid(row = 2, column = 1, pady = 20)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)

	frame = LabelFrame(bd, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	bd_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	bd_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	bd_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	bd_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	bd_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	bd_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	bd_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	bd_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	bd_close = Button(bd, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	bd_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(bd)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(bd, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx=30)
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)
	view_jd()

	bd.mainloop()





				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#OERATIONS MANAGER

def operations_manager():
	global jd
	op = Toplevel(jd)
	op.geometry("1400x1500")
	op.configure(background = "#a2e0f5")
	op.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		op_entry.delete(0,END)
		op_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_op():
			listbox.insert(END,row)

	def insert_jd():
		jd_back.add_op(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"

	def delete_jd():
		jd_back.delete_op(selected_tuple[0])
		display["text"] = "Record has been deleted"

		view_jd()

	def update_jd():
		jd_back.update_op(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		op_entry.delete(0,END)


			#LABELS

	op_label = Label(op, text = "Operations Manager Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	op_label.grid(row = 0, column = 1)

	op_jd = Label(op, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	op_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	op_entry = Entry(op, textvariable = entry_text, width = 70, bd = 4)
	op_entry.grid(row = 1, column = 1)

	op_add = Button(op, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	op_add.grid(row = 2, column = 1, pady = 20)


	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(op, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	op_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	op_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	op_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	op_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	op_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	op_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	op_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	op_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	op_close = Button(op, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	op_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(op)
	sb.grid(row = 3, column = 2)
	listbox = Listbox(op, width = 90, height = 27, bd = 6)
	listbox.grid(row = 3, column = 1, padx=30)
	view_jd()

	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)

	op.mainloop()




				#DAUGHTER WINDOWS OF JOB DESCRIPPTION
						#SECURITY

def security():
	global jd
	sec = Toplevel(jd)
	sec.geometry("1400x1500")
	sec.configure(background = "#a2e0f5")
	sec.title("Staff Job Description")
	import jd_back


			#FUNCTIONS
	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		sec_entry.delete(0,END)
		sec_entry.insert(END,selected_tuple[1])

	def view_jd():
		listbox.delete(0,END)
		for row in jd_back.view_sec():
			listbox.insert(END,row)
		view_jd()

	def insert_jd():
		jd_back.add_sec(entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,entry_text.get())
		view_jd()
		display["text"] = "Record has been added"

	def delete_jd():
		jd_back.delete_sec(selected_tuple[0])
		display["text"] = "Record has been deleted"
		view_jd()

	def update_jd():
		jd_back.update_sec(selected_tuple[0], entry_text.get())
		view_jd()
		display["text"] = "Record has been updated"

	def clear_entry():
		sec_entry.delete(0,END)


			#LABELS
	sec_label = Label(sec, text = "Operations Manager Job Description", font = "Cambria 30 bold italic underline", bg = "#a2e0f5", fg = "black", pady = 10)
	sec_label.grid(row = 0, column = 1)

	sec_jd = Label(sec, text="Enter job description", font = "Perpetua 15 bold italic", bd = 3, bg = "#a2e0f5", fg = "black", pady = 10)
	sec_jd.grid(row = 1, column = 0, padx = 10, pady = 10)

			#ENTRY

	entry_text = StringVar()
	sec_entry = Entry(sec, textvariable = entry_text, width = 70, bd = 4)
	sec_entry.grid(row = 1, column = 1)

	sec_add = Button(sec, text = "Add Job Description", bd = 3, bg = "#e681a2", width = 15, height = 1, font = "Garamond 11 bold italic", command = insert_jd)
	sec_add.grid(row = 2, column = 1, pady = 20)


	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 3, column = 1)


	frame = LabelFrame(sec, padx = 15, pady = 45, bg = "#BDBDBD", width = 200, height= 50, relief = SUNKEN)
	frame.grid(row = 3, column = 0, columnspan = 1, rowspan = 4, padx = 30)

			#BUTTONS

	sec_view = Button(frame, text = "View Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = view_jd)
	sec_view.grid(row = 3, column = 0, padx = 20, pady = 20)

	sec_delete = Button(frame, text = "Delete Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = delete_jd)
	sec_delete.grid(row = 4, column = 0, padx = 20, pady = 20)

	sec_update = Button(frame, text = "Update Job Description", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = update_jd)
	sec_update.grid(row = 5, column = 0, padx = 20, pady = 20)

	sec_clear = Button(frame, text = "Clear Entry Box", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = clear_entry)
	sec_clear.grid(row = 6, column = 0, padx = 20, pady = 20)

	sec_close = Button(sec, text = "Close Window", bd = 3, bg = "#cc3333", fg = "white", width = 20, height = 2, font = "Garamond 11 bold italic", command = jd.destroy)
	sec_close.grid(row = 7, column = 1, padx = 20, pady = 20)


	sb = Scrollbar(sec)   
	sb.grid(row = 3, column = 2)
	listbox = Listbox(sec, width = 90, height = 27, bd = 6) 
	listbox.grid(row = 3, column = 1, padx=30)
	view_jd()
	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)

	sec.mainloop()




		
				#PRESENTATION TOPIC

def presentation_command():

	pres = Toplevel(root)
	pres.geometry("1400x1500")
	pres.configure(background = "#4d5d75")
	pres.title("Presentations")
	import pres_back


					#FUNCTIONS

	def view_pres():
		listbox.delete(0,END)
		for row in pres_back.view():
			listbox.insert(END,row)


	def search_pres():
		listbox.delete(0,END)
		for row in pres_back.search(pres_text.get(),create_text.get(), date_text.get(), status_text.get()):
			listbox.insert(END,row)

	def insert_pres():
		pres_back.insert(pres_text.get(),create_text.get(), date_text.get(), status_text.get())
		listbox.delete(0,END)
		listbox.insert(END,(pres_text.get(),create_text.get(), date_text.get(), status_text.get()))
		view_pres()
		display["text"] = "Record has been added"

	def delete_pres():
		pres_back.delete(selected_tuple[0])
		view_pres()
		display["text"] = "Record has been deleted"

	def update_pres():
		pres_back.update(selected_tuple[0],pres_text.get(),create_text.get(), date_text.get(), status_text.get())
		view_pres()
		display["text"] = "Record has been updated"

	def clear_entry_command():
		pres_ent.delete(0,END)
		create_ent.delete(0,END)
		date_ent.delete(0,END)
		status_ent.delete(0,END)

	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		pres_ent.delete(0,END)
		pres_ent.insert(END,selected_tuple[1])

		create_ent.delete(0,END)
		create_ent.insert(END,selected_tuple[2])

		date_ent.delete(0,END)
		date_ent.insert(END,selected_tuple[3])
				
		status_ent.delete(0,END)
		status_ent.insert(END,selected_tuple[4])


					#FRAMES

	frame = LabelFrame(pres, padx = 15, pady = 5, bg = "#BDBDBD", width = 200, height= 50)
	frame.grid(row = 2, column = 0, rowspan = 10, columnspan = 2, padx = 10, pady = 5)


					#LABELS

	label_header = Label(pres, text= "Power Point Presentation Gallery",  font = "Courier 20 bold italic underline", bg = "#4d5d75", fg = "white", pady = 10)
	label_header.grid(row = 0, column = 0, padx = 20)

	image = ImageTk.PhotoImage(Image.open("C:\\Icons\\pres.png"))
	image_label = Label(pres, image = image, width = 450, height = 250)
	image_label.grid(row = 1, column = 0,pady = 6)

	image1 = ImageTk.PhotoImage(Image.open("C:\\Icons\\goo.png"))
	image1_label = Label(pres, image = image1, width = 100, height = 146)
	image1_label.grid(row = 2, column = 2)


	pres_label = Label(frame, text = "Presentation Topic", font = "Garamond 15 bold italic")
	pres_label.grid(row = 2, column = 0, pady = (20,20), ipadx = 10, ipady = 5)

	create_label = Label(frame, text = "Created by", font = "Garamond 15 bold italic")
	create_label.grid(row = 4, column = 0, pady = 20, ipadx = 10, ipady = 5)

	date_label = Label(frame, text = "Date presented", font = "Garamond 15 bold italic")
	date_label.grid(row = 6, column = 0, pady = 20, ipadx = 10, ipady = 5)

	stat_label = Label(frame, text = "Status", font = "Garamond 15 bold italic")
	stat_label.grid(row = 8, column = 0, pady = 20, ipadx = 10, ipady = 5)

	add_butt = Button(frame, text = "Add Presentation", font = "Consolas 10 bold italic", bg = "#218a5e", width = 30, command = insert_pres)
	add_butt.grid(row = 10, column = 0, pady = 20, ipadx = 10, ipady = 5)


					#ENTRY

	pres_text = StringVar()
	pres_ent = Entry(frame, textvariable = pres_text, width = 50, bd = 3)
	pres_ent.grid(row = 3, column = 0)

	create_text = StringVar()
	create_ent = Entry(frame, textvariable = create_text, width = 50, bd = 3)
	create_ent.grid(row = 5, column = 0)

	date_text = StringVar()
	date_ent = DateEntry(frame, textvariable = date_text, width = 50, bd = 3)
	date_ent.grid(row= 7, column = 0)

	status_text = StringVar()
	status_ent = Entry(frame, textvariable = status_text, width = 50, bd = 3)
	status_ent.grid(row = 9, column = 0)

	entry_search_text = StringVar()
	entry_search = Entry(pres, textvariable = entry_search_text, width = 30, bd = 2)
	entry_search.grid(row = 0, column = 4, sticky = E)


					#BUTTONS

	but_view = Button(pres, text = "View Presentation",  bd = 3, bg = "#218a5e", width = 12, font = "papyrus 8 bold italic", command = view_pres)
	but_view.grid(row = 1, column = 2, ipadx = 5)

	but_update = Button(pres, text = "Update Presentation",  bd = 3, bg = "#218a5e", width = 15, font = "papyrus 8 bold italic", command = update_pres)
	but_update.grid(row = 1, column = 3)

	but_clear = Button(pres, text = "Clear Entry",  bd = 3, bg = "#218a5e", width = 10, font = "papyrus 8 bold italic",command = clear_entry_command)
	but_clear.grid(row = 0, column = 2)

	but_delete = Button(pres, text = "Delete Presentation", bd = 3, bg = "#218a5e", width = 12, font = "papyrus 8 bold italic", command = delete_pres)
	but_delete.grid(row = 1, column = 4, ipadx = 20)

	but_search = Button(pres, text = "Search",  bd = 3, bg = "#218a5e", width = 12, font = "papyrus 8 bold italic", command = search_pres)
	but_search.grid(row = 0, column = 3, pady = 20)

	but_close_window = Button(pres, text = "Close Window", bg = "red", width = 20, bd = 5, font = "papyrus 8 bold italic", command = pres.destroy)
	but_close_window.grid(row = 6, column = 4, pady = 10)


	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 5, column = 4)


					#LISTBOX

	listbox = Listbox(pres, width = 73, height = 27, bd = 3) 
	listbox.grid(row = 2, column = 3, padx = 20)
	view_pres()


					#SCROLLBAR

	sb = Scrollbar(pres)
	sb.grid(row = 2, column = 4, rowspan = 4)

					#CONFIURATION      

	listbox.configure(yscrollcommand = sb.set)
	sb.configure(command = listbox.yview)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)

	pres.mainloop()
  


				#REMINDERS

def reminder():
	rem = Toplevel(root)
	rem.geometry("1100x1500")
	rem.configure(background = "#d4b09b")
	rem.title("Reminders")
	import rem_back


	def clear_entry():
		rem_entry.delete(0,END)
		date_entry.delete(0,END)
		time_entry.delete(0,END)



	def get_selected_rows(event):
		global selected_tuple_reminder
		index = listbox.curselection()[0]
		selected_tuple_reminder = listbox.get(index)

		rem_entry.delete(0,END)
		rem_entry.insert(END,selected_tuple_reminder[1])

		date_entry.delete(0,END)
		date_entry.insert(END,selected_tuple_reminder[2])

		time_entry.delete(0,END)
		time_entry.insert(END,selected_tuple_reminder[3])


	def view_reminder_command():
		listbox.delete(0,END)
		for row in rem_back.view_reminder():
			listbox.insert(END,row)

	def search_reminder_command():
		listbox.delete(0,END)
		for row in rem_back.search_reminder():
			listbox.insert(END,rem_entry_text.get(), date_entry_text.get(),time_entry_text.get())

	def insert_reminder_command():
		rem_back.insert_reminder(rem_entry_text.get(), date_entry_text.get(),time_entry_text.get())
		listbox.insert(END,(rem_entry_text.get(),date_entry_text.get(),time_entry_text.get()))
		view_reminder_command()
		display["text"] = "Record has been added"

	def update_reminder_command():
		rem_back.update_reminder(selected_tuple_reminder[0], rem_entry_text.get(), date_entry_text.get(),time_entry_text.get())
		view_reminder_command()
		display["text"] = "Record has been updated"

	def delete_reminder_command():
		rem_back.delete_reminder(selected_tuple_reminder[0])
		view_reminder_command()
		display["text"] = "Record has been deleted"



	#IMAGES

	img = ImageTk.PhotoImage(Image.open("C:\\Icons\\rem.png"))
	img_label = Label(rem, image = img, width = 300, height = 100)
	img_label.grid(row = 0, column = 1, pady = 20, padx = 30)




				#LABELS

	#rem_header = Label(rem, text = "Reminders",  font = "papyrus 30 bold italic underline",  fg = "#146120", bg = "#d4b09b")
	#rem_header.grid(row = 0, column = 1, pady = 20, padx = 30)

	search_rem = Button(rem, text = "Search", font = "papyrus 10 bold italic underline",  fg = "#146120", bg = "#218a5e", command = search_reminder_command)
	search_rem.grid(row = 0, column= 2)

	rem_label = Label(rem, text = "Reminder",  font = "Garamond 10 bold italic",  fg = "#403630", bg = "#d4b09b")
	rem_label.grid(row = 1, column = 0)

	date_label = Label(rem, text = "Date",  font = "Garamond 10 bold italic",  fg = "#403630", bg = "#d4b09b")
	date_label.grid(row = 2, column = 0)

	time_label = Label(rem, text = "Time",  font = "Garamond 10 bold italic",  fg = "#403630", bg = "#d4b09b")
	time_label.grid(row = 3, column = 0)

	man_label = Label(rem, text = "Manage Reminder",  font = "papyrus 30 bold italic underline",  fg = "#146120", bg = "#d4b09b")
	man_label.grid(row = 5, column = 1, pady = 20)

				#ENTRY


	rem_entry_text = StringVar()
	rem_entry = Entry(rem, textvariable = rem_entry_text, bd = 3, width = 30)
	rem_entry.grid(row = 1, column = 1, padx = 80, pady = 20)

	date_entry_text = StringVar()
	date_entry = DateEntry(rem, textvariable = date_entry_text,  bd = 3, width = 28)
	date_entry.grid(row = 2, column = 1, padx = 10, pady = 10)

	time_entry_text = StringVar()
	time_entry = Entry(rem, textvariable = time_entry_text, bd = 3, width = 30)
	time_entry.grid(row = 3, column = 1, padx = 10, pady = 10)

	search_entry_text = StringVar()
	search_entry = Entry(rem, textvariable = search_entry_text, bd = 3, width = 30)
	search_entry.grid(row = 0, column = 3)

				#LISTBOX

	listbox = Listbox(rem, width = 100, height =20, bd = 10)
	listbox.grid(row = 8, column = 0, rowspan = 2, columnspan = 3, pady = (30,15))
	view_reminder_command()
		
				#SCROLLBAR
	sb = Scrollbar(rem)
	sb.grid(row = 6, column = 2, rowspan = 16, padx = 20)

					#CONFIGURATION AND BINDING

	sb.configure(command = listbox.yview)
	listbox.configure(yscrollcommand = sb.set)
	listbox.bind("<<ListboxSelect>>", get_selected_rows)



				#BUTTONS

	but_add_reminder = Button(rem, text = "Add Reminder", relief = RAISED, bg = "#268a21", width = 20, height = 2, font = "Garamond 13 bold italic", command = insert_reminder_command)
	but_add_reminder.grid(row = 4, column = 1, pady = 20)


	but_view_reminder = Button(rem, text = "View Reminders", relief = RAISED, bg = "#218a5e", width = 20, height = 2, font = "Garamond 13 bold italic", command = view_reminder_command)
	but_view_reminder.grid(row = 6, column = 0, padx = 30)
            
	but_update_reminder = Button(rem, text = "Update Reminders", relief = RAISED, bg = "#218a5e", width = 20, height = 2, font = "Garamond 13 bold italic", command = update_reminder_command)
	but_update_reminder.grid(row = 6, column = 1)

	but_delete_reminder = Button(rem, text = "Delete Reminders", relief = RAISED, bg = "#218a5e", width = 20, height = 2, font = "Garamond 13 bold italic", command = delete_reminder_command)
	but_delete_reminder.grid(row = 6, column = 2)

	but_clear_entry = Button(rem, text = "Clear Entry box", relief = RAISED, fg = "white", bg = "#872626", width = 12, height = 2, font = "Garamond 7 bold italic", command = clear_entry)
	but_clear_entry.grid(row = 4, column = 0)

	but_close = Button(rem, text = "Close Window", relief = RAISED, bg = "#872626", width = 20, height = 2, font = "Garamond 13 bold italic", command = rem.destroy)
	but_close.grid(row = 8, column = 3)

	display = Label(rem, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 9, column = 3)


	rem.mainloop()

					#TO-DO LIST

def todolist():#-----------------This controls the todo button
	import todo_back
	todo = Toplevel(root)
	todo.geometry("1400x1200+120+120")
	todo.title("To-do List")
	todo.configure(background = "#514d63")
	
				#FUNCTIONS

	def get_selected_rows(event):
		global selected_tuple
		index = listbox.curselection()[0]
		selected_tuple = listbox.get(index)

		add_entry.delete(0,END)
		add_entry.insert(END,selected_tuple[1])

		date_entry.delete(0,END)
		date_entry.insert(END,selected_tuple[2])

	def view_command():
		listbox.delete(0,END)
		for row in todo_back.view_to_do_list():
			listbox.insert(END,row)



	def insert_command():
		todo_back.insert_to_do_list(add_entry_text.get(),date_entry_text.get())
		listbox.delete(0,END)
		listbox.insert(END,(add_entry_text.get(),date_entry_text.get()))
		view_command()
		display["text"] = "Record has been added"

	def update_command():
		todo_back.update_to_do_list(selected_tuple[0], add_entry_text.get(), date_entry_text.get())
		view_command()
		display["text"] = "Record has been updated"

		
	def delete_command():
		todo_back.delete_to_do_list(selected_tuple[0])
		display["text"] = "Record has been deleted"
		view_command()

	def clear_entry():
		add_entry.delete(0,END)  #This is to clear entry in the Entry widget
		date_entry.delete(0,END)  #This is to clear entry in the Entry widget

	def search_command():
		listbox.delete(0,END)
		for rows in todo_back.search(add_entry_text.get(), date_entry_text.get()):
			listbox.insert(END,rows)

				#FONTS
	label_fonts = font.Font(family = "Times", slant = 'italic',weight = 'bold', size = 13)
	arial20 = font.Font(family = "Arial", size = 20, slant = 'italic', underline = 1, weight = 'bold')		
	
				#LABELS


	title_label = Label(todo, bg = "#514d63", text = "Adding To-do Lists", font = arial20,  fg = "#c7c002")
	title_label.grid(row = 0, column = 0, padx = 5, pady = 10)

	title_label1 = Label(todo, bg = "#514d63", text = "Modifying To-do Lists", font = arial20, fg = "#c7c002")
	title_label1.grid(row = 4, column = 0, pady = 20)

	add_label_todolist = Label(todo,  bg = "#514d63", fg = "#4f0d25", text = "Insert To-do List", font = label_fonts)
	add_label_todolist.grid(row = 1, column = 0, padx = 5, pady = 10)

	date_label_todolist = Label(todo,  bg = "#514d63", fg = "#4f0d25", text = "Date", font = label_fonts)
	date_label_todolist.grid(row = 1, column = 2, padx = 5, pady = 10)
	

				#ENTRY

	add_entry_text = StringVar()
	add_entry = Entry(todo, textvariable = add_entry_text, bd = 3, width = 40)
	add_entry.grid(row = 1, column = 1, padx = 10, pady = 10)


	date_entry_text = StringVar()
	date_entry = DateEntry(todo, textvariable = date_entry_text, bd = 3, width = 40)
	date_entry.grid(row = 1, column = 3, padx = 10, pady = 10)


	search_entry_text = StringVar()
	search_entry = Entry(todo, textvariable = search_entry_text, borderwidth = 50, bd = 3, width = 40)
	search_entry.grid(row = 0, column = 6, padx = 10, pady = 40)

				#BUTTONS

	add_but_todolist = Button(todo, cursor = "hand2",bg = "#514d63", fg = "#4f0d25", text = "Add To-do List", relief = RIDGE, width = "50", height = "2", font = "Times 10 bold italic", command = insert_command)
	add_but_todolist.grid(row = 3, column = 1, columnspan = 3, sticky = W+E, pady = 25)

	ref_but_todolist = Button(todo, cursor = "hand2",bg = "#514d63", fg = "#4f0d25", text = "Refresh/View To-do List",width = "20", height = "2", font = label_fonts, command = view_command)
	ref_but_todolist.grid(row = 5, column = 0)

	update_but_todolist = Button(todo, cursor = "hand2",bg = "#514d63", fg = "#4f0d25", text = "Edit/Update To-do List",width = "20", height = "2", font = label_fonts, command = update_command)
	update_but_todolist.grid(row = 6, column = 0)

	delete_but_todolist = Button(todo, cursor = "hand2",bg = "#514d63", fg = "#4f0d25", text = "Delete To-do List",width = "20", height = "2", font = label_fonts, command =  delete_command)
	delete_but_todolist.grid(row = 7, column = 0)

	clear_entry_todolist = Button(todo, bg = "#514d63", fg = "#4f0d25", text = "Clear entry",width = "20", height = "2", cursor = "hand2",font = label_fonts, command =  clear_entry)
	clear_entry_todolist.grid(row = 8, column = 0)

	display = Label(todo, text = "", fg = "blue",font = "Rockwell 15 bold italic")
	display.grid(row = 9, column = 0)

	close_but_todolist = Button(todo, bg = "#514d63", fg = "#4f0d25", text = "Close to-do Window", command = todo.destroy, cursor = "hand2",width = "30", height = "4", font = "Times 10 bold italic")
	close_but_todolist.grid(row = 6, column = 6)	
				
	search_button_todolist = Button(todo,  bg = "#514d63", fg = "#4f0d25", cursor = "hand2",text = "Search",font = label_fonts, command = search_command)
	search_button_todolist.grid(row = 0, column = 5, padx = 5, pady = 10)


				#LISTBOX

	listbox = Listbox(todo, width = 120, height = 30)
	listbox.grid(row = 5, column = 1, columnspan = 4, rowspan = 9)
	view_command()
				#SCROLLBAR
	sb = Scrollbar(todo, orient = "vertical", command = listbox.yview)
	sb.grid(row = 5, column = 5, rowspan = 9, sticky = NS, pady = (10,0))

				#BINDING

	listbox.bind("<<ListboxSelect>>", get_selected_rows)



	todo.mainloop()


def pa_window():
	global root
	root = Tk()
	root.geometry("1150x1150+120+120")
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

	but_todolist = Button(frame, text = "To-do List", font = "Rockwell 13 bold italic", width = "20", height = "2", command = todolist)
	but_todolist.grid(row = 1, column = 0, padx = 10, pady = 10)

	but_reminders = Button(frame, text = "Reminders", width = "20", height = "2", font = "Rockwell 13 bold italic", command = reminder)
	but_reminders.grid(row = 2, column = 0, padx = 10, pady = 10)

	but_presentations = Button(frame, text = "Presentations", width = "20", height = "2", font = "Rockwell 13 bold italic", command = presentation_command)
	but_presentations.grid(row = 3, column = 0, pady = 10)

	but_jd = Button(frame, text = "Staff Job Descriptions", width = "20", height = "2", font = "Rockwell 13 bold italic", command = job_description)
	but_jd.grid(row = 4, column = 0, pady = 10)


							#RIGHT FRAME

	but_meeting = Button(frame1, text = "Meeting Schedule", width = "20", height = "2", font = "Rockwell 13 bold italic", command = meeting_schedule)
	but_meeting.grid(row = 1, column = 3, padx = 10, pady = 10)

	but_min_meeting = Button(frame1, text = "Minutes of Meeting", width = "20", height = "2", font = "Rockwell 13 bold italic", command = minutes)
	but_min_meeting.grid(row = 2, column = 3, padx = 10, pady = 10)

	but_calls = Button(frame1, text = "Call Records", width = "20", height = "2", font = "Rockwell 13 bold italic", command = call_record)
	but_calls.grid(row = 3, column = 3, padx = 10, pady = 10)

	but_org_chart = Button(frame1, text = "Organizational Chart", state = "disabled", width = "20", height = "2", font = "Rockwell 13 bold italic")
	but_org_chart.grid(row = 4, column = 3, padx = 10, pady = 10)

	exit_but = Button(root, text = "Exit Window", command = root.destroy, width = 20, bg = "red", font = "Rockwell 13 bold italic")
	exit_but.grid(row = 6, column = 2, padx = (10,0), pady = (10,0))
	root.mainloop()
	
pa_window()