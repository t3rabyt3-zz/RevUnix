class command:
    def __init__(self):
        self.name = "lastapp"
        self.description = "Check The Last Open Application!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
