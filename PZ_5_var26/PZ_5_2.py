#Описать функцию InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный
#(K — параметр целого типа, являющийся одновременно входным и выходным). С помощью этой функции поменять порядок
#следования цифр на обратный для каждого из пяти данных целых чисел.
import math
def InvertDigits(K):              # Функция
    p = 0
    while K != 0:                 # Цикл инверсии числа
        p = p * 10 + math.fmod(K,10)
        K = int(K / 10)
    return p

K = input("Введите порядок чисел: ")
while K != int:                 # Проверка на число
    try:
        K = int(K)
        break
    except ValueError:
        print("Неверные единицы данных")
        K = input("Введите число: ")

print("Обратный порядок цифр: ", int(InvertDigits(K)))
                                  # Вызов функции