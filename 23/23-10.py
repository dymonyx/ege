def f(curr, end, amount): #количество команд
    if curr > end: return 0
    if curr == end and amount == 6: return 1
    if curr == end and amount != 6: return 0
    if curr < end: return f(curr + 2, end, amount+1) + f(curr + 1, end, amount+1) + f(curr * 2, end, amount+1)

print(f(1, 20, 0))
