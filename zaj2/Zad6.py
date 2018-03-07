#! python
import sys, os
#sys.stdout.write("hello from Python %s\n" % (sys.version,))

path = ""
dirs = os.listdir( path )

for file in dirs:
	print file