class command:
    def __init__(self):
        self.name = "islocked"
        self.description = "Check If The Remote Device Is Currently Locked Or Not!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
