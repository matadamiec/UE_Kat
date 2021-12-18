from datetime import datetime


class Tag:
    def __init__(self, movie_id, user_id, tag, timestamp):
        self._movie_id = movie_id
        self._user_id = user_id
        self._tag = tag
        self._tag_date = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")

    def __str__(self):
        return f'Movie id: {self._movie_id}, User id: {self._user_id}, Rating: {self._tag}, Data: {self._tag_date}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca tag'
