from tweets_scraper import TweetScraper
import datetime
from database import Database
import time


def main():
    api = "fJ2XGVLLTGFcmzNO6Q4LsCfzi"
    api_secret = "8zQSkYZccg5hxbExK7iJgE21ID4zkKCAa7J2aFG8lxDf2tCflV"

    access_token = "1461054643-jksLThYOIQ0kjMZfU5ouOIjq5h3y7jILT8DIV2b"
    acesss_token_secret = "3ptY7ZBhOwf7HFHKrO4uPnHvBzh437akRpSzWku9pLPMP"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    users = api.get_valuable_users('Scobleizer')

    # Instantiate DB
    db_vector_column_name = ["username", "text", "favorite_count", "retweet_count", "created_at", "followers",
                             "nlp_score"]
    db_vector_column_type = ["VARCHAR", "VARCHAR", "INTEGER", "INTEGER", "DATE", "INTEGER", "SMALLINT"]
    db = Database("luke", "password", "0.0.0.0", "5432")
    db.create_table("litecoin", db_vector_column_name, db_vector_column_type)

    # Gather tweets from users
    keyword = 'litecoin'
    tweets = []
    for user in users:
        tweets = api.search(keyword, user)
        for tweet in tweets:
            time.sleep(20)
            print("Tweet Value for " + user + ": " + tweet)
            tweets.append(tweet)

    # Parse tweets into categorical vectors
    data = api.tweet_data_processing(tweets)
    db.insert_data('litecoin', db_vector_column_name, data)


if __name__ == "__main__":
    main()
