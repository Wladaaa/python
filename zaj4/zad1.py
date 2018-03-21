def zwr(zb):
	zb = zb.split("\n")
	res={}
	for i in zb:
		if i != "\n" and i != "":
			a,b=i.split(":")
			res[a]=b
	return res
napis = '''k1: w2
k2: w2
k3: w3
'''
print zwr(napis)