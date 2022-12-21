s = open('24-14.txt').readline()
s = s.split('AB')
m = 0
for i in range(len(s) - 22):
    c = 44 #надо проверить еще что два символа входят в начало и конец строки "A...B"
    for j in range(i, i + 22):
        c += len(s[j])
    m = max(c, m)
print(m)
