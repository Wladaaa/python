#!/usr/bin/env python
#encoding: utf-8

import re, json

regex_email = re.compile(
    r'''(?P<adresIPv4>
         ([0-2]{0,2}[0-5])
         .
         ([0-2]{0,2}[0-5])
         .
         ([0-2]{0,2}[0-5])
         .
         ([0-2]{0,2}[0-5])
    )''',
    re.IGNORECASE | re.VERBOSE
)

tekst = open("text.txt")
for line in tekst:
    lines = line.split()
    
    for i in lines:
        for match_object in regex_email.finditer(i):
            print match_object.groupdict()
