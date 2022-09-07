for N in range(1,100):
    b = bin(N)[2:]
    b  += b[-1]
    if bin(N).count('1')%2!=0:
        b+= '1'
    else: b+= '0'

    if b.count('1')%2!=0: b+='1'
    else: b+= '0'

    if int(b,2)>90:
        print(N)
        
