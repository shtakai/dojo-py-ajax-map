from system.core.controller import *
from time import strftime
import datetime
import string
import random
import re

class Services(Controller):
    def __init__(self, action):
        super(Services, self).__init__(action)
        self.load_model('Service')

    # helper methods
    def set_flash(self, messages, level):
        for message in messages:
            flash(message, level)

    def index(self):
        return self.load_view('/index.html')

    def search(self):
        print 'Services#search', request.form
        artist = request.form['artist_name'].replace(' ', '')
        print 'artist', artist
        url = "https://itunes.apple.com/search?term=" + artist + "&entity=musicVideo"
        print 'url', url
        # notice this is 'requests' not 'request'
        # we are using the request modules, 'get' function to send a request from our controller
        # then we use ".content" to get the content we are looking for
        response = requests.get(url).content
        print 'response', response
        # we then send the response back to our client which sent the initial post request
        return response
