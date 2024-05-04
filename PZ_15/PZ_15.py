"""
Приложение ПАРИКМАХЕРСКАЯ для некоторой организации. БД должна
содержать таблицу Услуги со следующей структурой записи: ФИО мастера, ФИО клиента,
пол, название стрижки, стоимость.
"""

import sqlite3

data = [('Смирнов Максим Иванович', 'Иванова Наталья Ивановна', 'ж', 'Укладка', 1500),
       ('Иванов Андрей Петрович', 'Кузнецов Петр Игоревич', 'м', 'Кроп', 1000),
       ('Васильева Наталья Сергеевна', 'Несторова Василиса Владимировна', 'ж', 'Бикси', 1000),
       ('Семёнова Елена Петровна', 'Ёлкин Борис Николаевич', 'м', 'Шторы', 900),
       ('Меркель Полина Адольфовна', 'Суворова Алина Максимовна', 'ж', 'Мелирование', 1500),
       ('Иванов Андрей Петрович', 'Медведев Иван Юрьевич', 'м', 'Бокс', 500),
       ('Смирнов Максим Иванович', 'Савченко Наталья Ивановна', 'ж', 'Укладка', 1000),
       ('Иванов Андрей Петрович', 'Васин Сергей Петрович', 'м', 'Полубокс', 600),
       ('Васильева Наталья Сергеевна', 'Пучкова Анастасия Михайловна', 'ж', 'Бикси', 1000),
       ('Семёнова Елена Петровна', 'Уваров Пётр Петрович', 'м', 'Наголо', 300)]

# Создание таблицы и вставка данных
with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS services(
    fio_master TEXT NOT NULL,
    fio_client TEXT NOT NULL,
    pol TEXT,
    haircut_name TEXT NOT NULL,
    price INTEGER NOT NULL
    )""")
    cursor.executemany("INSERT INTO services VALUES (?,?,?,?,?)", data)


with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM services")
    print('\n\nЗАПРОС К ДАННЫМ--------')
    for result in cursor.fetchall():
        print(result)

with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM services WHERE fio_master='Иванов Андрей Петрович'")
    print('\n\nЗАПРОС К ДАННЫМ, где мастер Иванов Андрей Петрович')
    for result in cursor.fetchall():
        print(result)

with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM services WHERE pol='м' AND price <= 1000")
    print('\n\nЗАПРОС К ДАННЫМ, где пол: м AND цена <= 1000')
    for result in cursor.fetchall():
        print(result)

with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("UPDATE services SET fio_master = 'Иванов Иван Иванович' WHERE haircut_name = 'Полубокс'")
    cursor.execute("UPDATE services SET price = 8000 WHERE fio_master = 'Меркель Полина Адольфовна' AND fio_client = 'Суворова Алина Максимовна'")
    connect.commit()

with sqlite3.connect('salon.db') as connect:
    cursor = connect.cursor()
    cursor.execute("DELETE FROM services WHERE pol = 'м' AND price <= 1000")
    cursor.execute("DELETE FROM services WHERE pol = 'ж' AND price = 1500")
    cursor.execute("DELETE FROM services WHERE fio_master = 'Меркель Полина Адольфовна'")
    connect.commit()
    print('\n\n---УДАЛЕНИЕ ДАННЫХ---')
    cursor.execute("SELECT * FROM services")
    for result in cursor.fetchall():
        print(result)