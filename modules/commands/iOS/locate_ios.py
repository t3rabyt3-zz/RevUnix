class command:
    def __init__(self):
        self.name = "locate"
        self.description = "Get Device Current Location & Cordiantes!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
