from src.scraper.tweets_scraper import TweetScraper
import numpy as np

def main():
    api = "fJ2XGVLLTGFcmzNO6Q4LsCfzi"
    api_secret = "8zQSkYZccg5hxbExK7iJgE21ID4zkKCAa7J2aFG8lxDf2tCflV"

    access_token = "1461054643-jksLThYOIQ0kjMZfU5ouOIjq5h3y7jILT8DIV2b"
    acesss_token_secret = "3ptY7ZBhOwf7HFHKrO4uPnHvBzh437akRpSzWku9pLPMP"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    # users = api.get_valuable_users('Scobleizer')
    #
    # # Instantiate DB
    db_vector_column_name = ["username", "text", "favorite_count", "retweet_count", "created_at", "followers",
                             "nlp_score"]
    db_vector_column_type = ["VARCHAR", "VARCHAR", "INTEGER", "INTEGER", "DATE", "INTEGER", "SMALLINT"]
    db = Database("luke", "password", "0.0.0.0", "5432")
    # db.create_table("litecoin", db_vector_column_name, db_vector_column_type)
    #

    # Put Tweet users in CSV
    # with open("output.csv", 'w') as resultFile:
    #     wr = csv.writer(resultFile, dialect='excel')
    #     wr.writerows(users)

    # Gather users from csv
    # with open('output.csv', newline='') as csvFile:
    #     data = list(csv.reader(csvFile))
    # # # Gather tweets from users
    # users = data[:50]
    # keyword = 'litecoin'
    # tweets = []
    # count = 0
    #
    # for user in users[0]:
    #     count += 1
    #     print(str(count) + "/" + str(len(users[0])))
    #     tweets = api.search(keyword, user)
    # print(tweets[0])
    #
    # # Parse tweets into categorical vectors
    # data = api.tweet_data_processing(tweets)
    # db.insert_data('litecoin', db_vector_column_name, data)
    user = db.get_column_data('training_set', 'text')
    processor = Processor()
    processed = processor.process_tweet_list(user)
    db.create_column("training_set", "processed_tweets", processed, "VARCHAR")




if __name__ == "__main__":
    main()
