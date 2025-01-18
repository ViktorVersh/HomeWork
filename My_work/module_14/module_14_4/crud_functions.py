import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()


def initiate_db():
    """
    Создаёт базу данных если её ещё нет
    :return:
    """
    connection1 = sqlite3.connect("Products.db")
    cursor1 = connection1.cursor()
    cursor1.execute("""
        CREATE TABLE IF NOT EXISTS Products
        (id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL)
    """)
    # =======Заполняем таблицу после чего комментируем=====
    # for i in range(1, 5):
    #     cursor1.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
    #                    (f'Product {i}', f'Описание {i}', f'{100 * i}'))
    connection1.commit()


def get_all_products():
    """
    Получаем список всех товаров из таблицы
    :return:
    """
    connection2 = sqlite3.connect("Products.db")
    cursor2 = connection2.cursor()
    cursor2.execute("SELECT title, description, price FROM Products")
    products = cursor2.fetchall()
    product = []
    for i in products:
        product.append(f'Название товара: {i[0]}, Описание: {i[1]}, Цена: {i[2]}')
    connection2.commit()
    return product


connection.commit()
connection.close()

if __name__ == '__main__':
    initiate_db()
    print(get_all_products())
