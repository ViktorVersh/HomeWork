from asyncio import timeout
from queue import Queue
from  time import  sleep
import threading


def getter(queue):
    while True:
        sleep(2.01)
        item = queue.get()
        print(threading.current_thread(), 'взял элемент', item)


q = Queue(maxsize=10)
thr1 = threading.Thread(target=getter, args=(q,), daemon=True)
thr1.start()


for i in range(10):
    sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил элемент', i)
