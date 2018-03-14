import math
class zesp(object):
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def __add__(self, other):
        if (type(other)==type(self)):
            res = zesp(self.a+other.a, self.b+other.b) 
        else:
            res=self
            res.a=self.a+other
        return res
    def __sub__(self, other):
        if (type(other)==type(self)):
            res = zesp(self.a-other.a, self.b-other.b) 
        else:
            res=self
            res.a=self.a-other
        return res
    def __mul__(self, other):
        if (type(other)==type(self)):
            res = zesp(self.a*other.a, self.b*other.b)
            return res
        else:
            res = zesp(self.a*other, self.b*other)
            return res
    def __div__(self, other):
        if (type(other)==type(self)):
            res = zesp(self.a/other.a, self.b/other.b) 
            return res
        else:
            res = zesp(self.a/other, self.b/other) 
            return res
    def modul(self):
        return math.sqrt((self.a**2)+(self.b**2))
    def __comp__(self, inny):
        if (self.modul()<inny.modul()):
            return -1
        elif (self.modul()>inny.modul()) :
            return 1
        else:
            return 0
    def __str__(self):
        return "%s + %si" % (self.a, self.b) 
    def porown(self,a,b):
        self.a=a
        self.b=b
m = zesp(2,3)
k = zesp(4,5)
y=m+k
print y
print m+k
print m+9
print m-k
print m-9
print m*k
print m*3
print m/k
print m/2
print m.modul()
print k.modul()
print k<m
print k>m
print k==m
print k
