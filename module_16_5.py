from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int
    username: str
    age: int

# Напишите новый запрос по маршруту '/':
# Функция по этому запросу должна принимать аргумент request и возвращать TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и список users. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
@app.get('/', response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse(request=request,
                                      name='users.html',
                                      context={'users': users})

#Измените get запрос по маршруту '/user' на '/user/{user_id}':
# Функция по этому запросу теперь принимает аргумент request и user_id.
# Вместо возврата объекта модели User, теперь возвращается объект TemplateResponse.
# TemplateResponse должен подключать ранее заготовленный шаблон 'users.html', а также передавать в него request и одного из пользователей - user. Ключи в словаре для передачи определите самостоятельно в соответствии с шаблоном.
@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request,
                   user_id: Annotated[int, Path(ge=1,
                                                le=100,
                                                description='Enter User ID',
                                                example='1')]
):
    for u in users:
        if u.id == user_id:
            return templates.TemplateResponse(request=request,
                                              name='users.html',
                                              context={'user': u})
    raise HTTPException(status_code=404,
                        detail='User was not found')


@app.post('/user/{username}/{age}', response_model=User)
async def post_user(username: Annotated[str, Path(min_length=5,
                                                  max_length=20,
                                                  description='Enter username',
                                                  example='UrbanUser')],
                    age: Annotated[int, Path(ge=18,
                                             le=120,
                                             description='Enter age',
                                             example=24)]
):
    user_id = max((u.id for u in users), default=0) + 1
    user = User(id=user_id,
                username=username,
                age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: Annotated[int, Path(ge=1, 
                                                   le=100,
                                                   description='Enter User ID',
                                                   example='1')],
                      username: Annotated[str, Path(min_length=5,
                                                    max_length=20,
                                                    description='Enter username',
                                                    example='UrbanUser')],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description='Enter age',
                                               example=24)]
):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id: Annotated[int, Path(ge=1, 
                                                   le=100,
                                                   description='Enter User ID',
                                                   example='1')]
):
    for i, u in enumerate(users):
        if u.id == user_id:
            return users.pop(i)
    raise HTTPException(status_code=404, detail='User was not found')
