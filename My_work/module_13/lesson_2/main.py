import time
import asyncio

async def get_temp():
    await asyncio.sleep(2)
    print('Первое показание')
    print('25 C')


async def get_press():
    await asyncio.sleep(4)
    print('Второе показание')
    print('101 kPa')


async def main():
    print('Старт')
    task1 = asyncio.create_task(get_temp())
    task2 = asyncio.create_task(get_press())
    await task1
    await task2
    print('Финиш')

start = time.time()
asyncio.run(main())
finish = time.time()

print(f'Время выполнения: {round(finish - start, 2)} сек')
