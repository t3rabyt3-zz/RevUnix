class command:
    def __init__(self):
        self.name = "safemode"
        self.description = "Put The Remote Device On The Safe Mode!"

    def run(self,session,cmd_data):
    	cmd_data["cmd"] = ";"
    	cmd_data["args"] = "touch /var/mobile/Library/Preferences/com.saurik.mobilesubstrate.dat; killall SpringBoard"
        result = session.send_command(cmd_data)
        if result:
        	print result
