from itertools import product
k = 0
for x in product('0123456789', repeat = 3):
    s = ''.join(x)
    if s[0]!= '0' and int(s[0]) <= int(s[1]) <= int(s[2]): #число не может начинаться с нуля, ноль обязательно в кавычках
        k+=1
print(k)
