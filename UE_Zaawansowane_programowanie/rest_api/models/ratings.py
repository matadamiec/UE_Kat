from datetime import datetime


class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self._movie_id = movie_id
        self._user_id = user_id
        self._rating = rating
        self._rate_date = datetime.fromtimestamp(timestamp).strftime("%d-%m-%Y")

    def __str__(self):
        return f'Movie id: {self._movie_id}, User id: {self._user_id}, Rating: {self._rating}, Data: {self._rate_date}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca ocene'
