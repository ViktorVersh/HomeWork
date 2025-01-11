# import random
import sqlite3

connection = sqlite3.connect("Products.db")
cursor = connection.cursor()


def initiate_db():
    """
    Создаёт базу данных если её ещё нет
    """
    connection1 = sqlite3.connect("Products.db")
    cursor1 = connection1.cursor()

    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Products
        (id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL);
    """)

    cursor1.execute("""
    CREATE TABLE IF NOT EXISTS Users
        (id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL);
    """)
    # =======Заполняем таблицу Products после чего комментируем=====
    # for i in range(1, 5):
    #     cursor1.execute("INSERT INTO Products(title, description, price) VALUES(?, ?, ?)",
    #                    (f'Product {i}', f'Описание {i}', f'{100 * i}'))

    # =======Заполняем таблицу Users после чего комментируем=====
    # for i in range(1, 30):
    #     cursor1.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                    (f'User {i}', f'user{i}@mail.ru', f'{random.randint(20, 60)}', f'{1000}'))
    connection1.commit()
    cursor1.close()


def get_all_products():
    """
    Получаем список всех товаров из таблицы
    :return: список товаров
    """
    connection2 = sqlite3.connect("Products.db")
    cursor2 = connection2.cursor()
    cursor2.execute("SELECT title, description, price FROM Products")
    products = cursor2.fetchall()
    product = []
    for i in products:
        product.append(f'Название товара: {i[0]}, Описание: {i[1]}, Цена: {i[2]}')
    cursor2.close()
    return product


def add_users(username, email, age):
    """
    Добавляем пользователя в таблицу
    :param username:
    :param email:
    :param age:
    :return: строка с именем добавленного пользователя
    """
    connection3 = sqlite3.connect("Products.db")
    cursor3 = connection3.cursor()
    cursor3.execute(f"INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)",
                    (username, email, age, 1000))
    connection3.commit()
    return f'Регистрация пользователя {username} прошла успешно'


def is_included(username):
    """
    Проверяем пользователя по базе данных
    :param username:
    :return: True если пользователь есть в таблице иначе False
    """
    connection4 = sqlite3.connect("Products.db")
    cursor4 = connection4.cursor()
    cursor4.execute("SELECT username FROM Users")
    users = cursor4.fetchall()
    for i in users:
        if i[0] == username:
            cursor4.close()
            return True
    cursor4.close()
    return False


connection.commit()
connection.close()

if __name__ == '__main__':
    initiate_db()
    print(get_all_products())
    print(is_included('User 30'))
