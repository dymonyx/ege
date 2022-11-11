#№ 47247 решуегэ


def f(x):
    return 3**0.5/3 * x
def f1(x):
    return -3**0.5/3 * x + 6
k = 0

for x in range(1,6):
    for y in range(1,6):
        if y > f(x) and y < f1(x):
            k+=1
print(k)
