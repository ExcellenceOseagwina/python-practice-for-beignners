# Store related facts in variables. Text uses quotes; year and duration are
# integers; dividing 10.0 by 10.0 produces a floating-point rating (1.0).
movie_title = 'Avengers Infinity War Endgame'
movie_year_release = 2019
movie_genre = 'Action, Superhero, Sci-Fi'
movie_rating = 10.0/10.0
movie_duration = 181
movie_director = 'The Russo Brothers'

# print() accepts comma-separated values and inserts spaces automatically.
# The first line instead concatenates strings, so the number is converted with str().
print("Title: " + movie_title)
print("Year of release:", movie_year_release)
print("Genre:", movie_genre)
print("Rating:", str(movie_rating))
print("Duration:", movie_duration)
print("Director:", movie_director)
