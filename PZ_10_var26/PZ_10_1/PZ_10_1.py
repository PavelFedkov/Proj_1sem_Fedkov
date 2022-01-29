# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

# Элементы первого и второго файлов:
# Элементы первого файла, отсутствующие во втором:
# Элементы второго файла, отсутствующие в первом:
# Количество элементов:
# Индекс первого минимального элемента:
# Индекс последнего максимального элемента:
from random import *

spisok1 = []
spisok2 = []

for i in range(randint(3, 10)):
    spisok1.append(randint(-9, 9))

for i in range(randint(3, 10)):
    spisok2.append(randint(-9, 9))

File1 = open("File1.txt", "w+")
print(str(spisok1).strip("[]"), file=File1)
File1.close()

File2 = open("File2.txt", "w+")
print(str(spisok2).strip("[]"), file=File2)
File2.close()

vso = spisok1 + spisok2
ot1 = []
ot2 = []
chet = 0

for i in spisok1:
    for r in spisok2:
        if i != r:
            chet += 1
    if chet == len(spisok2):
        ot1.append(i)
    chet = 0

for i in spisok2:
    for r in spisok1:
        if i != r:
            chet += 1
    if chet == len(spisok1):
        ot2.append(i)
    chet = 0

File3 = open("New_File.txt", "w+")
print("Содержимое первого и второго файла:", str(vso).strip("[]"), file=File3)
print("Элементы первого файла, отсутствующие во втором:", str(ot1).strip("[]"), file=File3)
print("Элементы второго файла, отсутствующие во втором:", str(ot2).strip("[]"), file=File3)
print("Количество элементов:", len(vso), file=File3)
print("Индекс первого минимального элемента:", vso.index(min(vso)), file=File3)
print("Индекс последнего максимального элемента:", vso.index(max(vso)), file=File3)
File3.close()