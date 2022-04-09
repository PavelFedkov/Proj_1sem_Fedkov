# В матрице найти среднее арифметическое положительных элементов.
from random import *

a = int(input("Кол-во строк матрицы: "))
b = int(input("Кол-во столбцов в матрице: "))

matr = [[randint(-10,10) for j in range(b)] for i in range(a)]
for i in matr:
    print(i)
polch = [matr[i][j] for i in range(a) for j in range(b) if matr[i][j] >= 0]
print("среднее арифметическое положительных элементов: ", round(sum(polch)/len(polch), 2))