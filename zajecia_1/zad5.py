n = input('Podaj ilosc liczb')
r = [];
for i in range(int(n)):
    pom = input()
    r.append(int(pom));
bl = input('Wybierz kierunek sortowania(1-od najw., 0-od najmn)')
if int(bl)==0:
 r.sort()
else:
 r.sort(reverse=True)
bl = input('Od ktorego wyswietlic?')
i = int(bl)
bl = input('Do ktorego wyswietlic?')
for i in range(int(bl)+1):
    print(r[i])