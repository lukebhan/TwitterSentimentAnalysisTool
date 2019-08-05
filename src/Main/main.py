from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV
from src.UIWidget.widget import UserInterface
from src.Database.data_to_csv import CSV
from src.Obj.tweetlist import TweetList
from src.LearningComponent.model import Model
from src.LearningComponent.preprocessing import PreProcessing
import os
from src.Visualization.plot import Plot
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
    print("Gathering Tweets....")
    tweets = api.get_weekly_tweets('bitcoin')


    # users = db.get_column_data('users', 'username')
    # tweet_list = db.parse_db_into_tweet_list('bitcoin')
    # # training_set = tweet_list.generate_random_tweet_list(50)
    # # Ui = UserInterface(training_set, db, 'bitcoin')
    # # Ui.classify()
    # # plot = Plot(db)
    # # plot.generate_projections('bitcoin', 'given_score')
    # # plot.build_projections_histogram('bitcoin')
    #
    # list = tweet_list.generate_random_tweet_list(50)
    # ui = UserInterface(list, db, 'bitcoin')
    # ui.classify()
    # training_set = TweetList()
    # test_set = TweetList()
    # for index in tweet_list.data:
    #     if tweet_list.data[index].given_score != -10:
    #         training_set.insert_data(tweet_list.data[index])
    #     else:
    #         test_set.insert_data(tweet_list.data[index])
    #
    # process = PreProcessing()
    # training_set = process.process_tweets(training_set)
    # model = Model()
    # model.build_vocabulary(training_set)
    # feature_vector = model.build_feature_vector(training_set)
    # model.train_classifier(feature_vector)
    # NBResultLabels = model.classify_test_set(test_set)
    # # get the majority vote
    # print(NBResultLabels)



if __name__ == "__main__":
    main()
