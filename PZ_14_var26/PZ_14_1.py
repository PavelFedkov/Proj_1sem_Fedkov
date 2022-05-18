# В исходном текстовом файле (Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.

import re

fil = open('Достоевский.txt', 'r', encoding='utf-8')
s = fil.read()
result = re.findall(r'Достоев\w+', s)
result = set(result)
print(result)
fil.close()




