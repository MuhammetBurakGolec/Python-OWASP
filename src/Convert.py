import os
import json
import xmltodict

def dic_to_pdf(dictioanry):
    json_object = json.dumps(dictioanry, indent = 4)
    return json_object

def xml_to_json(xml : str, output : str):
    
    f = open(xml)
    xml_content = f.read()
    f.close()
    os.remove(xml)

    with open(output, 'w') as json_file:
        json.dump(xmltodict.parse(xml_content), json_file, indent=4)

def json_to_data_json(path : str,output : str):
    with open (path) as json_file:
        data = json.load(json_file)
        with open(output, 'w') as json_file:
            json_file.write("{")
        
        try:
            scaninfo = (data['nmaprun']['scaninfo'])
            with open(output, 'a') as json_file:
                json_file.write('"scaninfo":')
                json.dump(scaninfo, json_file, indent=4)
        except KeyError:
            print("No Scan Info")
        try:
            Address = (data['nmaprun']['host'])
            with open(output, 'a') as json_file:
                json_file.write(",\n")
                json_file.write('"Address":')
                json.dump(Address, json_file, indent=4)
  
        except KeyError:
            print("No Address")    

        try:
            Ports = (data['nmaprun']['host']['ports'])
            with open(output, 'a') as json_file:
                json_file.write(",\n")
                json_file.write('"Ports":')
                json.dump(Ports, json_file, indent=4)

        except KeyError:
            print("No Ports")


        with open('nmap_responde.json', 'a') as json_file:
            json_file.write("}")