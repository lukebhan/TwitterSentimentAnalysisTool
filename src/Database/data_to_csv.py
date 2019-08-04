import pandas as pd
from src.Obj.tweet import Tweet
from src.Obj.tweetlist import TweetList


# Class CSV: Handles moving data to and from csv files. This is optional by user and is included if postgres is
# not a preferred method of storage
class CSV:
    # Write a list of tweets to a file
    # Takes in a data object holding a list of tweets
    # Default is tweetlist.csv in the ouptut folder
    @staticmethod
    def write_data_to_csv(tweet_list, file_name=None):
        id, user, text, favorite_count, follower_count, retweet_count, date, nlp_score, given_score = [], [], [], [], [], [], [], [], []
        for value in tweet_list.data:
            id.append(value)
            user.append(tweet_list.data[value].user)
            text.append(tweet_list.data[value].text)
            follower_count.append(tweet_list.data[value].follower_count)
            retweet_count.append(tweet_list.data[value].retweet_count)
            date.append(tweet_list.data[value].date)
            nlp_score.append(tweet_list.data[value].nlp_score)
            given_score.append(tweet_list.data[value].given_score)
            favorite_count.append(tweet_list.data[value].favorite_count)
        dict = {'id': id, 'text': text, 'user': user, 'favorite_count': favorite_count, 'retweet_count':
            retweet_count, 'follower_count': follower_count, 'date': date, 'nlp_score': nlp_score,
                'given_score': given_score}
        df = pd.DataFrame(dict)
        if file_name is None:
            df.to_csv('src/Database/output/tweetlist.csv', index=False)
        else:
            df.to_csv(file_name, index=False)

    # Reads a list of tweet objects from a file
    # Returns a data object and takes in a file location of tweets
    # def read_data_from_csv(self, file_name):
    def read_data_from_csv(self, file_name):
        data = TweetList()
        df = pd.read_csv(file_name)
        for index, row in df.iterrows():
            tweet = Tweet()
            tweet.add_tweet_noscore(row['text'], row['user'], row['favorite_count'], row['retweet_count'],
                                   row['follower_count'], row['date'])
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
            print("The file name: " + file_name + " is not a proper path")
        return userlist.values.tolist()
