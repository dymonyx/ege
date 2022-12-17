def f(curr, end):
    if curr > end or (curr%10 == 3) or int(str(curr)[0]) == 3: return 0
    if curr == end: return 1
    if curr < end: return f(curr+1, end) + f(curr*2, end)
print(f(1, 40))
