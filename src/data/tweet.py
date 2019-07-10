# Tweet Class: This class creates fast variable access for holding various tweet attributes as well as parsing tweets


class Tweet:
    def __init__(self):
        self.text = None
        self.user = None
        self.retweet_count = None
        self.date = None
        self.favorite_count = None
        self.follower_count = None
        self.nlp_score = None
        self.given_score = None

    def __str__(self):
        attributes = " "
        for attribute in self.__dict__:
            attributes += attribute + ": " + str(self.__dict__[attribute]) + " "
        return attributes[1:]

    def insert_custom_value(self, name, value):
        dict = {name: value}
        self.__dict__.update(dict)

    def remove_custom_value(self, name):
        del self.__dict__[name]

    def add_nlp_score(self, score):
        self.nlp_score = score

    def add_given_score(self, score):
        self.given_score = score

    def add_user(self, user):
        self.user = user

    def add_text(self, text):
        self.text = text

    def add_creation_date(self, date):
        self.date = date

    def add_favorite_count(self, count):
        self.favorite_count = count

    def add_retweet_count(self, count):
        self.retweet_count = count

    def add_follower_count(self, count):
        self.follower_count = count

    def add_tweet(self, tweet):
        self.add_user(tweet.user.screen_name)
        self.add_creation_date(tweet.created_at)
        self.add_favorite_count(tweet.favorite_count)
        self.add_retweet_count(tweet.retweet_count)
        self.add_text(tweet.full_text)
        self.add_follower_count(tweet.user.followers_count)
