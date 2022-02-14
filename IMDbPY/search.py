import imdb

ia = imdb.IMDb()

movie = input('Enter name: ')

search = ia.search_movie(movie)

print('Search results: ')

for i in search:

    print(i)