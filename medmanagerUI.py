from medmanager import Medication
import medmanager as mm 
from Tkinter import *

root_widget = Tk()
var_label_text = StringVar()

# GUI frame for system

def menu():
	menubar = Menu(root_widget)
	root_widget.geometry("350x200")
	root_widget.title("Medication Reminder")
	menubar.add_command(label = "Quit", command = root_widget.quit)
	var_label_text.set("Please choose an option below: ")
	first_label = Label(root_widget, textvariable = var_label_text)
	first_label.grid(row = 0, columnspan = 5)
	btn_show_meds = Button(text = "Show all medication and previously set parameters", command = lambda: mm.show_meds())
	btn_show_meds.grid(row = 1, columnspan = 2)
	btn_change_meds = Button(text = "Change a medication's name or reminder parameters", command = lambda: mm.change_info())
	btn_change_meds.grid(row = 2, columnspan = 2)
	btn_add_meds = Button(text = "Add a new medication to the program", command = lambda: mm.add_new())
	btn_add_meds.grid(row = 3, columnspan = 2)
	btn_del_meds = Button(text = "Delete a medication from the program", command = lambda: mm.delete())
	btn_del_meds.grid(row = 4, columnspan = 2)
	btn_exit = Button(text = "Exit", command = quit)
	btn_exit.grid(row = 5 ,columnspan = 2)
	root_widget.config(menu = menubar)
	root_widget.mainloop()

def main():
	menu()
	while(True):
		pass

if __name__ == '__main__':
	main()