class Movie:
    def __init__(self, movie_id, title, genres):
        self._movie_id = movie_id
        self._title = title
        self._genres = genres

    def __str__(self):
        return f'Id: {self._movie_id}, nazwa: {self._title}, typ: {self._genres}'

    def get_title(self):
        return self._title

    @staticmethod
    def class_info():
        return 'Klasa opisująca film'
