from itertools import product
k = 1
for x in product('елмру', repeat = 4):
    s = ''.join(x)
    if s[0] == 'л':
        print(k, s)
    k+=1
