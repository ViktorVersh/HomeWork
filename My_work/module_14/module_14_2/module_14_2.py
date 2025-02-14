# import random  # Закомментируем после создания записей в базе данных
import sqlite3
from matplotlib import pyplot as plt

"""
Задача "Средний баланс пользователя"
"""

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

try:
    (cursor.execute
     ("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL)
    """))
    # -----------------Комментируем после создания записей в базе данных-----------------------
    # for i in range(10, 30):
    #     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
    #                    (f'User{i}', f'example{i}@gmail.com', str(random.randint(10, 90)),
    #                     str(random.randint(500, 1000))
    #                     ))
    # ------------------------------------------------------------------------------------------

    # cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))  # меняем значение balance
    #
    # cursor.execute("DELETE FROM Users WHERE id % 3 = 1")  # удаляем каждую 3 запись
    #
    # cursor.execute('SELECT * FROM Users WHERE age != 60')  # выбираем записи, у которых возраст не равен 60
    #
    # users = cursor.fetchall()
    #
    # for i in users:
    #     print(f'Имя: {i[1]} | Почта: {i[2]} | Возраст: {i[3]} | Баланс: {i[4]}')

    cursor.execute("DELETE FROM Users WHERE id = 6")  # удаляем запись с id = 6
    # Запрос для получения всех данных о пользователях
    cursor.execute("SELECT username, email, age, balance FROM Users")
    users = cursor.fetchall()

    # Вывод заголовка
    print("--------------------------------------------------------------------")
    print("                     Просмотр базы данных                           ")
    print("--------------------------------------------------------------------")

    # Вывод данных о пользователях
    for user in users:
        print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

    # Подсчет количества пользователей
    count_users = len(users)
    print("--------------------------------------------------------------------")
    print(f"Количество пользователей: {count_users}")

    # Подсчет суммы всех балансов
    sum_balance = sum(user[3] for user in users)
    print("--------------------------------------------------------------------")
    print(f"Сумма всех балансов: {sum_balance}")

    # Вычисление среднего баланса
    average_balance = sum_balance / count_users
    print("--------------------------------------------------------------------")
    print(f"Средний баланс всех пользователей: {average_balance}")
    print("--------------------------------------------------------------------")

    # Построение графика
    x = range(count_users)
    y = [user[3] for user in users]

    plt.bar(x, y, label='Баланс', width=0.8, alpha=0.5)
    plt.plot(x, y, color='green', marker='o', markersize=7)

    plt.xlabel('Пользователи')
    plt.ylabel('Баланс')
    plt.title('Баланс пользователей')

    plt.show()
finally:
    # Закрытие соединения с базой данных
    connection.commit()
    connection.close()
