	for x in range(100):
    try:
        a = int('123'+str(x)+'5', 15) + int('1'+str(x)+'233', 15)
        if a % 14 == 0:
            print(a/14)
    except:
        pass
