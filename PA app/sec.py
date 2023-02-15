from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3

def meeting_schedule():
	ms = Tk()
	ms.title("Meeting Schedule")
	ms.geometry("1000x800")
	ms.configure(background = "#8499ba")




	#-------------------IMAGES-----------------#
	img = PhotoImage(file = "C:\\Icons\\meet1.png")
	img_lab = Label(ms, image = img)
	img_lab.grid(row = 1, column = 1, padx = (40,0))

	#--------------------FRAMES-------------------#

	frame_label = LabelFrame(ms, padx = 15, pady = 10, bg = "#7f9494", width = 20, height= 20, relief = SUNKEN)
	frame_label.grid(row = 1, column = 0, columnspan = 1)

	#----------------LABELS----------------------

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

	but_add = Button(frame_label, text = "Add Schedule", bd = 3, bg = "#38b9c2", fg = "#9c3030",width = 13, font = "Rockwell 15 bold italic")
	but_add.grid(row = 6, column = 1, padx = 10, pady = 10)


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
	date_entry = Entry(frame_label, textvariable = date_text, width = 50, bd = 3)
	date_entry.grid(row = 5, column = 1)

	#---------------TREEVIEW----------------------------#



	#--------------MENUS AND SUBMENU--------------------#





	#------------------TIME AND DATE---------------------#










	ms.mainloop()

meeting_schedule()