import sqlite3  # Импорт библиотеки для работы с базой данных
from faker import Faker  # Импорт библиотеки для генерации фиктивных данных

# Создаем объект Faker
faker = Faker(locale='ru_RU')

def generate_fake_data(count):
    """
    Функция для создания списка фиктивных данных состоящего из словарей
    :param count: Количество фиктивных данных
    :return:
    """
    data = []  # Создаем пустой список
    for _ in range(count):
        person = {
            'name': faker.name(),
            'address': faker.address(),
            'postal_code': faker.postcode(),
            'phone_number': faker.phone_number()
        }  # Цикл создания словаря с фиктивными данными
        data.append(person)  # Добавляем словарь в список
    return data


def create_database_table(conn):
    """
    Функция для создания таблицы в базе данных, если она не существует
    :param conn: Соединение с базой данных
    :return:
    """
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS People (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            postal_code TEXT,
            phone_number TEXT
        )
    ''')
    conn.commit()


def insert_data_into_database(conn, data):
    """
    Функция для записи созданных фиктивных данных в таблицу базы данных
    :param conn: Соединение с базой данных
    :param data: Список фиктивных данных
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM People")
    query = '''
        INSERT INTO People (name, address, postal_code, phone_number)
        VALUES (:name, :address, :postal_code, :phone_number)
    '''
    cursor.executemany(query, data)
    cursor.execute("SELECT * FROM People")
    for i in cursor.fetchall():
        print(i)
    conn.commit()


if __name__ == "__main__":
    # Подключение к базе данных SQLite
    conn = sqlite3.connect('example.db')

    # Создание таблицы, если она не существует
    create_database_table(conn)

    # Генерация фиктивных данных
    fake_data = generate_fake_data(100)

    # Запись данных в таблицу базы данных
    insert_data_into_database(conn, fake_data)

    # Закрытие соединения с базой данных
    conn.close()

    print("Данные успешно сохранены в базу данных!")