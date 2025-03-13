"""
Постой консольный калькулятор.
"""
from decimal import Decimal
while True:
    print()
    print('*' * 15, ' калькулятор ', '*' * 15)
    print('*' * 4, 'Для выхода из программы введите "q"', '*' * 4)
    print()
    a = input('Введите математическое действие "+", "-", "*", "/" ')
    if a == 'q':
        break
    elif a in ('+', '-', '*', '/'):
        b = Decimal(input('Введите первое число '))
        c = Decimal(input('Введите второе число '))
        if a == '+':
            print(Decimal(b + c))
        elif a == '-':
            print(Decimal(b - c))
        elif a == '*':
            print(Decimal(b * c))
        elif a == '/':
            if c == 0:
                print('Делить на ноль нельзя!')
            else:
                print(Decimal(b / c))
    else:
        print('Вы ввели не верное математическое действие ')
