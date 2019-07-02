import csv
import tweepy
import numpy as np


# Class builds a training set from a file of already classified tweets. Uses id's since it's illegal to hold
# tweets publicly via twitters agreement
class Training:
    # create array to hold data
    training_data_ids = []
    training_data_set = []
    db_name = "training_set"

    # initialize by opening the already classified training data with ids and add to id's list
    def __init__(self, path, api):
        self.api = api
        with open(path, 'r') as csvFile:
            line_reader = csv.reader(csvFile, delimiter=',', quotechar="\"")
            for row in line_reader:
                self.training_data_ids.append(
                    {"tweet_id": row[2], "label": row[1], "topic": row[0]})

    # calls api to gather the tweet status
    def gather_tweet_text(self):
        count = 0
        for tweet in self.training_data_ids:
            try:
                count += 1
                status = self.api.get_status(tweet["tweet_id"])
                print(str(count) + "/" + str(len(self.training_data_ids)) + " Tweet fetched: " + status.text)
                tweet['text'] = status.text
                print(tweet)
                self.training_data_set.append(tweet)
            except tweepy.TweepError as e:
                continue

    # places the tweets in training_data_set into database given by params
    def place_tweets_in_database(self, db):
        db_vector_column_name = ["text", "label", "topic", "tweet_id"]
        db_vector_column_type = ["VARCHAR", "VARCHAR", "VARCHAR", "VARCHAR"]
        db.create_table(self.db_name, db_vector_column_name, db_vector_column_type)
        for tweet in self.training_data_set:
            data = [tweet['text'], tweet['label'], tweet['topic'], tweet['tweet_id']]
            db.insert_data(self.db_name, db_vector_column_name, np.asarray(data))
