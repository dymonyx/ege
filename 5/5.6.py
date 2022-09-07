for n in range(1000,10000):
    k = str(n)
    r = int(k[0]) + int(k[2])
    c = int(k[1]) + int(k[3])
    if r > c: k = str(c) + str(r)
    else: k = str(r) + str(c)
    if k == '1113':
        print(n)
        break
