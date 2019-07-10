from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV


def main():
    api = "fJ2XGVLLTGFcmzNO6Q4LsCfzi"
    api_secret = "8zQSkYZccg5hxbExK7iJgE21ID4zkKCAa7J2aFG8lxDf2tCflV"

    access_token = "1461054643-jksLThYOIQ0kjMZfU5ouOIjq5h3y7jILT8DIV2b"
    acesss_token_secret = "3ptY7ZBhOwf7HFHKrO4uPnHvBzh437akRpSzWku9pLPMP"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    data = api.search("tesla", "elonmusk")

    db = Database('luke', 'password', '127.0.0.1', '5432')
    db_column_name = ['Id', 'Text', 'Username', 'Favorite_Count', 'Retweet_Count', 'Follower_Count', 'Date', 'Nlp_Score',
                      'Given_Score']
    db_column_type = ['integer', 'VARCHAR', 'VARCHAR', 'integer', 'integer', 'integer', 'VARCHAR', 'varchar', 'INTEGER']


if __name__ == "__main__":
    main()
