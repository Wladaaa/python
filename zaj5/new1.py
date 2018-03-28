#!/usr/bin/env python
#encoding: utf-8

import re, json

regex_email = re.compile(
    r'''(?P<adres>
         (?P<login>[\w+.]+)
         @
         (?P<domena>\w+(\.\w+)+)
    )''',
    re.IGNORECASE | re.VERBOSE
)

tekst = u'mail1@gmail.com, "jan.nowak@poczta.buyuy.pl"'
for match_object in regex_email.finditer(tekst):
    print match_object.groupdict()
    
slownik = {
    'k1': 'w1',
    'k2': 'w2',
    3: [1,2,3]
}

json_str = json.dumps(slownik)
print json_str
print isinstance(json_str, basestring)
slownik = json.loads(json_str)
print slownik.items()
