class ProZero(Exception):
    def __init__(self, message, extra_info):
        self.message = message
        self.extra_info = extra_info


def f(a, b):
    if b == 0:
        raise ProZero('Деление на ноль невозможно', {'a': a, 'b': b})
    return a / b

try:
    result = f(10, 0)
    print(result)
except ProZero as e:
    print('Не очень хороший день, мы словили ошибку')
    print(f'сообщение об ошибке{e.message}')
    print(f'Дополнительная информация{e.extra_info}')