import xml.etree.ElementTree as ET
import pandas as pd
import sys
import platform
from datetime import datetime
from LOGO_837477.src.logo_1 import logo
if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen

def converter(API_url):
    try:
        response = urlopen(API_url).read()
    except:
        print("\n!!! ERROR !!!")
        print("Please check busRouteId again.\n")
        return
    xtree = ET.fromstring(response)

    body = xtree.find("msgBody")
    itemList = body.findall("itemList")    
    rows = []
    for item in itemList:
        location_dict = {}
        for location in item:
            location_dict[location.tag] = location.text
        rows.append(location_dict)

    columns = ["gpsX", "gpsY", "no", "posX", "posY"]
    catelog_cd_df = pd.DataFrame(rows, columns = columns)
    if platform.system() == "Windows":
        catelog_cd_df.to_excel('.\\output\\' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.xlsx')
    else:
        catelog_cd_df.to_excel('./output/' + datetime.now().strftime('%Y%m%d_%H%M%S') + '.xlsx')
    print("\n### Sample is it ###")
    print(catelog_cd_df.head(10))
    print()

if __name__ == "__main__":
    logo()

    print("@@ Hello")
    print("This tool is \"Seoul bus route information API response to Excel converter.\"\n")

    print("@@ How to use")
    print("1. Enter the API url.")
    print("2. The output was created in the \"src/output/\" path.\n")

    print("\"exit\" to exit.\n")

    while True:
        API_url = input("Please enter API URL: ")
        if API_url == "exit":
            exit()
        converter(API_url)
