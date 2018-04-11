#! /usr/bin/env

#import urllib2
from xml.dom import minidom

#def divide(x, y):
#    try:
#        result = x/y
#    except (ZeroDivisionError, TypeError) as ex:
#        print ("Kurka, mam problem")
#        print (ex)
#    else:
#        print ("Spokoloko")
#        return result
 #   finally:
#        print ("Koniec funkcji")
#vprint (divide(4,"test"))

#class Wyjatek(Exception):
#    pass 
#try:
#    raise Wyjatek('Wystapil nieoczekiwany blad')
#except Wyjatek as w:
#    print (w)
    
#response = urllib2.urlopen('http://python.org')
#print (response.read())

doc = minidom.parse('xpl.xml')
ele = doc.getElementsByTagName('el')
for el in ele:
    sid = el.getAttribute("id")
    test = el.getElementsByTagName('test')[0]
