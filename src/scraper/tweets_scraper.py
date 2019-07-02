import tweepy


# class handles all twitter scraping necessary
# all rates are out of 15 minute windows
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

        # search with user, keyword, and dates
        else:
            query = keyword + "(from:" + user + ")(to:" + user + ")since:" + str(start_date.year) + "-" + str(
                start_date.month) + "-" + str(start_date.day) + "until:" + str(end_date.year) + "-" + str(
                end_date.month) + "-" + str(end_date.day)
            return self.api.search(query, tweet_mode='extended')

    # gather a users lists members (helper method to get valuable users)
    # Rate: 75
    def list_members(self, user, slug):
        members = []
        for page in tweepy.Cursor(self.api.list_members, user, slug).items():
            members.append(page)
        return [m.screen_name for m in members]

    #
    def get_valuable_users(self, base_user):
        lists = self.users_lists(base_user)
        valuable_users = []
        count = 1
        seen = set(valuable_users)
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
    def users_lists(self, user):
        lists = []
        for list in self.api.lists_all(user):
            if list.user.screen_name == user:
                lists.append(list)
        return lists

    @staticmethod
    # helper method to return a lists slug
    def get_list_slug(list_item):
        return list_item.slug

    def get_status(self, tweet):
        return self.api.get_status(tweet)



