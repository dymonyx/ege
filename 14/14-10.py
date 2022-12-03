for x in range(1, 1000):
    s = 343**5 + 7**3 - 1 - x
    a = ''
    while s > 0:
        a+=str(s%7)
        s = s//7
    if a.count('6') == 12:
        print(x)
        break
