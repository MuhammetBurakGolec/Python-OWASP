import json

def dic_to_pdf(dictioanry):
    json_object = json.dumps(dictioanry, indent = 4)
    return json_object