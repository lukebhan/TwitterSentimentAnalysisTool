import tweepy
import numpy as np


class TweetScraper:
    # initialize tweepy with account without access token required
    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        if access_token is None:
            self.api = tweepy.API(auth)
        else:
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth)

    # search with keyword, user, and date objects
    def search(self, keyword, user=None, start_date=None, end_date=None):
        # search with just user and dates
        if keyword is None:
            query = "(from:" + user + ")(to:" + user + ")since:" + str(start_date.year) + "-" + str(
                start_date.month) + "-" + str(start_date.day) + "until:" + str(end_date.year) + "-" + str(
                end_date.month) + "-" + str(end_date.day)
            return self.api.search(query, tweet_mode='extended')

        # search with just a keyword
        elif user is None:
            query = keyword
            return self.api.search(query, tweet_mode='extended')

        # search with just keyword and user
        elif start_date is None:
            query = keyword + "(from:" + user + ")(to:" + user + ")"
            return self.api.search(query, tweet_mode='extended')

        # search with everything
        else:
            query = keyword + "(from:" + user + ")(to:" + user + ")since:" + str(start_date.year) + "-" + str(
                start_date.month) + "-" + str(start_date.day) + "until:" + str(end_date.year) + "-" + str(
                end_date.month) + "-" + str(end_date.day)
            return self.api.search(query, tweet_mode='extended')

    @staticmethod
    def data_processing(data):
        tweet_vector = []
        for value in data:
            single_tweet = [value.user.screen_name, value.full_text, value.favorite_count, value.retweet_count,
                            value.created_at, 1]
            tweet_vector.append(single_tweet)
        tweet_vector = np.asarray(tweet_vector)
        return tweet_vector
