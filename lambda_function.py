import os
from datetime import datetime, timedelta
import twitter

RETRIEVAL_INTERVAL_MINS = int(os.getenv('RETRIEVAL_INTERVAL_MINS', default=5))
START_TIME = ((datetime.now() - timedelta(minutes=RETRIEVAL_INTERVAL_MINS)) + timedelta(hours=8)).strftime(
    "%Y-%m-%dT%H:%M")
END_TIME = (datetime.now() + timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M")


def retweet(settings: dict):
    api = twitter.Api(
        consumer_key=settings.get('consumer_key'),
        consumer_secret=settings.get('consumer_secret'),
        access_token_key=settings.get('access_token_key'),
        access_token_secret=settings.get('access_token_secret')
    )
    user = api.VerifyCredentials()

    print("\nLogged in as '{}'".format(user.name))

    for phrase in settings.get('phrases'):
        print("Phrase: {}".format(phrase))

        tweets = api.GetSearch(term=phrase, include_entities=False, return_json=False,
                               since=START_TIME)
        print('[{} to {}] Retweeting from the last {} minute/s'.format(START_TIME, END_TIME, RETRIEVAL_INTERVAL_MINS))
        for tweet in tweets:
            try:
                print(' - @{}: "{}"'.format(tweet.user.screen_name, tweet.text))
                api.PostRetweet(tweet.id)
            except Exception as err:
                print(' - ERROR: {}'.format(err))


def lambda_handler(event, context):
    is_active = bool(os.getenv('IS_ACTIVE', default=True))
    if is_active:
        settings = {
            "consumer_key": os.getenv('CONSUMER_KEY'),
            "consumer_secret": os.getenv('CONSUMER_SECRET'),
            "access_token_key": os.getenv('ACCESS_TOKEN_KEY'),
            "access_token_secret": os.getenv('ACCESS_TOKEN_SECRET'),
            "phrases": ["{} -filter:retweets".format(phrase) for phrase in (os.getenv('PHRASES')).split(", ")]
        }
        retweet(settings=settings)

