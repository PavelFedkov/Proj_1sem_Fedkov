#Даны строки S и S0. Удалить из строки S все подстроки, совпадающие с S0. Если совпадающих подстрок нет,
#то вывести строку S без изменений.

S = input("Введите строку: ")
S0 = input("Введите строку: ")

print(S.replace(S0,""))