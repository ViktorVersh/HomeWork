import multiprocessing as mp
from datetime import datetime

from PIL import Image
from multiprocessing import Queue, Process

from _queue import Empty


def resize_image(paths_images, queue):
    for path_image in paths_images:
        image = Image.open(path_image)
        image = image.resize((800, 600))
        queue.put((path_image, image))


def color_image(queue):
    while True:
        try:
            path_image, image = queue.get(timeout=5)
        except Empty:
            break
        image = image.convert('L')
        image.save(path_image)


if __name__ == '__main__':
    data = []
    queue = Queue()

    for image in range(151, 201):
        data.append(f'./image/img_{image}.jpg')

    start = datetime.now()
    resize_process = Process(target=resize_image, args=(data, queue))
    color_process = Process(target=color_image, args=(queue,))

    resize_process.start()
    color_process.start()

    resize_process.join()
    while not queue.empty():
        pass
    color_process.join()
    end = datetime.now()
    print(end - start)