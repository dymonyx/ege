s = open('24 - 1.txt').readline()
mass = list(s.split())
k = 0
for i in range(len(mass)):
    if mass[i][0] == 'A':
        k+=1
print(k)
