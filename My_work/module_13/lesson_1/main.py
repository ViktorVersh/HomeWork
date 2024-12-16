from time import sleep
import asyncio

async def message():
    sleep(1)
    print("Здравствуйте! Мы приехали!")


async def main():
    task = asyncio.create_task(message())
    print("Вызываем такси")
    sleep(1)
    print('Такси выехало!')
    sleep(1)
    print('Такси у подъезда')
    sleep(1)
    print('Едем в такси!')
    for _ in range(1, 4):
        sleep(1)
        print('Мы ещё едем!')
        sleep(1)
    print('Мы на месте!')

asyncio.run(main())