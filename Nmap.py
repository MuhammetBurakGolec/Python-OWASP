# from https://pypi.org/project/python-nmap/
# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10

import nmap


def __init__(self, *target, port, t_out):
    self.target = target.get('target', None)
    self.port = port.get('port', None)
    self.t_out = t_out.get('t_out', None)
    return self.scan(self.target, self.port, self.t_out)

def scan(self, target, port = '1-65535', t_out = 10):
    self.target = target
    nm = nmap.PortScanner()
    # scan all ports
    nm.scan(target, port, timeout=t_out)
    return nm
