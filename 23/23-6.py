def f(curr, end):          #уменьшение числа
    if curr < end: return 0
    if curr == end: return 1
    if curr > end: return f(curr - 1, end) + f(curr - 3, end) + f(curr//3, end)
print(f(22, 2))
