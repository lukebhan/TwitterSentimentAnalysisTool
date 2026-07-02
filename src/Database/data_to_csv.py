import pandas as pd
from src.Obj.tweet import Tweet
from src.Obj.tweetlist import TweetList


# Class CSV: Handles moving data to and from csv files. This is optional by user and is included if postgres is
# not a preferred method of storage
class CSV:
    TEXT_COLUMNS = ["text", "tweet", "full_text", "content", "clean_text", "message"]
    USER_COLUMNS = ["user", "username", "screen_name", "author", "handle"]
    FAVORITE_COLUMNS = ["favorite_count", "favorite", "favorites", "likes", "like_count"]
    RETWEET_COLUMNS = ["retweet_count", "retweets", "repost_count"]
    FOLLOWER_COLUMNS = ["follower_count", "followers", "followers_count"]
    DATE_COLUMNS = ["date", "created_at", "timestamp", "posted_at"]

    @staticmethod
    def _pick_column(columns, candidates):
        normalized = {column.strip().lower(): column for column in columns}
        for candidate in candidates:
            if candidate in normalized:
                return normalized[candidate]
        return None

    @staticmethod
    def _read_value(row, column, default=None):
        if column is None:
            return default
        value = row[column]
        if pd.isna(value):
            return default
        return value

    # Write a list of tweets to a file
    # Takes in a data object holding a list of tweets
    # Default is tweetlist.csv in the output folder
    @staticmethod
    def write_data_to_csv(tweet_list, file_name=None):
        tweet_id, user, text, favorite_count, follower_count, retweet_count, date, nlp_score, \
            given_score = [], [], [], [], [], [], [], [], []
        for value in tweet_list.data:
            tweet_id.append(value)
            user.append(tweet_list.data[value].user)
            text.append(tweet_list.data[value].text)
            follower_count.append(tweet_list.data[value].follower_count)
            retweet_count.append(tweet_list.data[value].retweet_count)
            date.append(tweet_list.data[value].date)
            nlp_score.append(tweet_list.data[value].nlp_score)
            given_score.append(tweet_list.data[value].given_score)
            favorite_count.append(tweet_list.data[value].favorite_count)
        dictionary = {'id': tweet_id, 'text': text, 'user': user, 'favorite_count': favorite_count, 'retweet_count':
            retweet_count, 'follower_count': follower_count, 'date': date, 'nlp_score': nlp_score,
            'given_score': given_score}
        df = pd.DataFrame(dictionary)
        if file_name is None:
            df.to_csv('src/Database/output/tweetlist.csv', index=False)
        else:
            df.to_csv(file_name, index=False)

    # Reads a list of tweet objects from a file
    # Returns a data object and takes in a file location of tweets
    # def read_data_from_csv(self, file_name):
    @staticmethod
    def read_data_from_csv(file_name):
        data = TweetList()
        df = pd.read_csv(file_name)
        text_col = CSV._pick_column(df.columns, CSV.TEXT_COLUMNS)
        if text_col is None:
            raise Exception("CSV must include a tweet text column")
        user_col = CSV._pick_column(df.columns, CSV.USER_COLUMNS)
        favorite_col = CSV._pick_column(df.columns, CSV.FAVORITE_COLUMNS)
        retweet_col = CSV._pick_column(df.columns, CSV.RETWEET_COLUMNS)
        follower_col = CSV._pick_column(df.columns, CSV.FOLLOWER_COLUMNS)
        date_col = CSV._pick_column(df.columns, CSV.DATE_COLUMNS)
        for index, row in df.iterrows():
            tweet = Tweet()
            tweet.add_tweet(
                CSV._read_value(row, text_col, ""),
                CSV._read_value(row, user_col, ""),
                CSV._read_value(row, favorite_col, 0),
                CSV._read_value(row, retweet_col, 0),
                CSV._read_value(row, follower_col, 0),
                CSV._read_value(row, date_col, "")
            )
            data.insert_data(tweet)
        return data

    # Writes an array of users to a csv file
    # Takes in an array and optionally a file_name to write to.
    # Default is userlist.csv in the output folder
    @staticmethod
    def write_userlist_to_csv(userlist, file_name=None):
        df = pd.DataFrame(userlist, columns=["Users"])
        if file_name is None:
            df.to_csv('src/Database/output/userlist.csv', index=False, mode='a')
        else:
            df.to_csv(file_name, index=False, mode='a')

    # Reads a list of users into an array
    # Takes the file location of users
    @staticmethod
    def read_userlist_from_csv(file_name):
        # noinspection PyBroadException
        try:
            userlist = pd.read_csv(file_name)
        except Exception:
            raise Exception("File not found")
        return userlist.values.tolist()
