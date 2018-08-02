class command:
    def __init__(self):
        self.name = "home"
        self.description = "Simulate A Home-Button Press!"
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
        	print error