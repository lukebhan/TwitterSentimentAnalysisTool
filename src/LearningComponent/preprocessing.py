import re
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords


# Tokenization of Data before ML Classifier
class PreProcessing:
    # create stop words set
    def __init__(self):
        self._stopwords = set(stopwords.words('english') + list(punctuation) + ['AT_USER', 'URL'])

    # process each tweet in a tweet_list
    def process_tweets(self, list_tweets):
        processed_tweets = []
        for index in list_tweets.data:
            processed_tweets.append(
                (self._process_tweet(list_tweets.data[index].text), list_tweets.data[index].given_score))
        return processed_tweets

    # remove junk and tokenize
    def _process_tweet(self, tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)  # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet)  # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)  # remove the # in #hashtag
        tweet = word_tokenize(tweet)  # remove repeated characters (helloooooooo into hello)
        return [word for word in tweet if word not in self._stopwords]

    @staticmethod
    def generate_token_array(token_arr):
        for index, value in enumerate(token_arr):
            string = ""
            for word in value[0]:
                string += word + ","
            token_arr[index] = string[:-1]
        return token_arr
