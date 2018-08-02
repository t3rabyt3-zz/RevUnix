class command:
    def __init__(self):
        self.name = "ipod"
        self.description = "Control The Music Player Of The Remote Device!"
        self.usage = "Usage: iPod Play||Pause||Next||Prev||Info"
    
    def run(self,session,cmd_data):
    	if not cmd_data['args'] or not cmd_data['args'] in ['Play','Pause','Next','Prev','Info']:
    		print self.usage
        result = session.send_command(cmd_data)
        if result:
        	print result.rstrip()