import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from src.Obj.TweetList import TweetList


# Tokenization of Data before ML Classifier
class PreProcessing:
    # create stop words set
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    # process each tweet in a tweet_list
    def process_tweets(self, list_tweets):
        processed_tweets = []
        for index in list_tweets.data:
            processed_tweets.append(self.process_tweet(list_tweets.data[index].text))
        return processed_tweets

    # remove junk and tokenize
    def process_tweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]
