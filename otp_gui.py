#!/usr/bin/env python3

try:
	from tkinter import *
	from tkinter import messagebox, ttk, StringVar
except ImportError:
	from Tkinter import *
	from Tkinter import message, ttk, StringVar

import otp_logic, pyotp, sys

global_font = font=("Arial", 12, "bold")

class GUI:
	def __init__(self, root, title, geometry):
		self.root = root
		self.root.title(title)
		self.root.geometry(geometry)
		self.passw = StringVar()

		Label(text="OTP Manager Login Page", width="30", height="2", font=global_font).pack() 
		Label(text="Password -", width="35", font=("Arial", 10, "bold")).place(x=-80, y=100)
		Entry(self.root, width=35, show="*", textvariable=self.passw).place(x=90, y=100, width=150)
		Button(text="Login", width="10", font=("Arial", 10, "bold"), command=self.check).place(x=100, y=130)

		self.root.mainloop()

	def check(self):
		if otp_logic.check_pass(self.passw.get()):
			self.Manager_GUI()
		else:
			messagebox.showwarning(title="Error", message="You entered the wrong password.")
			
	def Manager_GUI(self):
		self.new_win = Toplevel(self.root)
		self.new_win = Manager(self.new_win, "otp-manager", "380x250+600+175")

class Manager:
	def __init__(self, root, title, geometry):
		self.root = root
		self.root.title(title)
		self.root.geometry(geometry)

		self.test = StringVar()

		self.menubar = Menu(self.root)
		self.misc = Menu(self.menubar, tearoff=0)
		self.misc.add_command(label="Change Password", command=self.otp_pwd)
		self.misc.add_separator()
		self.misc.add_command(label="Quit", command=sys.exit)
		self.menubar.add_cascade(label="Misc", menu=self.misc)

		self.root.config(menu=self.menubar)

		btnList = ["Add", "List"]
		btnCmdList = [self.add_otp, self.otp_list]

		for i in range(2):
			Button(self.root, text=btnList[i], width=20, height=10, command=btnCmdList[i]).pack(padx=10, side=LEFT)

	def add_otp(self):
		self.root = Tk()
		self.root.title("Add")
		self.root.geometry("400x150")
		self.uname, self.secret = StringVar(), StringVar()

		Label(self.root, text="Name", width=30, height="2", font=("Arial", 10, "bold")).place(x=-80, y=40)
		Label(self.root, text="Secret", width=30, height="2", font=("Arial", 10, "bold")).place(x=-80, y=70)
		Entry(self.root, width=20, textvariable=self.uname).place(x=65, y=45, width=150)
		Entry(self.root, width=35, textvariable=self.secret).place(x=65, y=75)

		Button(self.root, text="Submit", font=global_font, command=self.send_input).place(x=0, y=100)

		self.root.mainloop()

	def send_input(self):
		otp_logic.write_to_file((self.uname.get()), (self.secret.get()))
		
	def otp_list(self):
		self.root = Tk()
		self.root.title("OTP List")
		self.root.geometry("300x610+660+125")
		self.root.resizable(0, 1)

		self.TableMargin = Frame(self.root, width=500)
		self.TableMargin.pack(side=TOP)
		self.scrollbary = Scrollbar(self.TableMargin, orient=VERTICAL)
		self.tree = ttk.Treeview(self.TableMargin, columns=("Name", "OTP"), height=30)
		self.tree.heading("Name", text="Name", anchor=W)
		self.tree.heading("OTP", text="OTP", anchor=W)
		self.tree.column("#0", stretch=NO, minwidth=0, width=0)
		self.tree.column("#1", stretch=NO, minwidth=0, width=200)
		self.tree.column("#2", stretch=NO, minwidth=0, width=100)
		self.tree.pack()

		keys = otp_logic.decrypt()
		for i in keys:
			Name = i
			Otp = pyotp.TOTP(keys.get(i)).now()
			self.tree.insert("", 1, values=(Name, Otp))

		self.root.mainloop()
	
	def otp_pwd(self):
		self.root = Tk()
		self.root.title("Change Password")
		self.root.geometry("400x150+660+125")

		self.new_pw = StringVar()
		
		Label(self.root, text="Password", width=30, height="2", font=("Arial", 10, "bold")).place(x=-80, y=40)
		Entry(self.root, textvariable=self.new_pw).place(x=65, y=40, width=150)
		Button(self.root, text="Submit", font=global_font, command=self.dummy).place(x=0, y=80)

		self.root.mainloop()

	def dummy(self):
		print(self.new_pw.get())

def main():
	root = Tk()
	MainWindow = GUI(root, "OTP-Manager", "300x300+700+150")

if __name__ == "__main__":
	main() 