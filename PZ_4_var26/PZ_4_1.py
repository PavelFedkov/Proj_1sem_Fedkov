#Даны два целых числа A и B (A < B). Вывести в порядке убывания все целые числа, расположенные между A и B
#(не включая числа A и B), а также количество N этих чисел.

A = input("Введите число (A): ")
B = input("Введите число (B): ")

#Счётчик
N = 0
# Проверка на ввод числа не буквы.
while True:
    try:
        A = int(A)
        B = int(B)
        break
    except ValueError:
        print("Неверная единица данных")
        A = input("Введите число (A): ")
        B = input("Введите число (B): ")

#Цикл с действием
while True:
    if A < B:
        print("Перечень чисел")
        while B != A+1:
            B -= 1
            N += 1
            print(B)
        print("Количество чисел =", N)
        break
    else:
        print("Попробуйте поменять местами")
        A = input("Введите число (A): ")
        B = input("Введите число (B): ")

        while True:
            try:
                A = int(A)
                B = int(B)
                break
            except ValueError:
                print("Неверная единица данных")
                A = input("Введите число (A): ")
                B = input("Введите число (B): ")
