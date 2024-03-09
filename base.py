import sqlite3


def connect():  # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('db/my_database.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    format TEXT NOT NULL,
    time TEXT NOT NULL
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def add_user(time, name="No_name", format="8x8"):
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('db/my_database.db')
    cursor = connection.cursor()

    # Добавляем нового пользователя
    cursor.execute('INSERT INTO Users (name, format, time) VALUES (?, ?, ?)', (name, format, time))
    connection.commit()
    connection.close()


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('db/my_database.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT name, format, time from Users"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")