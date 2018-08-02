class command:
    def __init__(self):
        self.name = "dial"
        self.description = "Make A Call From The Device!!"
        self.usage = "Usage: dial 8447231555"
    
    def run(self,session,cmd_data):
    	if not cmd_data['args']:
    		print self.usage
    		return
    	cmd_data.update({"cmd":"openurl","args":"tel://"+cmd_data['args']})
        session.send_command(cmd_data)
