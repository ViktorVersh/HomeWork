import asyncio

"""
Задача "Асинхронные силачи"
"""


async def start_strongman(name, power):
    """
    функция старт силача
    :param name: Имя силача
    :param power: Сила силача
    :return:
    """
    print(f'Силач {name} начал соревнования')
    """ Цикл соревнования"""
    for i in range(1, 6):
        await asyncio.sleep(12 / power)  # Задержка между поднятиями шара обратно пропорциональна силе силача
        print(f'Силач {name} поднял {i} шар')

    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    """
    функция старт турнира
    :return:
    """
    st1 = asyncio.create_task(start_strongman('Pasha', 3))
    st2 = asyncio.create_task(start_strongman('Denis', 4))
    st3 = asyncio.create_task(start_strongman('Appolon', 5))
    await st1
    await st2
    await st3


asyncio.run(start_tournament())
