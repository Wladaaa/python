def ciag_f(n):
        if(n==1 or n==2):
            return 1
        else:
            return ciag_f(n-2)+ciag_f(n-1)
print 'Podaj wartosc'
p = input()
res = [(ciag_f(i)) for i in range (1,p+1)]
print res