import sqlite3

# Подключаемся к базе данных (или создаем её, если она не существует)
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Создаем таблицу items
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    item_id INTEGER,
    name TEXT,
    price REAL,
    update_date TEXT,
    PRIMARY KEY (item_id, update_date)
)
''')

# Создаем таблицу orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item_id INTEGER,
    order_date TEXT,
    FOREIGN KEY (item_id) REFERENCES items(item_id)
)
''')

# Вставляем данные в таблицу items
items_data = [
    (1, 'Ручка гелевая', 10, '2020-02-01'),
    (2, 'Карандаш 1HH', 2, '2020-01-01'),
    (1, 'Ручка шариковая', 10, '2020-03-01'),
    (3, 'Ластик', 5, '2020-07-01'),
    (2, 'Карандаш 1HH', 3, '2020-05-01'),
    (1, 'Ручка шариковая', 5, '2020-05-01'),
    (2, 'Карандаш 1H', 7, '2020-06-01')
]

cursor.executemany('''
INSERT INTO items (item_id, name, price, update_date)
VALUES (?, ?, ?, ?)
''', items_data)

# Вставляем данные в таблицу orders
orders_data = [
    (1, 1, 1, '2020-02-01'),
    (2, 2, 2, '2020-02-01'),
    (3, 1, 3, '2020-07-01'),
    (4, 3, 2, '2020-07-01'),
    (5, 2, 1, '2020-04-01'),
    (6, 1, 1, '2020-06-01')
]

cursor.executemany('''
INSERT INTO orders (order_id, user_id, item_id, order_date)
VALUES (?, ?, ?, ?)
''', orders_data)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно создана и заполнена данными.")
