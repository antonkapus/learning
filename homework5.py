p = int(input('Какая у вас выручка '))
e = int(input('Какие у вас издержки '))
d = (p-e)/p
if p > e:
    print('Вы в плюсе')
    print('Ваша рентабильность',d)
    k = int(input('Кол-во ваших сотрудников '))
    с = (p - e) / k
    print('Прибыль фирмы в расчете на одного сотрудника ',с)
else:
    print('Вы в минусе')
