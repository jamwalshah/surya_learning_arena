# usemodule.py
import mymath

print(mymath.sum(10, 5))
print(mymath.diff(10, 5))

# usesmodule.py
import mymath as ma # ma is the alias for mymath module within this script

print(ma.sum(10, 5))
print(ma.diff(10, 5))

# usemodule.py
from mymath import * # imports all methods from module using '*'

print(sum(10, 5))
print(diff(10, 5))