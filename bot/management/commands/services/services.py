import logging
import requests
from config.settings import BASE_URL





def get_movie_by_code(code: str):
    logging.info(f"Fetching movie with code: {code}")
    response = requests.get(BASE_URL + f'/movies/movies/{code}/')
    if response.status_code == 200:
        try:
            movie = response.json()
            logging.info(f"Movie data received: {movie}")
            return movie
        except ValueError as e:
            logging.error(f"JSON decoding error: {e}")
    else:
        logging.error(f"Failed to fetch movie, status code: {response.status_code}")
    return None



def get_movie_by_list():
    response = requests.get(BASE_URL + 'api/movies_list/')
    if response.status_code == 200:
        try:
            movies = response.json()
            return movies
        except ValueError as e:
            logging.error(f'Json decoding error: {e}')
    else:
        logging.error(f"Failed to retrieve movies, status code: {response.status_code}")
    return None



def get_episodes_by_series_code(code: str):
    response = requests.get(BASE_URL + f'movies/series/{code}/episodes/')
    if response.status_code == 200:
        try:
            episodes = response.json().get('episodes', [])
            return episodes
        except ValueError as e:
            logging.error(f'Json decoding error: {e}')
    else:
        logging.error(f"Failed to retrieve episodes, status code: {response.status_code}")
    return None


def treyler_list(title):
    response = requests.get(BASE_URL + f"api/treyler/{title}")
    if response.status_code == 200:
        try:
            movies = response.json()
            return movies
        except ValueError as e:
            logging.error(f'Json decoding error: {e}')
    else:
        logging.error(f"Failed to retrieve movies, status code: {response.status_code}")
    return None

