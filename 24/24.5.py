#1
s = open('24-5.txt').readline()
s = s.replace('KEGE', 'KEG EGE')
print(max(len(c) for c in s.split()))

#2
s = open('24-5.txt').readline()
c = m = 3
for i in range(len(s)-3):
    if s[i] + s[i+1] + s[i+2] + s[i+3] != 'KEGE':
        c+=1
        m = max(c, m)
    else:
        c = 3
print(m)
