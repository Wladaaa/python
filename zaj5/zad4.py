#!/usr/bin/env python
#encoding: utf-8

import re, json

regex_email = re.compile(
    r'''(?P<Pesel>
         (?P<Rok>[\d]{2})
         (?P<Miesac>[\d]{2})
         (?P<Dzien>[\d]{2})
         [\d]{3}
         (?P<Plec>[\d])
         [\d]
    )''',
    re.IGNORECASE | re.VERBOSE
)

tekst = open("text.txt")
for line in tekst:
    lines = line.split()
    res={}
    for i in lines:
        print i
        for match_object in regex_email.finditer(i):
            print match_object.groupdict()
            if(match_object.groupdict()['Miesac']<=12) res['Rok']='19'+match_object.groupdict()['Rok']
            print res
