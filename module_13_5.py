import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # клавиатура и кнопочки


api = '0000000000:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton(text='Рассчитать'),
    KeyboardButton(text='Информация'))


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст (полных лет):')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        await message.answer('Введите свой рост (см):')
        await UserState.growth.set()
    else:
        await message.answer('Пожалуйста, введите число.')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(growth=int(message.text))
        await message.answer('Введите свой вес:')
        await UserState.weight.set()
    else:
        await message.answer('Пожалуйста, введите корректное число.')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(weight=int(message.text))

        data = await state.get_data()
        result = round(10*int(data['weight']) + 6.25*int(data['growth']) - 5*int(data['age']) + 5, 2)

        await message.answer(f'Ваша суточная норма: {result} ккал в сутки.')
        await state.finish()
    else:
        await message.answer('Пожалуйста, введите корректное число.')


@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью. '
                         'Нажмите "Рассчитать", чтобы узнать суточную норму калорий.', reply_markup=kb)


@dp.message_handler(text=['Информация'])
async def info(message):
    await message.answer(
        'Данный бот подсчитывает норму потребления калорий для мужчин по'
        ' упрощённой формуле Миффлина - Сан Жеора'
        ' (https://www.calc.ru/Formula-Mifflinasan-Zheora.html).')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)