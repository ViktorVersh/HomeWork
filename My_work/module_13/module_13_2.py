"""
Задача "Бот поддержки (Начало)"
"""
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = 'Здесь должен быть ваш Токен'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message):
    """
    Функция ответа на команду "/start"
    :param message:
    :return:
    """
    await message.reply("Привет! Я бот помогающий твоему здоровью.")  # Ответ бота
    print('Привет! Я бот помогающий твоему здоровью.')  # Вывод ответа бота в консоль


@dp.message_handler()
async def all_message(message):
    """
    Функция ответа на остальные запросы кроме "/start"
    :param message:
    :return:
    """
    await message.reply('Введите команду /start, чтобы начать общение.')  # Ответ бота
    print('Введите команду /start, чтобы начать общение.')  # Вывод ответа бота в консоль


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  # Запуск бота
