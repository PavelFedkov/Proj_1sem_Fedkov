# В матрице элементы первого столбца возвести в куб.
from random import *

a = int(input("Кол-во строк матрицы: "))
b = int(input("Кол-во столбцов в матрице: "))
n = int(input("Нужный столбец: "))
print("Старая матрица:")
matr = [[randint(-10,10) for j in range(a)] for i in range(b)]
for d in matr:
    print(d)
print('\n', "Новая матрица:")
for i in matr:
    i[n-1] = i[n-1]**3
    print(i)