from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel


app = FastAPI() # Создаем экземпляр приложения FastAPI
users = []  # Храним пользователей в виде списка


# Класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
class User(BaseModel):
    id: int # номер пользователя (int)
    username: str # имя пользователя (str)
    age: int # возраст пользователя (int)


# get запрос по маршруту '/users' теперь возвращает список users.
@app.get('/users')
async def get_users() -> List[User]: # Возвращаем список users
    return users


# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.
@app.post('/user/{username}/{age}')
async def registered_user(username: Annotated[str, Path(max_length=30,
                                                        description='Введите имя',
                                                        example='Pavel')],
                          age: Annotated[int, Path(le=120,
                                                   description='Введите возраст',
                                                   example='24')]
                          ) -> User:
    new_id = users[-1].id + 1 if users else 1 # Регистрируем нового пользователя с уникальным ID
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким
# user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение
# HTTPException с описанием "User was not found" и кодом 404.
@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: Annotated[str, Path(max_length=30,
                                                    description='Введите свое имя',
                                                    example='Pavel')],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description='Введите возраст',
                                               example='24')]
                      ) -> User:
    for user in users: # Обновляем данные существующего пользователя
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    raise HTTPException(status_code=404, detail='User was not found')


# delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id
# есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение
# HTTPException с описанием "User was not found" и кодом 404.
@app.delete('/user/{user_id}')
async def deleted_user(user_id: Annotated[str, Path(description='Введите ID для удаления',
                                                    example='1')]
                       ) -> User:
    for user in users: # Удаляем пользователя по его ID
        if user.id == user_id:
            users.remove(user)
            return user

    raise HTTPException(status_code=404, detail='User was not found')
