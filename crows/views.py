from flask import render_template, request, url_for
from crows import app, tweepy_api
import tweepy


@app.route('/', methods=['GET'])
def index():
    # for tweet in tweepy_api.home_timeline(): print tweet.text
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
            f.write(s)

        return render_template('index.html', sentiment=s)


def get_sentiment(lat, long, rad):
    print lat, long, rad
    #TODO: grab placeID, grab tweets, analyze sentiment of tweets
    places = tweepy_api.reverse_geocode(lat=lat, long=long,
        accuracy=rad*1000, granularity="city", max_results=10)
    tweets = []
    for place in places:
        for tweet in tweepy_api.search(q="place:%s" % place.id):
            tweets.append(tweet)
        print place.name
    print len(tweets)
    # for tweet in tweets: print tweet.text + "\n"
    return "weed"
