class Medication(object):
	def __init__ (self, med_name, days_between_orders, days_remind_before, dose = "", email = "", mobile = ""):
		self.med_name = med_name
		self.days_between_orders = days_between_orders
		self.days_remind_before = days_remind_before
		self.dose = dose 
		self.email = email
		self.mobile = mobile
	def send_email_reminder(self, med_name, days_between_orders, days_remind_before, email):
		if self.email == "":
			print "You have not set an email for this reminder to go to."
		else: #NEED SOMETHING TO MONITOR IF CORRECT # OF DAYS HAS PASSED 
			print "To: %s - Your medication, %s, needs to be renewed, as you last ordered it %s days ago" % (self.email, self.med_name, self.days_between_orders)
	def send_text_reminder(self, med_name, days_between_orders, days_remind_before, mobile):
		if self.mobile == "":
			print "You have not set a mobile number for this text reminder to go to."
		else: #NEED SOMETHING TO MONITOR IF CORRECT # OF DAYS HAS PASSED 
			print "To: %s - Your medication, %s, needs to be renewed, as you last ordered it %s days ago" % (self.mobile, self.med_name, self.days_between_orders)

med = Medication("Placeholder med", 60, "4 mg", "taliatrilling@gmail.com", 00000000000)

def main():
	meds_list = []


if __name__ == '__main__':
	main() 