from rest_api.services.links_utils import make_links_list
from rest_api.services.movies_utils import make_movies_list, get_movies_dict
from rest_api.services.ratings_utils import make_ratings_list, get_ratings_dict
from rest_api.services.tags_utils import make_tags_list, get_tags_dict
from services import load_csv

movies_list = make_movies_list(load_csv.make_json("data_source/movies.csv"))
# print(get_movies_dict(movies_list))

links_list = make_links_list(load_csv.make_json("data_source/links.csv"))
# print(get_movies_dict(links_list))

ratings_list = make_ratings_list(load_csv.make_json("data_source/ratings.csv"))
#print(get_ratings_dict(ratings_list))

tags_list = make_tags_list(load_csv.make_json("data_source/tags.csv"))
# print(get_tags_dict(tags_list))
