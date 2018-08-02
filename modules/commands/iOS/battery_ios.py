class command:
    def __init__(self):
        self.name = "Battery"
        self.description = "Get Current Battery Percentage!!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
