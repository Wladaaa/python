#! /usr/bin/env

from xml.dom import minidom
from urllib.request import urlopen
response = urlopen('https://www.yr.no/place/Poland/Lublin/Lublin/forecast.xml')
doc = minidom.parse(response)
ele = doc.getElementsByTagName('sun')
for el in ele:
    res=el.getAttribute("rise")
print (res[11:21])
