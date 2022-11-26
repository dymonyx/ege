s = open('24 - 1.txt').readline()
maxx = 0
mas = list(s.split())
for i in range(len(mas)):
    maxx = max(maxx, len(mas[i]))
print(maxx)
