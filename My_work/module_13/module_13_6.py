"""
Задача "Ещё больше выбора"
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = 'Здесь ваш токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_in = InlineKeyboardMarkup(row_width=2)
kb_in.add(InlineKeyboardButton(text='Расчитать норму калорий', callback_data='calories'),
          InlineKeyboardButton(text='Формулы расчета', callback_data='formulas'))
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb.add(KeyboardButton('Расчитать'), KeyboardButton('Информация'))
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb1.add(KeyboardButton('мужской'), KeyboardButton('женский'))


class UserState(StatesGroup):
    """
    Класс состояний пользователя
    """
    age = State()
    growth = State()
    weight = State()
    sex = State()


@dp.message_handler(commands='start')
async def start(message):  # Функция ответа на команду "start"
    await message.answer("Привет! Я бот помогающий твоему здоровью. Введите команду 'Расчитать'",
                         reply_markup=kb)  # Ответ бота, добавляем кнопки "Расчитать" и "Информация"


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer("Выберите опцию", reply_markup=kb_in)


@dp.callback_query_handler(text='formulas')  # Обработка команды "Информация"
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; " '\n'
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.")
    await call.answer()


@dp.callback_query_handler(text='calories')  # Обработка команды "Расчитать" и запуск машины состояний
async def set_age(calc):
    await calc.message.answer('Введите ваш возраст:')
    await UserState.age.set()
    await calc.answer()


@dp.message_handler(state=UserState.age)  # Обработка машины состояния после ввода возраста
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите ваш рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)  # Обработка машины состояния после ввода роста
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Ведите ваш вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)  # Обработка машины состояния после ввода веса
async def set_sex(message, state):
    await state.update_data(weight=message.text)
    # Ответ бота, добавляем кнопки "мужской" и "женский"
    await message.answer('Выберите ваш пол (мужской/женский):', reply_markup=kb1)
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)  # Обработка машины состояния после ввода пола
async def send_calories(message, state):
    await state.update_data(sex=message.text)
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    sex = data['sex']
    if sex == 'женский':
        message.text = (10 * int(weight) + 6.25 * int(growth) - 5 * int(age) - 161)  # формула для женщин
    else:
        message.text = (10 * int(weight) + 6.25 * int(growth) - 5 * int(age) + 5)  # формула для мужчин

    await message.answer(f'Ваша норма каллорий: {message.text}')
    await state.finish()


@dp.message_handler()
async def all_message(message):  # Функция ответа на все сообщения
    await message.answer('Введите команду /start, чтобы начать общение.')  # Ответ бота


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # Запуск бота
