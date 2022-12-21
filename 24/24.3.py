#1
s = open('24-3.txt').readline()
s = s.replace('E', ' ').replace('B', ' ')
print(max(len(c) for c in s.split()))

#2
s = open('24-3.txt').reapline()
c = m = 0
for i in range(len(s)):
    if s[i] in 'ACDF':
        c+=1
        m = max(c,m)
    else:
        c = 0
print(m)
