import tweepy
import csv
import pandas as pd


consumer_key =  '7B2QgrJxR4uqLK6RvXd9jN9Cq'
consumer_secret = 'XMR35ILFPxy45qeq5BgQ6OWihbcXBLLojfWXakUez6fe3rLRH6'

access_token = '937091694482395136-Jp33E1numtZtAzLPS6KUchiAQYMZnx1'
access_token_secret = 'r7omroHXwd46PckNkpiW3M9ixfUMFUZ0OgBBd1Q9CZseL'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)



keywords = ['syria', 'damascus', 'assad', 'politics', 'putin', 'trump', 'russia', 'usa', 'skripal', 'uk']
n_items = 10000

for keyword in keywords:
    with open('../tweets/en/{}.csv'.format(keyword), 'w+') as f:
        cursor = tweepy.Cursor(api.search,
                               q=keyword + ' -filter:retweets',
                               lang='en',
                               tweet_mode='extended',
                               until='2018-04-16').items(n_items)

        csvWriter = csv.writer(f)

        for i, tweet in enumerate(cursor):
            csvWriter.writerow([i + 1, tweet.full_text])

    print('finished {}'.format(keyword))
