def parz(n):
    if n%2 == 0:
        return 1
    else: 
        return 0

def podz_przez_3(n):
    if n%3 == 0:
        return 1
    else:
        return 0

def fun2(fun1,n):
    res = [(n[i]) for i in range(0,len(n)) if(fun1(n[i]))]
    return res
res1 = fun2(parz,[0,1,2,3,4,5,6,66])
print res1
res1 = fun2(podz_przez_3,[0,1,2,3,4,5,6,66])
print res1