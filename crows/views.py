from flask import render_template, request, url_for
from crows import app, tweepy_api, geolocator
import tweepy, requests, math


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/cs', methods=['GET', 'POST'])
def current_sentiment():
    if request.method == 'GET':
        return open('sentiment', 'r').readline()

    if request.method == 'POST':
        loc = request.form.get('location')
        rad = request.form.get('radius')

        s = get_sentiment(loc, rad)
        with open('sentiment', 'w') as f:
            f.write(str(s))

        return render_template('index.html', sentiment=s)


def get_sentiment(loc, rad):
    # grab placeID, grab tweets, analyze sentiment of tweets
    location = geolocator.geocode(str(loc))
    lat = location.latitude
    long = location.longitude
    place = tweepy_api.reverse_geocode(lat=lat, long=long, accuracy=rad*1000)[0]
    tweets = tweepy_api.search(q="place:{0}".format(place.id), lang="en")
    location = geolocator.reverse("{0}, {1}".format(lat, long))

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

    return neg/len(tweets), neutral/len(tweets), \
        pos/len(tweets), location.address.encode('ascii', 'ignore')
