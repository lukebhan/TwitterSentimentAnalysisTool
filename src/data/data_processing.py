import re
from nltk.tokenize import word_tokenize
import nltk
from string import punctuation
from nltk.corpus import stopwords
import numpy as np


# processes tweets before placing them into the database
class Processor:
    # creates remove_words set on initialization
    def __init__(self):
        self.remove_words = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    # Removes urls, @users, and punctuation
    def process_tweet(self, tweet):
        tweet = str(tweet).lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        tweet = word_tokenize(tweet) # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self.remove_words]

    # iterates through a list of tweets to process each one
    def process_tweet_list(self, tweet_list):
        processed_tweets = []
        for tweet in tweet_list:
            tweet = self.process_tweet(tweet)
            processed_tweets.append(tweet)
        return processed_tweets

    @staticmethod
    # create vector for tweets
    def tweet_data_processing(data):
        tweet_vector = []
        for value in data:
            single_tweet = [value.user.screen_name, value.full_text, value.favorite_count, value.retweet_count,
                            value.created_at, value.user.followers_count, 1]
            tweet_vector.append(single_tweet)
        tweet_vector = np.asarray(tweet_vector)
        return tweet_vector

    @staticmethod
    # process whether a user is actually a valuable user
    def user_processing(self, user_list, important_users):
        for user in user_list:
            # insert user specification
            # for example:
            # if(self.api.followers(user) > 10000
            important_users.append(user)
        return important_users


