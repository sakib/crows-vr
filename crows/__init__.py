#!venv/bin/python
from flask import Flask
from geopy.geocoders import Nominatim
import tweepy

app = Flask(__name__)
app.config.from_pyfile('../config.py')

auth = tweepy.OAuthHandler(app.config["TWITTER_CONSUMER_KEY"],
                           app.config["TWITTER_CONSUMER_SECRET"])
auth.set_access_token(app.config["TWITTER_ACCESS_TOKEN"],
                      app.config["TWITTER_ACCESS_TOKEN_SECRET"])

tweepy_api = tweepy.API(auth)

geolocator = Nominatim()

from crows import views
