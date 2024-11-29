import threading
from threading import Thread, Event
import time

print('Hi, PyCharm')
x=43
y=32
print(x*y)
print("End line")



my_set = {10, 20, 30}
my_set.add(20)
print(my_set)




def summ_all(n):
    if n == 1:
        return 1
    else:
        return n + summ_all(n-1)

res = summ_all(5)
print(res)

def decor(func):
    def func_out():
        print('*'*20)
        func()
        print('*'*20)
    return func_out()

@decor
def hello_world():
    print('Hello World')


count = 0

def first_worker():
    global count
    print('Первый рабочий начал выполнять задачу')
    event.wait()
    for i in range(10):
        count += i
        print(f'Первый рабочий добавил значение: {count}')
        time.sleep(1)
    print('Первый рабочий закончил выполнять задачу')

def second_worker():
    global count
    print('Первый рабочий начал выполнять задачу')
    for i in range(5, 10):
        count += i
        print(f'Второй рабочий добавил значение: {count}')
        time.sleep(1)
    print('Второй рабочий закончил выполнять задачу')
    event.set()

event = Event()
start = time.time()
td1 = Thread(target=first_worker)
td2 = Thread(target=second_worker)

td1.start()
td2.start()
td1.join()
td2.join()
print(count)
print(time.time() - start)
