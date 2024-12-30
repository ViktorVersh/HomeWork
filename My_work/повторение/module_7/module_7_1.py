class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weigth = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigth}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            products = file.read()
            return products

    def add(self, *products):
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for i in products:
                if i.name not in self.get_products():
                    file.write(f'{i}\n')
                else:
                    print(f'Продукт {i.name} уже был в магазине, его общий вес теперь равен {i.weigth}')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
