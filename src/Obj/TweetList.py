# Data Class: This class holds a dictionary of tweets for quick access via index
# Written by Luke Bhan
# Last Updated: 7/9/19


class TweetList:
    # Default Constructor
    def __init__(self):
        self.data = {}
        self.count = 1

    # Prints every tweet in dictionary
    def __str__(self):
        for attribute in self.data:
            print("ID: " + str(attribute), end=" ")
            print(self.data[attribute])
        return ""

    def insert_data(self, tweet):
        self.data[self.count] = tweet
        self.count += 1

    def remove_last(self):
        self.data = self.data[:-1]
        self.count -= 1

    def remove_index(self, index):
        del self.data[index]

    def remove_user(self, user):
        for key, value in self.data.items():
            if key['user'] == user:
                del self.data[key]

    def remove_creation_date(self, date):
        for key, value in self.data.items():
            if key['created_at'] == date:
                del self.data[key]

    def remove_tweet(self, text):
        for key, value in self.data.items():
            if key['text'] == text:
                del self.data[key]

    def get_tweet(self, index):
        return self.data[index]

    def get_size(self):
        return len(self.data)
