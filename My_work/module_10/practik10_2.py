import requests
import pprint
from threading import Thread

ACCESS_TOKEN = "your_access_token"
RANDOM_GENRE_API_URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre"
GENIUS_API_URL = "https://api.genius.com/search"
GENIUS_URL = "https://genius.com/"

genre = requests.get(RANDOM_GENRE_API_URL).json()

data = requests.get(GENIUS_API_URL, params= {"access_token": ACCESS_TOKEN, "q": "genre"})

pprint(data.json())

data = data.json()

song_id = ['response']['hits'][0]['result']['api_path']

print(f'{GENIUS_URL}, {song_id}/apple_music_player')

