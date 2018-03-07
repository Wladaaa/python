from math import sqrt
a =[ [1,2], [3,4],[1,2], [3,4],[1,2], [3,4]]

def punkcik(n,k):
    res = []
    for i in range(len(n)):
            res.append(((sqrt(((n[i][0]-k[0])**2)+((n[i][1]-k[1])**2))),((n[i][0]), (n[i][1]))))
    res.sort()
    return res
    
print punkcik(a,[1,1])