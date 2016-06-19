from flask import render_template, request, url_for
from crows import app
import tweepy


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

        s = get_sentiment(lat, long)
        with open('sentiment', 'w') as f:
            f.write(s)

        return render_template('index.html', sentiment=s)


def get_sentiment(lat, long):
    print lat, long
    #TODO: grab placeID, grab tweets, analyze sentiment of tweets
    return "lol"
