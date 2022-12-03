for x in '0123456789ABCDE':
    s = int('123'+ x +'5', 15) + int('1' + x + '233', 15)
    if s % 14 == 0:
        print(s/14)
