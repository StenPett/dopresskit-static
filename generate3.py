import xmltodict
import json

# Convert xml file to python dict

def xml2dict(src):
    with open(src, "r") as xml_file:
        dict_data = xmltodict.parse(xml_file.read())
    return dict_data

# Functions that output to console

def blabla_ga():
    if ga is None:
        print(">>> Google analytics ID Not found, skipping...\n    Use 'python3 generate3.py <Tracking ID> to activate Google analytics")
    else:
        print("Google analytics: Enabled (ID: %s)" % (ga))

def blabla_projects():
    projects = get_projects()
    if len(projects) == 0:
        print( ">>> No project found, skipping...")
        print( "    Duplicate the '_template' folder, rename it, and edit data.xml")
        print( "    The project folder name must be lowercase, and spaces by _underscores_.")

# Actual presskit stuff
now_project = "."
ga = sys.argv[1] if len(sys.argv) == 2 else None
blabla_ga() 