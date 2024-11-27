import multiprocessing as mp
from queue import Empty
from PIL import Image


def resize_image(paths_image, queue):
    for path_image in paths_image:
        image = Image.open(path_image)
        image = image.resize((600, 800))
        queue.put((path_image, image))


def color_image(queue):
    while True:
        try:
            path_image, image = queue.get(timeout=5)
        except Empty:
            break
        image - image.convert('L')
        image.save(path_image)


if __name__ == '__main__':
    data = []
    queue = mp.Queue

    for image in range(1, 10):
        data.append(f'./image/img_{image}.jpg')

    resize_proces = mp.Process(target=resize_image, args=(data, queue))
    color_proces = mp.Process(target=color_image, args= (queue, ))

    resize_proces.start()
    color_proces.start()
    resize_proces.join()
    color_proces.join()
