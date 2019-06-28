from tweets_scraper import TweetScraper
import datetime
from database import Database


def main():
    api = "fJ2XGVLLTGFcmzNO6Q4LsCfzi"
    api_secret = "8zQSkYZccg5hxbExK7iJgE21ID4zkKCAa7J2aFG8lxDf2tCflV"

    access_token = "1461054643-jksLThYOIQ0kjMZfU5ouOIjq5h3y7jILT8DIV2b"
    acesss_token_secret = "3ptY7ZBhOwf7HFHKrO4uPnHvBzh437akRpSzWku9pLPMP"

    date = datetime.date(2019, 6, 19)
    end_date = datetime.date(2019, 6, 26)
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    value = api.search("bitcoin")
    db_vector_column_name = ["username", "text", "favorite_count", "retweet_count", "created_at", "nlp_score"]
    db_vector_column_type = ["VARCHAR", "VARCHAR", "INTEGER", "INTEGER", "DATE", "SMALLINT"]

    db = Database("luke", "password", "0.0.0.0", "5432")
    data = api.data_processing(value)
    db.create_table("bitcoin", db_vector_column_name, db_vector_column_type)
    db.insert_data("bitcoin", db_vector_column_name, data)


if __name__ == "__main__":
    main()

