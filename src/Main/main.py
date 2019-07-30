from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV
from src.UIWidget.widget import UserInterface
from src.Database.data_to_csv import CSV
from src.Obj.TweetList import TweetList
from src.Obj.tweet import Tweet
import time
import random
import os
from dotenv import load_dotenv
from src.Visualization.Plot import Plot


def main():
    load_dotenv()
    api = os.environ.get('API')
    api_secret = os.environ.get('API_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    access_token_secret = os.environ.get('ACCESS_KEY')
    # Gather users
    api = TweetScraper(api, api_secret, access_token, access_token_secret)

    db = Database(os.environ.get('DB_NAME'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_ADDRESS'),
                  os.environ.get('DB_PORT'))
    db_column_name = ['Id', 'Text', 'Username', 'Favorite_Count', 'Retweet_Count', 'Follower_Count', 'Date',
                      'Nlp_Score',
                      'Given_Score']
    db_column_type = ['INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER', 'INTEGER', 'INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER']

    db_user_column = ['Username']
    db_usre_type = ['VARCHAR']
    plot = Plot(db)
    plot.generate_projections('bitcoin', 'given_score')
    plot.build_projections_histogram('bitcoin')


if __name__ == "__main__":
    main()
