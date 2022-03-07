import requests as req
from colorama import Fore, Back, Style


class MoviesSearch:

    __API_KEY = '<yourkeygoeshere>'
    __MOVIES_API = 'https://api.themoviedb.org/3/search/movie'

    def __init__(self, movie_search_term):
        self.__search_term = movie_search_term
        self.__search_result = None

    def get_movies(self):
        request = {'api_key': self.__API_KEY, 'query': self.__search_term}
        response = req.get(url=self.__MOVIES_API, params=request)
        self.__search_result = response.json()

    def get_formatted_result(self):
        if self.__search_result is None:
            self.get_movies()

        for movie in self.__search_result['results']:
            MoviesSearch.__print_movie(movie)

    @staticmethod
    def __print_movie(movie):
        title = movie["original_title"]
        overview = movie["overview"].replace('. ', '. \n')
        release_date = movie["release_date"]
        vote_average = movie["vote_average"]
        vote_count = movie["vote_count"]

        aux_len = 4
        print(f'{Style.BRIGHT}{Fore.GREEN}')
        print(''.center(len(title) + aux_len, '*'))
        print(title.center(len(title) + aux_len, ' '))
        print(''.center(len(title) + aux_len, '*'))
        print(f'{Style.RESET_ALL}')
        print(f'Release Date: {release_date}, Rating: {vote_average}, Rating Count: {vote_count}')
        print(f'{Style.BRIGHT}Overview{Style.RESET_ALL}')
        print(f'{overview}')
        print(f'{Style.BRIGHT}{Fore.GREEN}')
        print(''.center(len(title) + aux_len, '*'))
        print(f'{Style.RESET_ALL}')
