import webbrowser
import media
import fresh_tomatoes

# The instances representing my favourite movies

bourne_identity = media.Movie("The Bourne Identity",
                              "http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v8_ai.jpg",
                              "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

bourne_supremacy = media.Movie("The Bourne Supremacy",
                               "http://www.gstatic.com/tv/thumb/movieposters/34579/p34579_p_v8_at.jpg",
                               "https://www.youtube.com/watch?v=Y-HqyyfBbSo")

bourne_ultimatum = media.Movie("The Bourne Ultimatum",
                               "http://www.gstatic.com/tv/thumb/movieposters/166270/p166270_p_v8_ai.jpg",
                               "https://www.youtube.com/watch?v=ZT2ZxjUjSo0")

august_rush = media.Movie("August Rush",
                          "http://www.gstatic.com/tv/thumb/movieposters/166757/p166757_p_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=zhpwjrbeoJQ")

interstellar = media.Movie("Interstellar",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

ex_machina = media.Movie("Ex Machina",
                         "http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

# Gathering the instances in a list

movies = [bourne_identity, bourne_supremacy, bourne_ultimatum,
          august_rush, interstellar, ex_machina]

#Sending the list to the web page

fresh_tomatoes.open_movies_page(movies)
