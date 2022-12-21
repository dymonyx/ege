s = open('24-15.txt').readline()
for x in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    s = s.replace(x, ' ')
s = list(s.split())
m = 1000000000
for i in range(len(s)):
    if int(s[i])%2 == 0:
        m = min(int(s[i]), m)
print(m)
