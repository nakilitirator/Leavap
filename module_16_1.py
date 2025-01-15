from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def message() -> str:
    return 'Главная страница'


@app.get('/user/admin')
async def admin() -> str:
  return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_id(user_id) -> str:
  return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user(username: str, age: int) -> str:
  return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
