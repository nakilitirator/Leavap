from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI() # Создаём новое приложение FastAPI

users = {'1': 'Имя: Example, возраст: 18'} # Создаём словарь

# get запрос по маршруту '/users', который возвращает словарь users.
@app.get('/users')
async def get_users() -> dict:
    return users

# post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению
# ключом значение строки "Имя: {username}, возраст: {age}".
# И возвращает строку "User <user_id> is registered".
@app.post('/users/{username}/{age}')
async def post_user(username: Annotated[str, Path(max_length=30,
                                                  description='Введите имя',
                                                  example='Pavel')],
                    age: Annotated[int, Path(le=120,
                                             description='Введите возраст',
                                             example='24')]
                    ) -> str:

    user_id = str(int(max(users, key=int)) + 1) # присвоение следующего id пользователю
    users[user_id] = f'Имя: {username}: Возраст: {age}' # добавление в users
    return f'User {user_id} is registered'


# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом user_id
# на строку "Имя: {username}, возраст: {age}". И возвращает строку
# "The user <user_id> is updated"
@app.put('/user/{user_id}/{username}/{age}')
async def put_users(user_id: int,
                    username: Annotated[str, Path(max_length=30,
                                                  description='Введите свое имя',
                                                  example='Pavel')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description='Введите возраст',
                                             example='24')]
                    ) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}' # изменяем user_id: имя, возраст пользователя с user_id на новое
    return f'The user {user_id} is updated'

# delete запрос по маршруту '/user/{user_id}',
# который удаляет из словаря users по ключу user_id пару.
@app.delete('/user/{user_id}')
async def delete_users(user_id: Annotated[str, Path(description='Введите ID для удаления',
                                                 example='1')]
                    ) -> str:
    users.pop(user_id)
    return f'The user {user_id} is delete'