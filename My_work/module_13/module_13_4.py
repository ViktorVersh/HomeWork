"""
Задача "Цепочка вопросов"
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup



api = 'Здесь будет токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    """
    Класс состояний пользователя
    """
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(commands='start')
async def start(message):
    """
    Функция ответа на команду "/start"
    :param message:
    :return:
    """
    await message.answer("Привет! Я бот помогающий твоему здоровью. Введите команду 'Calories'")  # Ответ бота

@dp.message_handler(text='Calories') # Обработка команды "Calories" и запуск машины состояний
async def set_age(message):
    await message.answer('Введите ваш возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age) # Обработка машины состояния после ввода возраста
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите ваш рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth) # Обработка машины состояния после ввода роста
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Ведите ваш вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight) # Обработка машины состояния после ввода веса
async def set_sex(message, state):
    await state.update_data(weight=message.text)
    await message.answer('Выберите ваш пол (мужской/женский):')
    await UserState.sex.set()

@dp.message_handler(state=UserState.sex) # Обработка машины состояния после ввода пола
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    sex = data['sex']
    if sex == 'женский':
        message.text = (10 * int(weight) + 6.25 * int(growth) - 5 * int(age) - 161) # формула для женщин
    else:
        message.text = (10 * int(weight) + 6.25 * int(growth) - 5 * int(age) + 5) # формула для мужчин

    await message.answer(f'Ваша норма каллорий: {message.text}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    """
    Функция ответа на остальные запросы кроме "/start"
    :param message:
    :return:
    """
    await message.answer('Введите команду /start, чтобы начать общение.')  # Ответ бота



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # Запуск бота
