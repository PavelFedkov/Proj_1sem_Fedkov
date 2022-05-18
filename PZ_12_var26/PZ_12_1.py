# https://web-programmist.ru/news/2/2.jpg
# Простите но мой максимум породии интерфейса вот он
from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Практическая работа 12 №1")
root.geometry("1000x800+450+100")
root.resizable(height=False, width=False)

zagalovok = Label(root, text='Параметры скидки', font=('Arial', 20), padx=20, pady=10, bd=1)
zagalovok.grid(row=0, column=0, stick='nw')

aktivnost = Label(root, text='Активность: ', font=('Arial', 14))
aktivnost2 = Checkbutton(root)
aktivnost.grid(row=1, column=0, stick='e')
aktivnost2.grid(row=1, column=1, stick='w')

nazvanie = Label(root, text='Название: ', font=('Arial', 14))
nazvanie2 = Entry(root, width=50)
nazvanie.grid(row=2, column=0, stick='e')
nazvanie2.grid(row=2, column=1, stick='w')

sait = Label(root, text='Сайт: ', font=('Arial', 14))
sait2 = Combobox(root, values=('(s1) Моя компания', 'Что-то ещё'))
sait2.current(0)

sait.grid(row=3, column=0, stick='e')
sait2.grid(row=3, column=1, stick='w')

period = Label(root, text='Тип скидки: ', font=('Arial', 14))
period2 = Combobox(root, values=('В процентах', 'Что-то ещё'))
period2.current(0)

period.grid(row=4, column=0, stick='e')
period2.grid(row=4, column=1, stick='w')

Velich_skidki = Label(root, text='Величина скидки: ', font=('Arial', 14))
Velich_skidki2 = Entry(root, width=20)
Velich_skidki.grid(row=5, column=0, stick='e')
Velich_skidki2.grid(row=5, column=1, stick='w')

valuta = Label(root, text='Валюта скидки: ', font=('Arial', 14))
valuta2 = Combobox(root, values=('RUB', 'Что-то ещё'), width= 5)
valuta2.current(0)

valuta.grid(row=6, column=0, stick='e')
valuta2.grid(row=6, column=1, stick='w')

max_summa_skidki = Label(root, text='Максимальная сумма скидки (в валюте скидки; \n'
                                    '0 - скидка не ограничена) : ', font=('Arial', 12))
max_summa_skidki2 = Entry(root, width=20)
max_summa_skidki2.insert(0,'0')
max_summa_skidki.grid(row=7, column=0, stick='e')
max_summa_skidki2.grid(row=7, column=1, stick='w')

opisanie = Label(root, text='Краткое описание (до 255 символов): ', font=('Arial', 14))
opisanie2 = Entry(root, width=50)
opisanie.grid(row=8, column=0, stick='ne')
opisanie2.grid(row=8, column=1, stick='wens')

root.grid_columnconfigure(0, minsize=400)
root.grid_columnconfigure(1, minsize=400)

root.grid_rowconfigure(0, minsize=100)
root.grid_rowconfigure(8, minsize=200)
root.mainloop()
