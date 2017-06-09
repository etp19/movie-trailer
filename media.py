import webbrowser

#This is the class Movie, it contain the
#funtions that allows save the information and play the trailer.
class Movies():
    """ ... contain the functions that allows us to save the information
        """
    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube):
        """ ... this is the constructor method docstring ...
                this function gets series of arguments as an input from the entertainments.py file
                """
        self.title = title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ ... This function makes possible to show trailers by using the webbrowser function.
                        """
        webbrowser.open(self.trailer_youtube_url)

