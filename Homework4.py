p = int(input('Введите число '))
a = p%10
p = p//10
while p > 0:
    if p%10 > a:
        a = p%10
    p = p//10
print(a)
