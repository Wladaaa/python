#! /usr/bin/env

from xml.dom import minidom
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
response = urlopen('https://www.yr.no/place/Poland/Lublin/Lublin/forecast.xml')
doc = minidom.parse(response)
ele = doc.getElementsByTagName('sun')
for el in ele:
    print (el.getAttribute("rise"))
