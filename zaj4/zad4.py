import sys
arg = sys.argv
znaki =arg[2]
if arg[1]!="-":
	f = open(arg[1])
	for line in f:
		res = line.split(" ")
		for i in res:
			if i==znaki:
				print line
				break
	f.close()
else:
	lin = " "
	while(lin != ""):
		lin=raw_input()
		linie = lin.split(" ")
		for i in linie:
			if i==znaki:
				print lin
				break
	