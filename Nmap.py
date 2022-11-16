# from https://pypi.org/project/python-nmap/
# Path: Nmap.py
# Compare this snippet from main.py:
# #!/bin/env/python3.10

import nmap


def scan(target, port='1-65535'):
    nm = nmap.PortScanner()
    result_scan = nm.scan(target, port)
    return result_scan
