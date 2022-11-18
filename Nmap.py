# from https://pypi.org/project/python-nmap/
# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10

import sys
import subprocess


class scannmap:
    def __init__(self, target, port='1-65535',request='sudo', options='-sU -sT -sV -O -p'):
        self.target = target
        self.port = port
        self.request = request
        self.options = options


    def scan(self):
        if (self.target == None):
            print("Please enter a target")
            sys.exit(1)

        elif (self.target == '127.0.1.1' or self.target == 'localhost'):
            print("Please enter a target")
            sys.exit(1)

        elif (self.port == None):
            print("Please enter a port")
            sys.exit(1)

        elif (self.options != None):
            print("Options Set")
            print(self.request,'nmap' ,self.target,self.options, self.port)
            return subprocess.call([self.request,'nmap' ,self.target,self.options, self.port])
        
        else:
            print("OPTIONS NOT SET")