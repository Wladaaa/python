#!/usr/bin/env python
#encoding: utf-8

width = input()

f = open("text.txt")
res=""
k=1
for line in f:
    line = line.strip()
    if len(line)>width:
        for i in range(len(line)):
            if(k<=width):
                k+=1
                res=res+line[i]
            else:
                k=2
                print res.center(width)
                res = line[i]
    else: print line.center(width-len(line))
print res.center(width)
