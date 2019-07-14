from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV
from src.UIWidget.widget import UserInterface


def main():
    api = "igiH98aVHuB4zsmwKlWEe6qYs"
    api_secret = "lvECXM12Yh7SKYCU6ge05m7dE8R8evdPiIIIcAje7lIruKjvmf"

    access_token = "1461054643-TZHKekB1XCxqssymTtjzB249dO2YmBNy9bTyzpR"
    acesss_token_secret = "UyeMbBlMRqHgqLJnwSSH6iGn01GYuqxceprJ1kWswnS2q"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    data = api.search("tesla", "elonmusk")

    db = Database('luke', 'password', '127.0.0.1', '5432')
    db_column_name = ['Id', 'Text', 'Username', 'Favorite_Count', 'Retweet_Count', 'Follower_Count', 'Date', 'Nlp_Score',
                      'Given_Score']
    db_column_type = ['integer', 'VARCHAR', 'VARCHAR', 'integer', 'integer', 'integer', 'VARCHAR', 'varchar', 'INTEGER']

    apple = UserInterface()
    orange = apple.classify(data.data[1].text)


if __name__ == "__main__":
    main()
