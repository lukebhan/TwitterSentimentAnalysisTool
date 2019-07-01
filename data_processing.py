import re
from ntlk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

class Processor:
    def __init__(self):
        self.remove_words = set(stopwords.word('english') + list(punctuation) + ['AT_USER', 'URL'])

    def process_tweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        tweet = word_tokenize(tweet) # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]

    def process_tweet_list(self, tweet_list):

