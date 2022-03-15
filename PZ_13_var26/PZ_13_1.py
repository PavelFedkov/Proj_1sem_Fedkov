from random import *
while True:
    a = int(input("Введите размер списка: "))
    if a % 2 == 0:
        break
spisok = [randint(0, 20) for n in range(a)]
spisok = [f for f in spisok[a//2:] if f > 10]
print("Сумма чисел второй половины списка, что больше 10 равна:", sum(spisok))