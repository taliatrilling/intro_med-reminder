from medreminder import Medication

med_list = []

def check_med(med_name):
	for item in med_list:
		if item.med_name == med_name:
			return 1
		else:
			return 2

def show_meds():
	print "Your current medications are:"
	for item in med_list:
		print item.med_name

def reminder_frequency(days_between_orders, days_remind_before):
	pass

def change_info():
	show_meds()
	change = raw_input("Which medication would you like to change the information for? ").lower()
	if check_med(change) == 1:
		print "Your current info for this medication is:"
		for i in range(len(med_list)):
			if med_list[i].med_name == change:
				print "Medication name: " + med_list[i].med_name
				print "Days between orders: " + med_list[i].days_between_orders
				print "Shipping time for orders in days" + med_list[i].days_remind_before
				print "Dose (if specified): " + med_list[i].dose
		change_part = raw_input("""what part of this medication's information would you like to change?
Please enter 'name,' 'days between orders,' 'shipping days,' 'dose,' or 'exit' if you have decided not to change the listing.""").lower()
		if change_part == "name" or change_part == "name,":
			new_name = raw_input("What would you like the medication's new name to be? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list.med_name = new_name
			print "Your medication name has been changed"
		elif change_part == "days between orders" or change_part == "days between orders,":
			new_days = raw_input("What would you like to set as the number of days between this medication's orders? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].days_between_orders = new_days
			print "The time one shipment of your medication covers has been changed."
		elif change_part == "shipping days" or change_part == "shipping days,":
			new_shipping = raw_input("What would you like to set as the new shipping time for this medication's orders? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].days_remind_before = new_shipping
			print "Your shipping time for this medication has been changed." 
		elif change_part == "dose" or change_part == "dose,":
			new_dose = raw_input("What would you like to set as the new dose for this medication? ")
			for i in range(len(med_list)):
				if med_list[i].med_name == change:
					med_list[i].dose = new_dose
			print "Your medication dose has been changed."
		elif change_part == "exit":
			return
	else:
		print """That medication is not on your list of medications. 
Please make sure you are spelling the medication correctly."""

def add_new():
	# make sure to account for .lower()
	pass

def delete():
	show_meds()
	delete = raw_input("""Which medication would you like to remove (please type exit if you have decided to not
delete a medication)? """).lower()
	if check_med(delete) == 1:
		for i in range(len(med_list)):
			if med_list[i].med_name == delete:
				med_list.remove(med_list[i])
				break
		print "Your medication has been deleted." 
	elif delete == "exit":
		return
	else:
		print """That medication is not on your list of medications. 
Please make sure you are spelling the medication correctly."""


def main():
	pass

if __name__ == '__main__':
	main()