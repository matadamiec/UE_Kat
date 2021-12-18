class Link:
    def __init__(self, movie_id, imdb_id, tmdb_id):
        self._movie_id = movie_id
        self._imdb_id = imdb_id
        self._tmdb_id = tmdb_id

    def __str__(self):
        return f'Movie id: {self._movie_id}, Imdb id: {self._imdb_id}, Tmdb id: {self._tmdb_id}'

    @staticmethod
    def class_info():
        return 'Klasa opisująca link'
