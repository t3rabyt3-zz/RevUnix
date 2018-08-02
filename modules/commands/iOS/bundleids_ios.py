class command:
    def __init__(self):
        self.name = "bundleids"
        self.description = "List Bundle Identifiers!"
    
    def run(self,session,cmd_data):
        print session.send_command(cmd_data).rstrip()
