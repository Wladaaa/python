#!/usr/bin/env python
#encoding: utf-8
napisUnicode = u'Zażycie c cos tam'
napisStr = napisUnicode.encode('utf8') 
print len(napisUnicode)
print len(napisStr)

napisStr = 'Zażycie c cos tam'
napisUnicode = napisStr.decode('utf8')

print len(napisUnicode)
print len(napisStr)

print (isinstance(napisStr, basestring))
print (isinstance(napisUnicode, basestring))

newString = '        TESTTTTT    '
print newString
print newString.strip().center(30)
print newString.strip().capitalize()
print newString.lower()
print newString.islower()
newString = newString.strip()
print newString.startswith('TESTTTTT')
print newString.ljust(30)

newS = u'Test test'
print newS.title().istitle()
print newS.istitle()

print 'test' in newS
print newS.replace('test', 'XYZ')
