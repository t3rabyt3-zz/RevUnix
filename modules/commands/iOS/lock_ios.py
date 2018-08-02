class command:
    def __init__(self):
        self.name = "lock"
        self.description = "Simulate A Lock Button Press!"
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
        	print error