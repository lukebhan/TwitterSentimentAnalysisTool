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
    # Load Environment
    load_dotenv()

    # Connect To Twitter API
    print("Connecting to Twitter API...")
    try:
        api = TweetScraper(os.environ.get('API'), os.environ.get('API_SECRET'), os.environ.get('ACCESS_TOKEN'),
                           os.environ.get('ACCESS_KEY'))
    except Exception:
        raise Exception("Unable to Connect to API")
    print("Connected to API")

    # Gather Tweets From Past Week
    print("Gathering Tweets....")
    try:
        tweets = api.get_weekly_tweets('bitcoin')
    except Exception:
        raise Exception("Unable to gather tweets")

    # Connect to DB
    print("Establishing DB Connection")
    db = Database(os.environ.get('DB_NAME'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_ADDRESS'),
                  os.environ.get('DB_PORT'))

    # Create Table
    db_column_name = ['Id', 'Text', 'Username', 'Favorite_Count', 'Retweet_Count', 'Follower_Count', 'Date',
                      'Nlp_Score',
                      'Given_Score', 'tokenized_text']
    db_column_type = ['INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER', 'INTEGER', 'INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER',
                      'VARCHAR']
    table_name = os.environ.get('TABLE_NAME')
    print("Creating table " + str(table_name))
    db.create_table(table_name, db_column_name, db_column_type)

    # Insert Tweets
    print("Inserting Tweets")
    try:
        db.insert_tweet_list(table_name, tweets)
    except Exception:
        raise Exception("Unable to insert tweets into Postgres DB")

    # Parse DB Into Tweets and Build Training Set
    tweet_list = db.parse_db_into_tweet_list(table_name)
    training_set_size = int(tweet_list.get_size()*.95)
    training_set = tweet_list.generate_random_tweet_list(training_set_size)

    # Create Tweet Classifier UI and Classify Training Set
    ui_widget = UserInterface(training_set, db, table_name)
    ui_widget.classify()

    # Visualize Classification Projections
    plot = Plot(db)
    plot.generate_projections(table_name, 'given_score')
    plot.build_projections_histogram(table_name)

    # PreProcess Data and Add Tokenized Text To DB:
    try:
        process = PreProcessing()
        token_data = process.generate_token_array(process.process_tweets(tweet_list))
        for index, value in enumerate(token_data):
            db.update_column_by_text(table_name, 'tokenized_text', tweet_list.data[index+1].text, token_data[index])
    except Exception:
        raise Exception("Unable to Tokenize Data")

    # ReParse DB to Get Test Set
    tweet_list = db.parse_db_into_tweet_list(table_name)
    training_set = TweetList()
    test_set = TweetList
    for index in tweet_list.data:
        if tweet_list.data[index].given_score != -10:
            training_set.insert_data(tweet_list.data[index])
        else:
            test_set.insert_data(tweet_list.data[index])

    # Build Vocabulary
    labeled_training_set = process.process_tweets(training_set)
    model = Model()
    model.build_vocabulary(labeled_training_set)

    # Build Feature Vector and Classify
    feature_vector = model.build_feature_vector(labeled_training_set)
    model.train_classifier(feature_vector)

    # Test on test set
    results = model.classify_test_set(test_set)
    plot.create_classification_plot(results.count(1), results.count(-1), results.count(0), results.count(100))


if __name__ == "__main__":
    main()
