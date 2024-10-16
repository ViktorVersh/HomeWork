class User:
    __instance = None

    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args = args
        for key, value in kwargs.items():
            setattr(self, key, value)

other = [1, 2, 3, 4]
user = {'name':'Den', 'age':22, 'gender':'male'}

user1 = User(*other, **user)
print(user1.args)
print(user1.name)
print(user1.age)
print(user1.gender)
