import sqlite3


def initiate_db():
    """
    Создаёт базу данных если её ещё нет
    :return:
    """
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("""
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

    connection.commit()
    cursor.close()
    connection.close()


def get_all_products():
    """
    Получаем список всех товаров из таблицы
    :return:
    """
    connection = sqlite3.connect("Products.db")
    cursor = connection.cursor()
    cursor.execute("SELECT title, description, price FROM Products")
    products = cursor.fetchall()
    product = []
    for i in products:
        product.append(f'Название товара: {i[0]}, Описание: {i[1]}, Цена: {i[2]}')
    connection.commit()
    cursor.close()
    return product


if __name__ == '__main__':
    connection = sqlite3.connect("Products.db")
    initiate_db()
    print(get_all_products())
    connection.close()
