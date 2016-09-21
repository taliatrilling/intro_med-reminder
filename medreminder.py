from mailin import Mailin
import datetime
from key import m 

class Medication(object):
	def __init__ (self, med_name, days_between_orders, days_remind_before, dose = "", email = ""):
		self.med_name = med_name
		self.days_between_orders = days_between_orders
		self.days_remind_before = days_remind_before
		self.dose = dose 
		self.email = email
	def send_email_reminder(self):
		days_to_remind = int(self.days_between_orders - self.days_remind_before)
		target = datetime.timedelta(days = days_to_remind)
		future_target = str(datetime.datetime.now() + datetime.timedelta(days = days_to_remind))
		if self.email == "":
			print "You have not set an email for this reminder to go to."
		else: 
			data = { "to" : {self.email:"Reminder recipient"},
		"from" : ["taliatrilling@gmail.com", "Talia"],
		"subject" : "You have a medication awaiting renewal!",
		"html" : "REMINDER: your medication, %s, needs to be renewed, as you last ordered it %s days ago. Thank you for using MedReminder!" % (self.med_name, days_to_remind),
		"listid": [2,7],
		"scheduled_date":future_target
		}
			result = m.send_email(data)
	    	print(result)


med = Medication("Placeholder med", 60, 10, email = "taliatrilling@gmail.com")

def main():
	meds_list = []
	Medication.send_email_reminder(med)

if __name__ == '__main__':
	main() 

