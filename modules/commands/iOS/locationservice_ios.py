class command:
    def __init__(self):
        self.name = "locationservice"
        self.description = "toggle location services"
        self.usage = "Usage: locationservice On||Off"
    
    def run(self,session,cmd_data):
       	if not cmd_data['args'] or not cmd_data['args'] in ['O','Off']:
       		print self.usage
       		return
       	if cmd_data['args'] == "On":
       		cmd_data = {'cmd':'locationon','args':''}
       	elif cmd_data['args'] == "Off":
       		cmd_data = {'cmd':'locationoff','args':''}
        error = session.send_command(cmd_data)
        if error:
        	print error