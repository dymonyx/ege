#1
s = open('24-10.txt').readline()
s = s.replace('ZX', '*').replace('ZY', '*')
s = s.replace('X', ' ').replace('Y', ' ').replace('Z', ' ')
print(max(len(c) for c in s.split()))

#2
s = open('24-10.txt').readline()
c = m = 0
for i in range(0, len(s)-1, 2):
    if s[i] + s[i+1] == 'ZY' or s[i] + s[i+1] == 'ZX':
        c+=1
        m = max(m, c)
    else:
        c = 1
print(m)

s = open('24-10.txt').readline()
c = m = 0
for i in range(1, len(s)-1, 2):
    if s[i] + s[i+1] == 'ZY' or s[i] + s[i+1] == 'ZX':
        c+=1
        m = max(m, c)
    else:
        c = 1
print(m)
