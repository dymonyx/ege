x = 2*27**7 + 3**10 - 9
a = ''
while x>0:
    a+= str(x%3)         #какая система исчиления, то число и пишем(3)
    x = x//3             #какая сс, то число и пишем (3)
print(a.count('0'))