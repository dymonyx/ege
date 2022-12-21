from fnmatch import *
for i in range(0, 10**9, 169):
    if fnmatch(str(i), '345*789?'):
        print(i, i//169)
