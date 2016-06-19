from flask import render_template, request, url_for
from geopy.geocoders import Nominatim
from crows import app, tweepy_api
import tweepy, requests, math


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/cs', methods=['GET', 'POST'])
def current_sentiment():
    if request.method == 'GET':
        return open('sentiment', 'r').readline()

    if request.method == 'POST':
        lat = request.form.get('latitude')
        long = request.form.get('longitude')
        rad = request.form.get('radius')

        s = get_sentiment(lat, long, rad)
        with open('sentiment', 'w') as f:
            f.write(str(s))

        return render_template('index.html', sentiment=s)


def get_sentiment(lat, long, rad):
    print lat, long, rad
    # grab placeID, grab tweets, analyze sentiment of tweets
    places = tweepy_api.reverse_geocode(lat=lat, long=long, accuracy=rad*1000)
    tweets = []
    for place in places:
        for tweet in tweepy_api.search(q="place:%s" % place.id):
            tweets.append(tweet)

    geolocator = Nominatim()
    location = geolocator.reverse("{0}, {1}".format(lat, long))

    print "------------"
    neg, neutral, pos = 0.0, 0.0, 0.0
    for tweet in tweets:
        print tweet.text
        r = requests.post('http://text-processing.com/api/sentiment/',
            data={'text': tweet.text}).json()["probability"]
        neg += r["neg"]
        neutral += r["neutral"]
        pos += r["pos"]
        print r["neg"], r["neutral"], r["pos"]
        print "\n"

    return {"place": location.address,
            "neg": neg/len(tweets),
            "neutral": neutral/len(tweets),
            "pos": pos/len(tweets)}
