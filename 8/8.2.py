from itertools import permutations #перебирает слова путем перестановки букв
k = 0
a = ['аи','иа','ао','оа','ау','уа','ио','ои','иу','уи','оу','уо','бк','кб','бл','лб','бн','нб','кл','лк','кн','нк','лн','нл']
for x in permutations('абиколун'): #если нужны уникальные слова, то  set(permutations)
    s = ''.join(x)
    if all(sub not in s for sub in a):
        k+=1
print(k)
