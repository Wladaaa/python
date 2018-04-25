#!/usr/bin/env python
import subprocess, os
try:
    with open(os.devnull, 'w') as devnull:
        subprocess.check_call(["g++ p.cpp -o p"], stderr = devnull, shell=True)
    subprocess.check_call(["./p"], shell=True)
except subprocess.CalledProcessError as ex:
    print (ex)
