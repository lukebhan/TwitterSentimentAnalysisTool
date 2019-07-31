from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV
from src.UIWidget.widget import UserInterface
from src.Database.data_to_csv import CSV
from src.Obj.tweetlist import TweetList
from src.LearningComponent.model import Model
from src.LearningComponent.preprocessing import PreProcessing
import os
from dotenv import load_dotenv


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
                      'Given_Score', 'tokenized_text']
    db_column_type = ['INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER', 'INTEGER', 'INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER', 'VARCHAR']

    db_user_column = ['Username']
    db_user_type = ['VARCHAR']
    users = db.get_column_data('users', 'username')
    tweet_list = db.parse_db_into_tweet_list('bitcoin')
    process = PreProcessing()
    list_words = process.process_tweets(tweet_list)
    model = Model()
    apple = model.build_vocabulary(list_words)
    feature_vector = model.build_feature_vector(list_words)
    classifier = model.train_classifier(feature_vector)


if __name__ == "__main__":
    main()
