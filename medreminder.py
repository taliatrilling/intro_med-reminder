class Medication(object):
	def __init__ (self, med_name, days_between_orders, days_remind_before, dose = "", email = ""):
		self.med_name = med_name
		self.days_between_orders = days_between_orders
		self.days_remind_before = days_remind_before
		self.dose = dose 
		self.email = email
	def send_email_reminder(self):
		if self.email == "":
			print "You have not set an email for this reminder to go to."
		else: #NEED SOMETHING TO MONITOR IF CORRECT # OF DAYS HAS PASSED 
			days_to_remind = days_between_orders - days_remind_before
			print "To: %s - Your medication, %s, needs to be renewed, as you last ordered it %s days ago" % (self.email, self.med_name, days_to_remind)
	# def send_text_reminder(self):
	# 	if self.mobile == "":
	# 		print "You have not set a mobile number for this text reminder to go to."
	# 	else: #NEED SOMETHING TO MONITOR IF CORRECT # OF DAYS HAS PASSED 
	# 		days_to_remind = days_between_orders - days_remind_before
	# 		print "To: %s - Your medication, %s, needs to be renewed, as you last ordered it %s days ago" % (self.mobile, self.med_name, days_to_remind)

med = Medication("Placeholder med", 60, "4 mg", "taliatrilling@gmail.com")

def main():
	meds_list = []

if __name__ == '__main__':
	main() 