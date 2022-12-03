def f(x, y):
    return int( x + '23' + x + '5', 22) - int('67' + y + '9' + y, 13)
#ЧИСЛО НЕ МОЖЕТ НАЧИНАТЬСЯ С НУЛЯ
for x in '0123456789ABCDEFGHIJK':
    for y in '0123456789ABC':
        if f(x, y) % 57 == 0:
            print(f(x, y)/57, x, y)
