from tkinter import *


def add_digit(digit):
    value = calc.get()
    if value[0] =='0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)

def add_delit(delit):
    calc.delete(0, END)
    calc.insert(0, '0')

def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc.delete(0, END)
    calc.insert(0, eval(value))

def make_digit_button(digit):
    return Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))

def make_calc_button(ravno):
    return Button(text=ravno, bd=5, font=('Arial', 13), fg='red', command= calculate)

def make_delit_button(delit):
    return Button(text=delit, bd=5, font=('Arial', 13), fg='blue', command=lambda: add_delit(delit))

root = Tk()
root.title('Калькулятор')
root.geometry('240x305')
root.config(bg='aqua')

calc = Entry(root, justify=RIGHT, font=('Arial', 15))
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick='wens')

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

make_delit_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(0, minsize=65)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()
