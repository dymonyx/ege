def f(curr, end):           #не проходя через число
    if curr > end or curr == 4: return 0
    if curr == end: return 1
    if curr < end: return f(curr+1, end) + f(curr*2, end)
print(f(2, 16))
