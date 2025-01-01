"""
Задача "Некорректность"
"""


class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        self.model = model
        self.__vin = self.__is_valid_vin(__vin)
        self.__numbers = self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if 1000000 <= vin_number <= 9999999 and isinstance(vin_number, int):
            return True
        else:
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            else:
                raise IncorrectVinNumber('Некорректный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        if len(numbers) == 6 and isinstance(numbers, str):
            return True
        elif not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип номера')
        else:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
