# Дан целочисленный список A размера N (< 15). Переписать в новый целочисленный список B все элементы с нечетными
# порядковыми номерами (1,3,...) и вывести размер полученного списка B и его содержимое.
# Условный оператор не использовать.

N = int(input("N:"))    # Ввод длины списка
while N > 14:
    N -=1

A = []
for i in range(N):      # функция позволяющая заполнить список вручную
    A.append(int(i) + 1)

print("Данный список A = ",A)

G = len(A)

B =[]
K = 0
while G > 0:
    K += 1
    B.append(K)
    K += 1
    G -= 2

print("новый список с нечётными элементами первого списка = ",B)
print("Размер полученного списка = ",len(B))
