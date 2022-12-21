#1
s = open('24-4.txt').readline()
s = s.replace('ST', 'S T')
print(max(len(c) for c in s.split()))

#2
s = open('24-4.txt').readline()
c = m = 1
for i in range(len(s)-1):
    if s[i] + s[i+1] != 'ST':
        c+=1
        m = max(m, c)
    else:
        c = 1
print(m)
