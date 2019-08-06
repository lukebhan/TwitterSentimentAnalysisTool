

# Tweet Class: This class creates fast variable access for holding various tweet
# attributes as well as parsing tweets.
class Tweet:
    # Default Constructor
    def __init__(self):
        self.text = None
        self.user = None
        self.retweet_count = None
        self.date = None
        self.favorite_count = None
        self.follower_count = None
        self.nlp_score = None
        self.given_score = None
        self.tokenized_text = None

    # Prints All Tweet Attributes
    def __str__(self):
        attributes = " "
        for attribute in self.__dict__:
            attributes += attribute + ": " + str(self.__dict__[attribute]) + " "
        return attributes[1:]

    # Insert Custom Attributes to class dict. Properties act as default properties
    def insert_custom_value(self, name, value):
        dictionary = {name: value}
        self.__dict__.update(dictionary)

    # Remove Custom Attribute
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

    def add_tokenized_text(self, text):
        self.tokenized_text = text

    # Parses json Obj to add tweet attributes
    def add_tweet_json(self, tweet):
        self.add_user(tweet.user.screen_name)
        self.add_creation_date(tweet.created_at)
        self.add_favorite_count(tweet.favorite_count)
        self.add_retweet_count(tweet.retweet_count)
        self.add_text(tweet.full_text)
        self.add_follower_count(tweet.user.followers_count)

    # adds tweet from input without scores
    def add_tweet_noscore(self, text, user, favorite_count, reteweet_count, follower_count, date, tokenized_text=None):
        self.add_user(user)
        self.add_creation_date(date)
        self.add_favorite_count(favorite_count)
        self.add_retweet_count(reteweet_count)
        self.add_text(text)
        self.add_follower_count(follower_count)
        if tokenized_text is not None:
            self.add_tokenized_text(tokenized_text)

    # adds tweet from inputs with scores
    def add_tweet(self, text=None, user=None, favorite_count=None, reteweet_count=None, follower_count=None, date=None,
                  nlp_score=None, given_score=None, tokenized_text=None):
        self.add_user(user)
        self.add_creation_date(date)
        self.add_favorite_count(favorite_count)
        self.add_retweet_count(reteweet_count)
        self.add_text(text)
        self.add_follower_count(follower_count)
        self.add_nlp_score(nlp_score)
        self.add_given_score(given_score)
        self.add_tokenized_text(tokenized_text)
