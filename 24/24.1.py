s = open('24-1.txt').readline()
s = s.replace('A', ' ').replace('B', ' ')
print(max(len(c) for c in s.split()))
