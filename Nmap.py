# from https://pypi.org/project/python-nmap/
# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10

import nmap3 as nmap

def __init__(self, *args, **kwargs):
    pass

def scan(self, target):
    nmap = nmap.Nmap()
    results = nmap.scan_top_ports(target)
    return results