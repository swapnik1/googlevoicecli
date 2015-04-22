class GoogleVoice():
	def __init__(self, email, password):
		self.errors = []
		if email is null:
			self.errors.append("Please enter an email")
		if password is null:
			self.errors.append("Please enter a password")
		self.email = email
		self.password = password
		self.v = Voice()
		self.isloggedin = False

	def login(self):
		v.login(self.email, self.password)
		self.isloggedin = True

	def sendsms(self, number, message):
		if self.isloggedin:
			self.v.send_sms(number, message)