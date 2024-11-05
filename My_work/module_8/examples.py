try:
    print(a + b)
    i = 0
    print(10 / i)
    print('сделано')

except ZeroDivisionError as exp:
    print(f'ошибка {exp} на ноль делить нельзя')

except NameError as exp1:
    print(f'ошибка {exp1} переменная не задана')
