def f(curr, end): #найти конечное число
    if curr > end: return 0
    if curr == end: return 1
    if curr < end: return f(curr + 1, end) + f(curr + 5, end) + f(curr * 3, end)

for i in range(2, 1000):
    if f(1, i) == 175:
        print(i)
