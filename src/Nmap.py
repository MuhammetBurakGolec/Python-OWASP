# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10


import sys
import subprocess


class scannmap:
    def __init__(self, target: str, port: str, request: str, options :str):
        self.target = target
        if port.lower == "all" or port == None:
            self.port = "1-65535"
        else:
            self.port = port
        self.request = request
        self.options = options
        self.dict = { "target": self.target, "port": self.port, "request": self.request, "options": self.options}
        self.scan_approuved = False
        
        if (self.target == None):
            print("Please enter a target")
            sys.exit(1)

        elif (self.target == '127.0.0.1' or self.target == 'localhost'):
            print("Please enter a target")
            sys.exit(1)

        elif (self.port == None):
            print("Please enter a port")
            sys.exit(1)
        
        elif (self.options != None):
            print("Options Set")
            self.scan_approuved = True
            print("Scan Approuved")

        else:
            print("Please enter a option")
            print("Scan Not Approuved")

    def scan(self):
        if (self.scan_approuved == True):

            print(self.request,'nmap' ,self.target,self.options, self.port)
            value =f"{self.request} nmap {self.target} {self.options} {self.port} -oX nmap.xml"
            try:
                subprocess.call([value,], shell=True)
                return self.dict

            except subprocess.CalledProcessError as e:
                print("Error: ", e.output)
                sys.exit(1)     

            finally:
                print("Scan PID Completed")

        else:
            print("Options not set")

    def scan_script(self):

        pass
        