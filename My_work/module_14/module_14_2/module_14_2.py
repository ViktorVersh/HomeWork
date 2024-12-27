# import random  # Закомментируем после создания записей в базе данных
import sqlite3

"""
Задача "Средний баланс пользователя"
"""
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

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
# for i in range(1, 11):
#     cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
#                    (f'User{i}', f'example{i}@gmail.com', str(random.randint(10, 90)),
#                     '1000'))
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

cursor.execute("SELECT COUNT(*) FROM Users")  # Подсчитываем количество записей
count_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")  # Подсчитываем сумму всех балансов
sum_balance = cursor.fetchone()[0]

print (sum_balance / count_users)  # Выводим на консоль средний баланс

connection.commit()
connection.close()
