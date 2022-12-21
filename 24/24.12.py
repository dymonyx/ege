s = open('24-12.py').readline()
c = m = 0
for  j in 0,1:
    c = 0
    for i in range(j, len(s)-1, 2):
        if s[i] + s[i+1] == 'AA' or s[i] + s[i+1] == 'CC':
            c+=1
            m = max(m,c)
        else:
            c = 0
print(m)
