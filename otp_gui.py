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
		Entry(self.root, width='35', show="*", textvariable=self.passw).place(x=90, y=100, width=150)
		Button(text="Login", width="10", font=("Arial", 10, "bold"), command=self.check).place(x=100, y=130)

		self.root.mainloop()

	def test(self):
		return self.passw.get()

	def check(self):
		if otp_logic.check_pass(self.test()) == True:
			self.Manager_GUI()
		else:
			messagebox.showwarning(title="Error", message="You entered the wrong password.")
			
	def Manager_GUI(self):
		self.new_win = Toplevel(self.root)
		self.new_win = Manager(self.new_win, "otp-manager", "1010x610+510+125")


class Manager:
	def __init__(self, root, title, geometry):
		self.root = root
		self.root.title(title)
		self.root.geometry(geometry)
		
		self.root.mainloop()
		

def main():
	root = Tk()
	MainWindow = GUI(root, "OTP-Manager", "300x300+700+150")

if __name__ == "__main__":
	main() 