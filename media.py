class Movie():
    """The class representing the template of a movie"""

    def __init__(self, name, art_url, trailer_url):
        self.title = name
        self.poster_image_url = art_url
        self.trailer_youtube_url = trailer_url
