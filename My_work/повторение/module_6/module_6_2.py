class Vehicle:
    _COLOR_VARIANTS = ['red', 'blue', 'green', 'white', 'black']
    def __init__(self, owner: str, _model: str, _color: str , _engine_power: int):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        return f'Модель: {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def set_color(self, new_color: str):
        if new_color.lower() in self._COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец имя: {self.owner}')



class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

