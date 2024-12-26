# import random  # Закоментируем после создания записей в базе данных
import sqlite3

"""
Задача "Первые пользователи"
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

cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 != 0", (500,))  # меняем значение balance

cursor.execute("DELETE FROM Users WHERE id = 1 OR id = 4 OR id = 7 OR id = 10")  # удаляем каждую 3 запись

cursor.execute("SELECT username, email, age, balance FROM Users")  # Выбираем все записи

new_age_list = cursor.fetchall()  # получаем список всех записей

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")  # выбираем если возраст не равен 60

for i in new_age_list:
    print(i)

connection.commit()
connection.close()
