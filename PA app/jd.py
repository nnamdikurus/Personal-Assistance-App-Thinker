from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from PIL import ImageTk, Image
import datetime
import time
import sqlite3


def job_description():
	global jd
	jd = Tk()
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

	jd_pa = Button (frame, text = "Personal assistant", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#132363", width = 25, font = "Florence 18 bold italic")
	jd_pa.grid(row = 2, column = 0, pady = 2)

	jd_acc = Button (frame, text = " Accountant", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic")
	jd_acc.grid(row = 3, column = 0, pady = 2)

	jd_rec = Button (frame, text = "Receptionist", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic")
	jd_rec.grid(row = 4, column = 0, pady = 2)

	jd_cus = Button (frame, text = "Customer Service", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic")
	jd_cus.grid(row = 5, column = 0, pady = 2)

	jd_sm = Button (frame, text = "Social Media Personnel", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#ed0020",width = 25, font = "Florence 18 bold italic")
	jd_sm.grid(row = 6, column = 0, pady = 2)

	jd_hr = Button (frame, text = "Human Resource", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#132363",width = 25, font = "Florence 18 bold italic")
	jd_hr.grid(row = 7, column = 0, pady = 2)

	jd_bd = Button (frame, text = "Business Development Officer", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e67732",width = 25, font = "Florence 18 bold italic")
	jd_bd.grid(row = 8, column = 0, pady = 2)

	jd_op = Button (frame, text = "Operations Manager", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#e632e3",width = 25, font = "Florence 18 bold italic")
	jd_op.grid(row = 9, column = 0, pady = 2)

	jd_sec = Button (frame, text = "Security Personnel", relief = FLAT, bd = 3, bg = "#a2e0f5", fg = "#fafa5c",width = 25, font = "Florence 18 bold italic")
	jd_sec.grid(row = 10, column = 0, pady = 2)

	jd_close = Button(jd, text = "Close Window", relief = RAISED, bd = 3, bg = "red", fg = "white",width = 15, font = "Florence 15 bold italic", command = jd.destroy)
	jd_close.grid(row = 11, column = 2)

	jd.mainloop()




























job_description()