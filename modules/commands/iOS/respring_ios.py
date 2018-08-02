class command:
	def __init__(self):
		self.name = "respring"
		self.description = "Restart SpringBoard!"

	def run(self,session,cmd_data):
		session.send_command({"cmd":"killall","args":"SpringBoard"})
