# В матрице найти среднее арифметическое положительных элементов.
from random import *

a = int(input("Кол-во строк матрицы: "))
b = int(input("Кол-во столбцов в матрице: "))

matr = [[randint(-10,10) for j in range(a)] for i in range(b)]
polch = []
for i in matr:
    print(i)
    for j in i:
        if j >= 0:
            polch.append(j)
print("среднее арифметическое положительных элементов: ", round(sum(polch)/len(polch), 2))