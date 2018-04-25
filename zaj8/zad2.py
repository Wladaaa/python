#!/usr/bin/env python
import subprocess
dirStr = '''K1
    K2
    K3
        K4
K5
    K6'''
stopien = -1
poprz = ""
for i in dirStr.splitlines():
    if (stopien >= i.count('    ') and i.count('    ') !=-1 and i.count('    ') !=0):
        print ("Tak")
        poprz = poprz[0:len(poprz)-3]
        poprz += "/"+i[i.count('    ')*4]+i[i.count('    ')*4+1]
    if (stopien < i.count('    ') and i.count('    ') !=-1 and i.count('    ') !=0):
        print (stopien)
        print (i.count('    '))
        poprz += "/"+i[i.count('    ')*4]+i[i.count('    ')*4+1]
    if(i.count('    ') ==0 or i.count('    ') == -1):
        poprz += i[i.count('    ')*4]+i[i.count('    ')*4+1]
    print ("mkdir "+poprz)
    #subprocess.check_call(["mkdir "+poprz], shell=True)
    #print("mkdir "+poprz+i[i.count('    ')*4]+i[i.count('    ')*4+1])
    
    stopien  = i.count('    ')
    print (poprz)
    print (stopien)
    
    
