import pandas as pd


# Class CSV: Handles moving data to and from csv files. This is optional by user and is included if postgres is
# not a preferred method of storage
class CSV:
    # Write a list of tweets to a file
    # Takes in a data object holding a list of tweets
    # Default is tweetlist.csv in the ouptut folder
    # def write_data_to_csv(self, tweet_list, file_name=None):

    # Reads a list of tweet objects from a file
    # Returns a data object and takes in a file location of tweets
    # def read_data_from_csv(self, file_name):

    # Writes an array of users to a csv file
    # Takes in an array and optionally a file_name to write to.
    # Default is userlist.csv in the output folder
    def write_userlist_to_csv(self, userlist, file_name=None):
        df = pd.DataFrame(userlist, columns=["Users"])
        if file_name is None:
            df.to_csv('src/Database/output/userlist.csv', index=False)
        else:
            df.to_csv(file_name, index=False)

    # Reads a list of users into an array
    # Takes the file location of users
    def read_userlist_from_csv(self, file_name):
        # noinspection PyBroadException
        try:
            userlist = pd.read_csv(file_name)
        except Exception:
            print("The file name: " + file_name + " is not a proper path")
        return userlist.values.tolist()
