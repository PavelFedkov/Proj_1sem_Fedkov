# Дан список ненулевых целых чисел размера N. Проверить, чередуются ли в нем положительные и отрицательные числа.
# Если чередуются, то вывести 0, если нет, то вывести порядковый номер первого элемента, нарушающего закономерность.

N = int(input("N:"))    # Ввод длины списка
spisok = []
for i in range(N):      # функция позволяющая заполнить список вручную
    spisok.append(int(input("Пордковый номер " + str(i + 1) + " = "))) # i + 1, потому что порядок в списке начинается
                                                                       # с 0, а порядковые номера с 1.

k=0
for i in range(len(spisok) - 1):  # функция вычесляющая порядок списка
    if spisok[i]<0 and spisok[i+1]>=0:
        continue
    elif spisok[i]>=0 and spisok[i+1]<0:
        continue
    else:
        k=i+2
        break
print(k)