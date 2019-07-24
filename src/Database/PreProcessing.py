import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from src.Obj.TweetList import TweetList


class PreProcessing:
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    def process_tweets(self, list_tweets):
        processed_tweets = TweetList()
        for index in list_tweets.data:
            processed_tweets.insert_data(self.process_tweet(list_tweets.get_tweet(index).text))
        return processed_tweets

    def process_tweet(self, tweet):
        tweet = tweet.lower()  # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]
