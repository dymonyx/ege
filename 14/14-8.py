def f(x, y):
    return int('131' + x + '1', 15) + int('13' + y + '3', 17)

for x in '0123456789ABCDE':
    for y in '0123456789ABCDEFG':
        if f(x, y) % 11 == 0:
            print(f(x, y)/11, x, y)
