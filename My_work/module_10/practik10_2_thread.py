import requests
import pprint
import queue
from threading import Thread, Event

all_songs = []

ACCESS_TOKEN = "your_access_token"
RANDOM_GENRE_API_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre"
GEIEUS_API_URL = "https://api.genius.com/search"
GENIUS_URL = "https://genius.com/"

class GetGenre(Thread):
    def __init__(self, queue, stop_event):
        self.queue = queue
        self.stop_event = stop_event
        super().__init__()

    def run(self):
        while not stop_event.is_set():
            genre = requests.get(RANDOM_GENRE_API_URL).json()
            self.queue.put(genre)


class Genius(Thread):
    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        genre = queue.get()
        data = requests.get(GEIEUS_API_URL, params={"access_token": ACCESS_TOKEN, "q": "genre"})
        data = data.json()
        try:
            song_id = ['response']['hits'][0]['result']['api_path']
            all_songs.append(f'{GENIUS_URL}, {song_id}/apple_music_player')
        except IndexError as e:
            pass

queue = queue.Queue
genre_list = []
genius_list = []

for _ in range(10):
    stop_event = Event()
    t = GetGenre(queue, stop_event)
    t.start()
    genre_list.append(t)

for _ in range(10):
    t = Genius(queue)
    t.start()
    genius_list.append(t)


for t in genius_list:
    t.join()


stop_event.set()

for t in genre_list:
    t.join()

print(all_songs)
print(len(all_songs))
print(queue.qsize())
