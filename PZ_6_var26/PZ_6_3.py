# Дано множество A из N точек (N > 2, точки заданы своими координатами x, у). Найти такую точку из данного множества,
# сумма расстояний от которой до остальных его точек минимальна, и саму эту сумму.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#                             R = √(x2 – x1)^2 + (у2 – y1)^2
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый список для хранения абсцисс,
# второй — для хранения ординат.

from math import *    # Импорт функций из библиотеки math

N = int(input("Введите кол-во точек: "))
X = []
Y = []
for i in range(N):   # Функция позволяющая пользователю ручной ввод
    X.append(int(input("Введите координату X" + str(i + 1) + ":")))
    Y.append(int(input("Введите координату Y" + str(i + 1) + ":")))

sum =[]              # Список сумм

for h in range(N):   # Функция нахождения сумм расстояний
    S = 0
    for i in range(N - 1):
        R = (sqrt(pow((X[0] - X[i+1]),2) + pow((Y[0]-Y[i+1]),2)))
        S += R

    X.append(X[0])   # Прокрутка списка координат
    Y.append(Y[0])
    X = X[1:]
    Y = Y[1:]
    sum.append(round(S , 2)) # Ввод в список сумм с округлением до сотых
print("Минимальная сумма расстояний: ",min(sum))
print("Координаты точки: (", X[sum.index(min(sum))],";",Y[sum.index(min(sum))],")")

