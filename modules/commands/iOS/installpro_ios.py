import modules.helper as h
import re, os, time

class command:
    def __init__(self):
        self.name = "installpro"
        self.description = "Install Substrate Commands!"
    
    def run(self,session,cmd_data):
    	h.info_general("Uploading dylib 1/2...")
        session.upload_file("resources/rupro.dylib","/Library/MobileSubstrate/DynamicLibraries",".rupl.dylib")
    	h.info_general("Uploading plist 2/2...")
        session.upload_file("resources/rupro.plist","/Library/MobileSubstrate/DynamicLibraries",".rupl.plist")
        h.info_general("Respring...")
        time.sleep(1)
        session.send_command({"cmd":"killall","args":"SpringBoard"})
