for x in range(2, 10):
    s = 1234
    a = ''
    while s > 0:
        a+=str(s%x)
        s = s//x
    print(sum(int(i) for i in a), x)
