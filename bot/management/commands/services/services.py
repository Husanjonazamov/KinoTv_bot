import logging
import requests
from config.settings import BASE_URL

def getBasketList(user_id):
    url = BASE_URL + f"food/busket-list?user_id={user_id}"
    response = requests.get(url)
    return response.json()


def getBasketItem(basket_id):
    response = requests.get(BASE_URL + f"food/busket-item?basket_id={basket_id}")
    return response.json()


def changeBasketItem(basket_id, action):
    response = requests.get(BASE_URL + f'/food/busket-change?basket_id={basket_id}&action={action}')
    return response.json()

def clearBasketAndSetRating(user_id):

    response = requests.get(BASE_URL + f'/food/busket-clear-and-rating?user_id={user_id}')
    return response.json()

def deleteBasket(basket_id):
    response = requests.get(BASE_URL + f'/food/basket-delete?basket_id={basket_id}')
    return response.json()



def get_movie_by_code(code: str):
    logging.info(f"Fetching movie with code: {code}")
    response = requests.get(BASE_URL + f'/api/movies/{code}/')
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