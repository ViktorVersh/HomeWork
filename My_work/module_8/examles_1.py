def f1(number):
    return 10 / number


def f2():
    print('Какой хороший день!')
    summ = 0
    try:
        for i in range(-2, 2):
            summ += f1(i)
            print(summ)
        # return summ
    except ZeroDivisionError as exc:
        print(f'Вот что пошло не так - "{exc}", но программа ещё жива')  # Отрабатывает ошибку внутри функции
    return summ


try:
    total = f2()
    print(total)
    print(f'Вот ваш результат: {total}')
    print(total / 0)

except ZeroDivisionError as exc:
    print(f'Вот что пошло не так - "{exc}", но мы устояли')  # Отрабатывает ошибку вне функции
