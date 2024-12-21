import sqlite3

connection = sqlite3.connect('not_telegram.db') # подключение к БД
cursor = connection.cursor() # создание курсора для взаимодействия с базой данных

cursor.execute('''
                  CREATE TABLE IF NOT EXISTS Users( 
                  id INTEGER PRIMARY KEY, 
                  username TEXT NOT NULL,
                  email TEXT NOT NULL,
                  age INTEGER,
                  balance INTEGER NOT NULL
                                           )''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

for i in range(10): # Заполнить 10 записями
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                  (f'User{i + 1}', f'example{i + 1}gmail.com', f'{(i + 1)*10}', '1000'))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))

for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

cursor.execute('SELECT * FROM Users WHERE age != 60')
result = cursor.fetchall()
for user in result:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
connection.commit()
connection.close()