#! /usr/bin/env
import math

def pierv(x):
    try:
        res = math.sqrt(x)
        return res
    except(ValueError):
        print("ERROR: Nie da sie policzyc pierwiastku z liczb ujemnych!")
    except(TypeError):
        print("ERROR: Nie da sie policzyc pierwiastku z stringu!")
print (pierv(3/4000))
print (pierv(4))
print (pierv(0.3535345))
print (pierv(-4))
print (pierv("test"))
