#Разработать программу с применением пакета tk, взяв в качестве условия одну
#любую задачу из ПЗ №№ 3 – 8.

# Даны числа X, Y. Проверить истинность высказывания «Точка с координатами (X, Y)
# лежит в четвёртой координатной четверти».

from tkinter import *

def proverka():
    X = coordinatX.get()
    Y = coordinatY.get()
    try:
        X = int(X)
        Y = int(Y)
        coordinat()
    except ValueError:
        iotg['text'] = 'Неверные еденицы данных'
        coordinatX.delete(0, END)
        coordinatY.delete(0, END)


def coordinat():
    X = coordinatX.get()
    Y = coordinatY.get()
    X = int(X)
    Y = int(Y)

    if X > 0 and Y < 0:
        iotg['text'] = f'Координаты ({X};{Y}) лежат в \n четвёртой координатной четверти.'
        coordinatX.delete(0, END)
        coordinatY.delete(0, END)
    else:
        iotg['text'] = f"Координаты ({X};{Y})  не лежат в \n четвёртой координатной четверти."
        coordinatX.delete(0, END)
        coordinatY.delete(0, END)

root = Tk()
root.geometry('300x200')
root.config(bg='gray')
root.resizable(height=False,width=False)
root.title('Практическая работа 12 №2')

zadacha = Label(text='Даны числа X, Y. Проверить истинность \n высказывания «Точка с координатами (X, Y) \n лежит в \
четвёртой координатной четверти»')
zadacha.grid(row=0, columnspan=2, stick='wens')

coordinatX_text = Label(root, text='Введите координату X : ')
coordinatY_text = Label(root, text='Введите координату Y : ')
coordinatX_text.grid(row=1, column=0, pady=5, stick='wens')
coordinatY_text.grid(row=2, column=0, pady=5, stick='wens')

coordinatX= Entry(root)
coordinatY= Entry(root)
coordinatX.grid(row=1, column=1, stick='wens', pady=5)
coordinatY.grid(row=2, column=1, stick='wens', pady=5)

iotg = Button(text='Нажмите чтобы узнать к какой \n четверти относится точка.', bd=5, font=('Arial', 12), fg='blue',
              command= lambda : proverka())
iotg.grid(row=3, columnspan=2, stick='wens', padx= 5, pady=5)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=20)
root.grid_rowconfigure(2, minsize=20)
root.grid_rowconfigure(3, minsize=80)

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=150)

root.mainloop()