from src.scraper.tweets_scraper import TweetScraper
import numpy as np

def main():
    api = "fJ2XGVLLTGFcmzNO6Q4LsCfzi"
    api_secret = "8zQSkYZccg5hxbExK7iJgE21ID4zkKCAa7J2aFG8lxDf2tCflV"

    access_token = "1461054643-jksLThYOIQ0kjMZfU5ouOIjq5h3y7jILT8DIV2b"
    acesss_token_secret = "3ptY7ZBhOwf7HFHKrO4uPnHvBzh437akRpSzWku9pLPMP"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)
    api.search("tesla", "elonmusk")




if __name__ == "__main__":
    main()
