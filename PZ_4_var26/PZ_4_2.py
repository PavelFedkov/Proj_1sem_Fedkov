#Дано целое число N (> 1). Вывести наибольшее из целых чисел K, для которых сумма 1 + 2 + ... + K
#будет меньше или равна N, и саму эту сумму.

N = input("Введите число (N): ")
K = 0
SUMM = 0
while True:
    try:
        N = int(N)
        break
    except ValueError:
        print("Неверная единица данных")
        N = input("Введите число (N): ")

while True:
    if N > 1:
        while SUMM <= N:
            K += 1
            SUMM += K

        SUMM -= K
        K -= 1

        print("К =",K)
        print("Сумма чисел до",K,"равна",SUMM)
        break

    else:
        print("Неверное число")
        N = input("Введите число (N): ")

        while True:
            try:
                N = int(N)
                break
            except ValueError:
                print("Неверная единица данных")
                N = input("Введите число (N): ")
