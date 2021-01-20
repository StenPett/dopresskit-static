import xmltodict
import json


def xml2dict(src):
    with open(src, "r") as xml_file:
        dict_data = xmltodict.parse(xml_file.read())
    return dict_data

dict_data = xml2dict('data.xml')
ordered_data = json.loads(json.dumps(dict_data))
print(ordered_data)
