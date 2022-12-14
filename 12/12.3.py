a = []
for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            for w in range(1, 100):
                if 2*x+z == y+2*w:
                    s = '0' + '22'*x + '1'*y + '2'*z + '11'*w + '0'
                    while '00' not in s:
                        s = s.replace('011', '20', 1)
                        s = s.replace('022', '10', 1)
                        s = s.replace('01', '220', 1)
                        s = s.replace('02', '110', 1)
                        if s.count('1') == 40 and s.count('2')>50:
                            a.append(s.count('2'))
print(min(a))
