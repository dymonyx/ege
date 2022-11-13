#функция првоеряет, можно ли выиграть за m ходов
def f(s, c, m):
    #если игра окончена, то кол-во ходов должно иметь ту же четность, что и m
    if s >= 30: return  c%2 == m%2
    #если игра не окончилась за m ходов - Забиваем
    if c == m: return 0
    #смотрим след. ходы
    h = [f(s+2, c + 1, m), f(s+3, c + 1, m), f(s*2, c + 1, m)]
    #если это ход главного игрока, то достаточно any (победа в одном из вариантов)
    #иначе должны подходить all варианты (везде победа)
    return any(h) if (c+1) % 2 == m % 2 else all(h)

for s  in range(1,30):
    for m in range(1,5):
        if f(s, 0, m) == 1:
            print(s, m)
            break
