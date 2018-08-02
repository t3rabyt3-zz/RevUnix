class command:
    def __init__(self):
        self.name = "getvol"
        self.description = "Detect The Volume Status From The Remote Device!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
