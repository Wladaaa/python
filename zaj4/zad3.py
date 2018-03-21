import sys
arg = sys.argv
f = open(arg[1])
res = f.read().split(" ")
tab = {}
for i in res:
	if i in tab.keys():
		tab[i]+=1
	else:
		tab[i]=1
	
print tab
f.close
