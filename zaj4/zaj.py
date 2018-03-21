# encoding: utf-8
import sys
#print sys.arg
slownik = {
'k1': 'w1',
'k2': 'w2',
2: [1,2,3],
(1,2,3): 4 
}

slownik['slownik'] = slownik


print slownik
print slownik.get('w3','none')

for i in slownik.items():
	print i
	
for i in slownik.keys():
	print i
	
for i in slownik.values():
	print i
napis1 = """abs
test2"""
print napis1
Slist = ["a","b","c"]
napis = " "
napis = napis.join(Slist)
print napis
print napis.split(" ")

#f = open("text.txt")
#print f.read()
#for line in f:
#	print line
#with open("text.txt") as f:
#	print f.read()
with open("text.txt","w") as f:
	f.write("hehehehe")
f.close()