from movies_search import MoviesSearch

movie_to_search = input('Enter a movie name or part of it: ')
search = MoviesSearch(movie_to_search)
search.get_formatted_result()
