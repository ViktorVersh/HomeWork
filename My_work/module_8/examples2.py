def greet_persons(names):
    try:
        if names == 'ВоланДеМорт':
            raise Exception(f'Мы не любим тебя, ВоланДеМорт')
    except Exception:
        print('Мы не любим тебя ВоланДеМорт')
    else:
        print(f'Приветствуем тебя {names}')


def greet_pers(name):
    try:
        if name == 'Привет там':
            raise NameError('Привет там')
    except NameError as exc:
        print(f'исключение типа {type(exc)}, пролетело мимо. Его параметры {exc.args}')
    else:
        print(f'Здравствуйте {name}')
        

greet_persons('Добрый человек')
greet_persons('ВоланДеМорт')
greet_pers('Привет там')
greet_pers('Наш ученик')
