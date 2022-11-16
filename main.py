#!/bin/env/python3.10
import Nmap, Convert, Output, Split, Vuln_port

def main():
    scan = Nmap.scan(target="127.0.0.1")
    scan_json = Convert.dic_to_pdf(scan)
    print(scan_json)


if __name__ == '__main__':
    main()
