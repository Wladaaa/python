class Kolo:
    __rozm = None
    __stan = None
    def __init__(self, rozm):
        self.__rozm=rozm
    def zepsucSia(self):
        __stan="Bad"
    def zostacNaprawione(self):
        __stan="Good"
class Silnik:
    __stanPracy = None
    __marka = None
    def __init__(self, marka):
        self.__marka=marka
    def zmienicStanPracyNaAktywny(self):
        self.__stanPracy="Aktywny"
    def zmienicStanPracyNaPasywny(self):
        self.__stanPracy="Pasywny"
    def pokazStanPracy(self):
        return self.__stanPracy
class Swiatlo:
    __tryb = None
    __kolor = None
    def __init__(self, color):
        self.__kolor = color
    def Wlacz(self):
        self.__tryb = 1
    def Wylacz(self):
        self.__tryb = 0
class Samochod(Swiatlo, Silnik, Kolo):
    def __init__(self,kolo, swiatlo, silnik, marka):
        super(Samochod, self).__init__(kolo)
myCar = Samochod('a','d','d','d')
