##########################################################################
# The IMDb (Internet Movie Database) contains information on various movies:
# the title, rating, review, list of actors, etc.
#
# We are given a dictionary that contains data on some of the movies.
# (See the example below.) The key is the title of the movie and the values
# is a triple that contains the year in which it was released, the rating,
# and a list of one or more genres.
##########################################################################

movies_example = {
	'Pulp Fiction': (1994, 8.9, ['Crime', 'Drama']),
	'The Good, the Bad and the Ugly': (1966, 8.8, ['Adventure', 'Western']),
	'The Painted Bird': (2019, 7.3, ['Drama', 'Thriller', 'War']),
	'Schindler\'s List': (1993, 9.0, ['Biography', 'Drama', 'History']),
	'The Dark Knight':(2008, 9.0, ['Action', 'Crime', 'Drama', 'Thriller']),
	'12 Angry Men':(1957, 9.0, ['Crime', 'Drama']),
	'The Shawshank Redemption':(1994, 9.3, ['Drama']),
	'The Godfather':(1972, 9.2, ['Crime', 'Drama']),
	'The Lord of the Rings: The Fellowship of the Ring': 
		(2001, 8.8, ['Action', 'Adventure', 'Drama', 'Fantasy']),
	'Forrest Gump': (1994, 8.8, ['Drama', 'Romance']),
	'Fight Club': (1999, 8.8, ['Drama']),
}

##########################################################################
# Write a function by_year(movies) that gets a dictionary as descibred above.
# The function should print the list of movies sorted by the year. For each
# year that is present in the list there should be a line with that number
# is should be followed by titles of all movies of that year, sorted
# by the title. The line with the title should be indented by 4 spaces.
#
# Example:
#
#     >>> by_year(movies_example)
#     1957
#         12 Angry Men
#     1966
#         The Good, the Bad and the Ugly
#     1972
#         The Godfather
#     1993
#         Schindler's List
#     1994
#         Forrest Gump
#         Pulp Fiction
#         The Shawshank Redemption
#     1999
#         Fight Club
#     2001
#         The Lord of the Rings: The Fellowship of the Ring
#     2008
#         The Dark Knight
#     2019
#         The Painted Bird
##########################################################################
def by_year(movies):
    d = {} # {year: [title_1, title_2, ...]}
    for title in movies:
        year, rating, genre = movies[title]
        if year not in d:
            d[year] = []
        d[year].append(title)

    for year in sorted(d):
        print(year)
        for title in sorted(d[year]):
            print('    ' + title)
    
# by_year(movies_example)

##########################################################################
# Write a function by_genre(movies) that gets a dictionary as descibred above.
# The function should return a new dictionary where keys are genres and
# values are lists of movies of that genre. For each movie we shall have
# a pair (title, rating) as shown in the examples below. Note that the
# same movie may appear several times if it belongs to several genres.
#
# Example:
# 
#     >>> by_genre(movies_example)
#     {'Crime': [('Pulp Fiction', 8.9), ('The Dark Knight', 9.0), 
#                ('12 Angry Men', 9.0), ('The Godfather', 9.2)], 
#      'Drama': [('Pulp Fiction', 8.9), ('The Painted Bird', 7.3), 
#                ("Schindler's List", 9.0), ('The Dark Knight', 9.0), 
#                ('12 Angry Men', 9.0), ('The Shawshank Redemption', 9.3), 
#                ('The Godfather', 9.2), ('The Lord of the Rings: The Fellowship of the Ring', 8.8), 
#                ('Forrest Gump', 8.8), ('Fight Club', 8.8)], 
#      'Adventure': [('The Good, the Bad and the Ugly', 8.8), 
#                   ('The Lord of the Rings: The Fellowship of the Ring', 8.8)], 
#      'Western': [('The Good, the Bad and the Ugly', 8.8)], 
#      'Thriller': [('The Painted Bird', 7.3), ('The Dark Knight', 9.0)], 
#      'War': [('The Painted Bird', 7.3)], 
#      'Biography': [("Schindler's List", 9.0)], 
#      'History': [("Schindler's List", 9.0)], 
#      'Action': [('The Dark Knight', 9.0), ('The Lord of the Rings: The Fellowship of the Ring', 8.8)], 
#      'Fantasy': [('The Lord of the Rings: The Fellowship of the Ring', 8.8)], 
#      'Romance': [('Forrest Gump', 8.8)]}
##########################################################################

def by_genre(movies):
    d = {} # {genre: [(title_1, rating_1), (title_2, rating_2), ...]}
    for title in movies:
        year, rating, genre = movies[title]
        for g in genre:
            if g not in d:
                d[g] = []
            d[g].append((title, rating))
    return d

# print(by_genre(movies_example))

##########################################################################
# Write a function avg_genre_ratings(movies) that gets a dictionary of movies
# as descibred above. The function should return a new dictionary where
# keys are genres and the corresponding values is the average rating of all
# movies that belong to that genre.
#
# Example:
#
#     >>> avg_genre_ratings(movies_example)
#     {'Crime': 9.025, 'Drama': 8.81, 'Adventure': 8.8, 'Western': 8.8, 
#      'Thriller': 8.15, 'War': 7.3, 'Biography': 9.0, 'History': 9.0, 
#      'Action': 8.9, 'Fantasy': 8.8, 'Romance': 8.8}
#
# Note: Do not worry if there is roundoff error :-)
##########################################################################
def avg_genre_ratings(movies):
    movies = by_genre(movies)
    # {genre: [(title_1, rating_1), (title_2, rating_2), ...]}
    d = {}
    for genre in movies:
        ratings = []
        for x in movies[genre]:
            ratings.append(x[1])
        d[genre] = sum(ratings) / len(ratings)
    return d

# print(avg_genre_ratings(movies_example))

##########################################################################
# Write a function genres_in_year(movies) that gets a dictionary of movies
# as descibred above. The function should return a new dictionary where
# keys are years, and values are sets of genres of all movies in that year.
#
# Example:
#
#     >>> genres_in_year(movies_example)
#     {1994: {'Romance', 'Crime', 'Drama'}, 1966: {'Western', 'Adventure'}, 
#      2019: {'War', 'Thriller', 'Drama'}, 1993: {'Biography', 'History', 'Drama'}, 
#      2008: {'Thriller', 'Crime', 'Drama', 'Action'}, 
#      1957: {'Crime', 'Drama'}, 1972: {'Crime', 'Drama'}, 
#      2001: {'Drama', 'Fantasy', 'Adventure', 'Action'}, 1999: {'Drama'}}
##########################################################################

def genres_in_year(movies):
    d = {} # {year: [title_1, title_2, ...]}
    for title in movies:
        year, rating, genre = movies[title]
        if year not in d:
            d[year] = set()
        for g in genre:
            d[year].add(g)
    return d

print(genres_in_year(movies_example))
