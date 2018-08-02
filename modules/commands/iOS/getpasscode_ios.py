class command:
    def __init__(self):
        self.name = "getpasscode"
        self.description = "Retrieve The Remote Device Password!"
    
    def run(self,session,cmd_data):
        error = session.send_command(cmd_data)
        if error:
        	print error