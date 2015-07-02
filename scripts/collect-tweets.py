from __future__ import unicode_literals

import twitter
import time
import os
import sys

user_to_collect = sys.argv[1]

consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN_KEY')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret,
        )

api.VerifyCredentials()

# shitty but works
timeline = api.GetUserTimeline(
        screen_name=user_to_collect,
        count=200,
        include_rts=False,
        )

all_tweets = []
max_id = None

tweets = api.GetUserTimeline(
        screen_name=user_to_collect,
        count=200,
        include_rts=True,
        )
all_tweets = tweets

older_than = all_tweets[-1].id

while True:
    tweets = api.GetUserTimeline(
            screen_name=user_to_collect,
            count=200,
            include_rts=False,
            max_id=older_than,
            )
    all_tweets = all_tweets + tweets

    if older_than == tweets[-1].id:
        break
    older_than = tweets[-1].id
    print 'getting tweets older than {}'.format(older_than)
    with open('tweets.out', 'wa') as f:
        for tweet in all_tweets:
            text = tweet.text.encode('utf-8').strip()
            f.write(text)
            f.write('\n')
    #time.sleep(0.25) # sleep here because the twitter api rate limits us. could tweak it



