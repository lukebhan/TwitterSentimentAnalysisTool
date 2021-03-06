import tweepy
from src.Obj.tweet import Tweet
from src.Obj.tweetlist import TweetList
from datetime import datetime
from datetime import timedelta


# Tweet Scrape Class: This class uses tweepy to handle twitter api's and builds tweets
class TweetScraper:
    # connect to twitter api with account
    def __init__(self, consumer_key, consumer_secret, access_token=None, access_token_secret=None):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        # does not use access token
        if access_token is None:
            self.api = tweepy.API(auth, wait_on_rate_limit=True)
        # uses required auth access tokens
        else:
            auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(auth, wait_on_rate_limit=True)

    # search with keyword, user, and date objects
    # Rate: 180 calls per window
    # Returns a tweet list
    def search(self, keyword, user=None, start_date=None, end_date=None):
        # search with just a keyword
        if user is None and start_date is None and end_date is None:
            query = keyword + " -RT"
            return self.parse_tweets(self.api.search(query, tweet_mode='extended', count=100))

        # search with just keyword and user
        elif start_date is None and end_date is None:
            query = keyword + "(from:" + user + ")(to:" + user + ")" + " -RT"
            return self.parse_tweets(self.api.search(query, tweet_mode='extended'))

        # search with user, keyword, and dates
        elif end_date is None:
            query = keyword + "(from:" + user + ")(to:" + user + ")since:" + str(start_date.year) + "-" + str(
                start_date.month) + "-" + str(start_date.day) + "until:" + str(end_date.year) + "-" + str(
                end_date.month) + "-" + str(end_date.day) + " -RT"
            return self.parse_tweets(self.api.search(query, tweet_mode='extended'))
        # search with keyword and end date (used in get_weekly_tweets)
        elif user is None and start_date is None:
            query = keyword + "()until:" + str(end_date.year) + "-" + str(end_date.month) + "-" + str(
                end_date.day) + " -RT"
            return self.parse_tweets(self.api.search(query, tweet_mode='extended', count=100))

    # gets weekly tweets
    def get_weekly_tweets(self, keyword):
        today = datetime.today()
        cur_date = today
        sub_week = timedelta(days=6, hours=20)
        last_week = today - sub_week
        tweet_list = TweetList()
        query_count = 0
        while cur_date > last_week:
            tweet_list.insert_list(self.search(keyword=keyword, end_date=cur_date))
            query_count += 1
            cur_date = tweet_list.get_last().date
        print("Over the Past Week: \nThere have been {0} tweets about {1} which were collected over {2} queries".format(
            tweet_list.get_size(), keyword, query_count))
        return tweet_list

    # gather a users lists members (helper method to get valuable users)
    # Rate: 75
    # Returns a python list
    def list_members(self, user, slug):
        members = []
        for page in tweepy.Cursor(self.api.list_members, user, slug).items():
            members.append(page)
        return [m.screen_name for m in members]

    # Method takes a user - gathers their lists and then compiles all members in those lists
    # Rate: 15 lists, 75 members
    # Returns a python list
    def get_valuable_users(self, base_user):
        # gather users lists
        lists = self.users_lists(base_user)
        valuable_users = []
        count = 1
        seen = set(valuable_users)
        # adds members of lists into a set. Does not repeat users
        for item in lists:
            print(str(count) + "/" + str(len(lists)))
            slug = self.get_list_slug(item)
            print(slug)
            users = self.list_members(base_user, slug)
            count += 1
            for user in users:
                print(user)
                if user not in seen:
                    seen.add(user)
                    valuable_users.append(user)
        return valuable_users

    # gather a users lists
    # Rate: 15
    # Returns a list status object (tweepy defined)
    def users_lists(self, user):
        lists = []
        for tweet_list in self.api.lists_all(user):
            if tweet_list.user.screen_name == user:
                lists.append(tweet_list)
        return lists

    # Returns the text of a tweet id
    def get_status(self, tweet):
        return self.api.get_status(tweet)

    @staticmethod
    # helper method to return a lists slug
    def get_list_slug(list_item):
        return list_item.slug

    # helper method to transform tweet into usable tweet object
    # returns a tweet list object (Data)
    @staticmethod
    def parse_tweets(data):
        tweet_list = TweetList()
        for tweet in data:
            tweet_obj = Tweet()
            tweet_obj.add_tweet_json(tweet)
            tweet_list.insert_data(tweet_obj)
        return tweet_list
