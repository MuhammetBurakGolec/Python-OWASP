#!/bin/env/python3.10
import Nmap, Convert, Output, Split, Vuln_port

def main():
    nmap = Nmap.scannmap(target="127.0.0.1",port="631",request="sudo",options="-sT -sU -sV -O -Pn -p")  
    #scan_json = Convert.dic_to_pdf(scan)
    print(nmap.scan())

if __name__ == '__main__':
    main()
