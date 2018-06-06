#!/usr/bin/env python
#encoding: utf-8

import re, json

text="codshihihico8ssfiiiiicohs"

SLOWO = "cos"

my_wyr = r"[\w]*["+ re.escape(SLOWO) +r"+][\w]*"

if re.search(my_wyr, text, re.IGNORECASE):
    print("Niesamowite")
else:
    print("None")
