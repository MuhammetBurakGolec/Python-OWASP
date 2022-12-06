#!/bin/env/python3.10
import Nmap, Convert, Output, Split, Vuln_port
import json

def main():
    target, port, request, options = input_data()
    print(target, port, request, options)
    nmap = Nmap.scannmap(target=f"{target}",port=f"{port}",request=f"{request}",options=f"{options}") # Change this to your needs
    data = nmap.scan()
    Convert.xml_to_json(xml="nmap.xml",output='/tmp/nmap.json')
    #Convert.json_to_data_json(path='../nmap_result/nmap.json',output='../nmap_result/nmap_responde.json')

def input_data():
    with open('config.json') as json_file:
        data = json.load(json_file)
        target = data['host']['target']
        port = data['host']['port']
        request = data['host']['request']
        options = data['host']['options']
        return str(target), str(port), str(request), str(options)



if __name__ == '__main__':
    main()
