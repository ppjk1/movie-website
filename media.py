class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        movie_title: Title of the movie
        poster_image: URL for box art
        trailer_youtube: URL for a YouTube-hosted trailer
        release_date: Date of movie release
        director: Director(s)
        writers: Writer(s)
    """

    def __init__(self, movie_title, poster_image, trailer_youtube,
                 release_date, director, writers):
        """Inits Movie"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        self.director = director
        self.writers = writers
