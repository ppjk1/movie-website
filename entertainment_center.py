# coding=utf-8

import media
import fresh_tomatoes


def main():
    # We instantiate a number of Movie objects
    # and use them to generate an HTML page
    # allowing a user to view box art and trailers.

    shaun_of_the_dead = media.Movie(
        "Shaun of the Dead",
        "http://ia.media-imdb.com/images/M/MV5BMTU2NjA0NDk0NV5BMl5BanBnXkFtZTcwOTA0OTQzMw@@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=z-lmF5DAssU",
        "2004",
        "Edgar Wright",
        "Simon Pegg, Edgar Wright")
    hot_fuzz = media.Movie(
        "Hot Fuzz",
        "http://ia.media-imdb.com/images/M/MV5BMTIxODg2NDU1MF5BMl5BanBnXkFtZTcwOTc3MDM0MQ@@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=KOddZELDPmk",
        "2007",
        "Edgar Wright",
        "Edgar Wright, Simon Pegg")
    paul = media.Movie(
        "Paul",
        "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Paul_poster.jpg/215px-Paul_poster.jpg",  # noqa
        "https://www.youtube.com/watch?v=tav42JTdW4A",
        "2011",
        "Greg Mottola",
        "Simon Pegg, Nick Frost")
    fantastic_fear = media.Movie(
        "A Fantastic Fear of Everything",
        "https://upload.wikimedia.org/wikipedia/en/4/45/Afantasticfearofeverything0001.jpg",  # noqa
        "https://www.youtube.com/watch?v=R9_H34YiKH0",
        "2012",
        "Crispian Mills, Chris Hopewell",
        "Crispian Mills")
    the_worlds_end = media.Movie(
        "The World's End",
        "http://ia.media-imdb.com/images/M/MV5BNzA1MTk1MzY0OV5BMl5BanBnXkFtZTgwNjkzNTUwMDE@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=hFo7eJR2cvc",
        "2013",
        "Edgar Wright",
        "Simon Pegg, Edgar Wright")
    hector = media.Movie(
        "Hector and the Search for Happiness",
        "http://ia.media-imdb.com/images/M/MV5BNTAzNTIyNDYzNV5BMl5BanBnXkFtZTgwNDg1NjYyMjE@._V1_SX214_AL_.jpg",  # noqa
        "https://www.youtube.com/watch?v=ghCKHlMJoxM",
        "2014",
        "Peter Chelsom",
        "Maria von Heland, Peter Chelsom and Tinker Lindsay	(screenplay) and \
        François Lelord (novel \"Le voyage d'Hector ou la recherche de \
        bonheur\")")
    movies = [
        shaun_of_the_dead,
        hot_fuzz,
        paul,
        fantastic_fear,
        the_worlds_end,
        hector]

    # Generate and open the HTML page
    fresh_tomatoes.open_movies_page(movies)

# Ensures script only runs when loaded directly
if __name__ == '__main__':
    main()
