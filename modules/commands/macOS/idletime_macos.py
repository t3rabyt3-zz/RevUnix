class command:
    def __init__(self):
        self.name = "idletime"
        self.description = "Get The Amount Of Time Since The Keyboard/Cursor Were Touched!"
        self.type = "native"

    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
