import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        return self.nickname == other.nickname  # переопределяем сравнение имя пользователя с пользователями

    def __str__(self):
        return f'{self.nickname}'  # строковое представление пользователя


class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        self.password = hash(password)
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                # Если такой пользователь существует, то current_user меняется на найденного.
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
            else:
                print("Ошибка входа: неверный логин или пароль.")
                return False

    def register(self, nickname, password, age):
        new_users = User(nickname, password, age)
        if new_users in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_users)
            self.current_user = new_users

    def log_out(self):
        self.current_user = None
        return None

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)
            else:
                return

    def get_videos(self, word_key):
        return [video.title for video in self.videos if word_key.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                while video.time_now < video.duration:
                    print(video.time_now + 1, end=' ')
                    video.time_now += 1
                    time.sleep(0.5)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
