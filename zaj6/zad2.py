#! /usr/bin/env
import re, json

class Wyjatek(Exception):
   pass 

class Emaily:
    emaily = {}
    def __init__(self,napis):
        regex_email = re.compile(
            r'''(?P<adres>
            [\w+.]+
            @
            \w+(\.\w+)+
            )''',
            re.IGNORECASE | re.VERBOSE
        )
        if (not regex_email.match(napis)):
            print ("None")      
            try:
                raise Wyjatek("ERROR: Niewlasciwy email")
            except Wyjatek as w:
                print (w)
        else:
            for i in regex_email.finditer(napis):
                self.emaily['adres']=i.groupdict()['adres']
napis = "vlada55mail.ru"
emtab = Emaily(napis)
print (emtab.emaily)
napis = "vlada@mail.ru"
emtab = Emaily(napis)
print (emtab.emaily)
 
