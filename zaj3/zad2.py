import math
class Punkt2D(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def odleglosc(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
class Punkt3D(Punkt2D):
    def __init__(self, x, y, z):
        super(Punkt3D, self).__init__(x,y)
        self.z=z
    def odleglosc(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2+(self.z-other.z)**2)
a = Punkt3D(1,2,6)
b = Punkt3D(2,3,6)
print a.odleglosc(b)
