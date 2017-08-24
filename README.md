# Crows VR

Battle of the Hacks
Rutgers Summer 2016

## Setup

After going into the directory, these are the steps to get the app up and running locally:

#### Step 1. Create a Virtual Environment and Install Dependencies

Create a new Virtual Environment for the project and source it.  If you don't have Virtual Environment yet, you can find installation [instructions here](https://virtualenv.readthedocs.org/en/latest/).

```
$ virtualenv venv
$ source venv/bin/activate
```

Next we need to install the project dependencies, which are listed in `pip.req`. If you have issues, try install MySQL python dev libs.

```
(venv) $ pip install -r pip.req
```

Finally, before running the server, make a `config.py` file and set these four secret variables:
- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_TOKEN_SECRET`

You will need to set up 3rd party app credentials with the [Twitter API](https://dev.twitter.com/rest/public).

#### Step 2. Run the Server

Now we're ready to start our server which is as simple as:

```
(venv) $ ./run.py
```

Optional: If we want to expose this to a public facing URL, we can use [ngrok](https://ngrok.com/):

```
(venv) $ ./ngrok http 5000
```

## Credit

Built by Sakib Jalal, Jamie Liao, and Mihai Andrei at Rutgers University, kept under the MIT License.
