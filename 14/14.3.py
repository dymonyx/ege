for i in range(1000):   #если питон не дает ответа, увеличиваем range
    a = ''
    x = 125**200 - 5**i +74
    while x >0:
        a+= str(x%5)
        x=x//5
    if a.count('4') == 100:
        print(i)
