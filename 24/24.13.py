s = open('24-13.txt').readline()
s = s.split('.')
m = 0
for i in range(len(s)-2):
    c = s[i] + '.' + s[i+1] + '.' + s[i+2]
    m = max(len(c), m)
print(m)
