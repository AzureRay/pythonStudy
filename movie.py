##########################################
# Project : My Favorite Movies Website
# Date Started: 12/20/2016
# Date Completed: 12/20/2016
# Submitted by: Azure Ray
##########################################

######################################## Movie File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              main.py file. Class Movie has three basic properties now.
########################################################################################################

class Movie:
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """
        :param title: the movie's name
        :param poster_image_url: the movie's poster picture url
        :param trailer_youtube_url: the movie's video address in youtube
        :return: no return value
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url