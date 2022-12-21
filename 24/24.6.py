#1
s = open('24-6.txt').readline()
while 'PPPPP' in s:
    s = s.replace('PPP', 'PP PP')
print(max(len(c) for c in s.split()))

#2
s = open('24-6.txt').readline()
c = m = 2
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2] != 'PPP':
        c+=1
        m = max(c, m)
    else:
        c = 2
print(m)
