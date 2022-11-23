# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10


import sys
import subprocess


class scannmap:
    def __init__(self, target: str, port: str, request: str, options :str):
        self.target = target
        self.port = port
        self.request = request
        self.options = options
        dict = { "target": self.target, "port": self.port, "request": self.request, "options": self.options}

    def scan(self):
        if (self.target == None):
            print("Please enter a target")
            sys.exit(1)

        elif (self.target == '127.0.1.1' or self.target == 'localhost'):
            print("Please enter a target")
            sys.exit(1)

        elif (self.port.lower == "all" ):
            self.port = "1-65535"

        elif (self.port == None):
            print("Please enter a port")
            sys.exit(1)

        elif (self.options != None):
            print("Options Set")
            print(self.request,'nmap' ,self.target,self.options, self.port)

            try:
                Scan_Value = subprocess.call([self.request,'nmap' ,self.target,self.options, self.port])
                Scan_Value = str(Scan_Value)
                print(Scan_Value)
                return Scan_Value
            except subprocess.CalledProcessError as e:
                print("Error: ", e.output)
                sys.exit(1)
        
        else:
            print("OPTIONS NOT SET")