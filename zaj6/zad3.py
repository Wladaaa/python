#! /usr/bin/env

from xml.dom import minidom
doc = minidom.parse('xpl.xml')
open('nowy.xml', 'w').write(doc.getElements())
