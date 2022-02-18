#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import otp_logic

global_font = font=("Arial", 16, "bold")

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
		self.new_win = Manager(self.new_win, "otp-manager", "560x200+600+175")


class Manager:
	def __init__(self, root, title, geometry):
		self.root = root
		self.root.title(title)
		self.root.geometry(geometry)

		btnList = ["Add", "List", "Quit"]
		btnCmdList = [self.add_otp, self.test, self.test]

		for i in range(3):
			Button(self.root, text=btnList[i], width=20, height=10, command=btnCmdList[i]).pack(padx=10, side=LEFT)

	def add_otp(self):
		self.root = Tk()
		self.root.title("Add")
		self.root.geometry("400x150")
		self.uname = StringVar()
		self.secret = StringVar()

		Label(self.root, text="Name", width=30, height="2", font=("Arial", 10, "bold")).place(x=-80, y=40)
		Entry(self.root, width=20, textvariable=self.uname).place(x=65, y=45)
		
		Label(self.root, text="Secret", width=30, height="2", font=("Arial", 10, "bold")).place(x=-80, y=70)
		Entry(self.root, width=35, textvariable=self.secret).place(x=65, y=75)
	
	def test(self):
		messagebox.showinfo(title="Success", message="Succesfully executed")


def main():
	root = Tk()
	MainWindow = GUI(root, "OTP-Manager", "300x300+700+150")

if __name__ == "__main__":
	main() 