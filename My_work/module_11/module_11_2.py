class Guest:
    """Создаем класс Guest в качестве примера для проверки
    работоспособности функции introspection_info(obj)
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Гость {self.name}, возраст  {self.age} лет'


guest = Guest('Игорь', 36)  # Создаем объект класса Guest


def introspection_info(obj):
    """Функция принимает объект и возвращает словарь
    с информацией об этом объекте
    """
    try:
        return {'type': type(obj),
                'attributes': [x for x in dir(obj) if not str(x).startswith('__')],
                'methods': [x for x in dir(obj) if callable(getattr(obj, x))],
                'module': obj.__module__}
    except AttributeError:
        return type(obj)  # В случае ошибки возвращаем тип объекта


# выводим результат работы функции introspection_info

print(introspection_info(Guest))
print(introspection_info(Guest.__str__))
print(introspection_info(guest))
print(introspection_info(guest.name))
print(introspection_info("Привет"))
print(introspection_info(45))
print(introspection_info(45.3))
