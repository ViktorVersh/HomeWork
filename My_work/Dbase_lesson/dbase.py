import random
import sqlite3
from faker import Faker

fake = Faker('ru_RU')

connect = sqlite3.connect('base.db')
cursor = connect.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    phone INTEGER NOT NULL)
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Names(
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL)
""")
cursor.execute("DELETE FROM Names")
cursor.execute("DELETE FROM Users")
for i in range(1, 101):
    cursor.execute("INSERT INTO Users(name, email, age, phone) VALUES(?, ?, ?, ?)",
                   (f'user{i}', f'user{i}@mail.ru', random.randint(20, 65),
                    f'8924{random.randint(2000000, 9999999)}'))

names = [fake.name() for _ in range(1, 50)]  # Создаем список фиктивных имен
for i in names:
    # ----Записываем имена в базу----
    cursor.execute("INSERT INTO Names (name) VALUES (?)", (i,))

connect.commit()

cursor.execute("SELECT * FROM Users WHERE age <= 40 ORDER BY age >= 20")
for i in cursor.fetchall():
    print(i)

print()

cursor.execute("SELECT * FROM Names")
for i in cursor.fetchall():
    print(i)
print()

cursor.execute("DELETE FROM Users WHERE id % 2 = 0")
connect.commit()

cursor.execute("SELECT * FROM Users WHERE age <50")
for i in cursor.fetchall():
    print(i)
cursor.close()
connect.close()
