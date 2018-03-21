def zwr(nazwa):
	f = open(nazwa)
	zb = f.read()	
	f.close()
	zb = zb.split("\n")
	res={}
	for i in zb:
		if i != "\n" and i != "":
			a,b=i.split(":")
			res[a]=b
	return res

print zwr("text.txt")
