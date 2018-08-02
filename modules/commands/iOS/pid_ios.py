class command:
    def __init__(self):
        self.name = "pid"
        self.description = "Get Active Process ID!"

    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
