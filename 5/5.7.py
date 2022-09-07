for n in range(30,100):
    k = n
    a = ''
    while k >0:
        a += str(k%3)
        k = k //3
    a = a[::-1]
    a += str(n%3)
    print(int(a,3))
