from itertools import product      #product - итератор для составления всех возможных слов
k = 0
for x in product('сало',repeat = 6): #значение после repeat - скольки буквенное слово требуется
    s = ''.join(x)
    if 1 <= s.count('о') <= 3:
        k+=1
print(k)
