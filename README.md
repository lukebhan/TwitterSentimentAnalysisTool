# TwitterSentimentAnalysisTool (TSAT)
 A highly adaptable tool for analyzing twitter data. 
 Auto scrapes Tweets based on user keyword from the previous week and applies a naive bayes classifier to analyze sentiment. Comes prebuilt with a docker postgres server managed by pgadmin
 Includes graphical visuals to analyze and categorize data. 
 
**Basic Usage:**
1. Clone the project 
2. Install docker and docker-compose (not listed in requirements.txt)
3. Install requirements.txt
4. In terminal navigate to the project and cd to Docker
5. sudo docker-compose up
6. Check localhost:5555 and sign in to postgres using 'user' and 'password' as email and password respectively
7. create a server with the login 'user' and 'password' and the network 172.XX.0.1 - Look at the terminal for the ip address to fill in the XX
8. Go to .env file and set environment variables (Assumes you created a twitter app)
9. Run main.py, classify tweets and view projections

**Important References:**
* https://arxiv.org/pdf/1811.07522.pdf
* https://jakevdp.github.io/PythonDataScienceHandbook/05.05-naive-bayes.html
* https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed
* https://www.sciencedirect.com/science/article/pii/S1877050919302789
* https://www.sciencedirect.com/science/article/pii/S2405844018332067
* https://arxiv.org/pdf/1509.02971.pdf

**Advanced Usage:**
The tool consists of a series of classes for managing and classifying twitterdata documented here:

**Tweet**
* *Constructor:* * Initializes all the tweet properties to none. Properties include: {Text, User, Retweet_Count, Date, Favorite Count, Follower Count, Nlp Score, Given Score, Tokenized Text
* *insert_custom_value(name, value):* * Allows user to add a custom tweet property
* *add_{insert_property}(property):* * Allows users to update defined properties
* *add_tweet_json(tweet)* * When referencing the twitter API, tweets are returned in Json. This parses the json into a tweet obj
* *add_tweet(text,user, favorite_count, retweet_count, follower_count, date, nlp_score, given_score, tokenized_text):* * Allows the user to add multiple properties at once. None of the properties are required

**TweetList**
* *Constructor:* * Initializes the dict for storing counds a begins indexing
* *insert_data(tweet)* * Inserts a tweet 
* *remove_{insert_property}(property):* * Removes any tweets in the list matching the proeprty
* *generate_random_tweet_list(size):* * Returns a random subset of current tweet list (used to make test and training sets)

**TweetScraper**
* *Constructor(consumer_key, consumer_secret, access_token, access_key):* * Initializes conncetion with twitter api. Access token and key not required
* *search(keyword, user, start_date, end_date):* * Searches twitter and returns a tweet list. Keyword is the only reqauired value. Combinations of {keyword, user},{keyword, user, start_date, end_date}, and {keyword,end_date} are supported
* *get_weekly_tweets(keyword):* * Gets tweets containing the keyword from the past week
* *list_members(user, slug):* * Gets members of a list
* *get_valuable_users(base_user):* * Gets all members of all base_users lists
* *users_lists(user):* * Gets user lists

**Data_To_Csv (Not used in Default Main)**
* *Constructor:* * Does nothing
* *write_data_to_csv(tweet_list, file_name):* * Writes tweets to a csv file at the file_name path. File_name defaults to src/Database/output/tweetlist.csv
* *read_data_from_csv(file_name):* * Reads tweets from a csv file and parses into a TweetList obj
* *write_userlist_to_csv(userlist, file_name):* * Writes a list of users to a csv file at the file_name path. File_name defaults to src/Database/output/userlist.csv
* *read_userlist_from_csv(file_name):* * Reads a column of users from csv. Returns python list

**Database**
* *Constructor(user, password, host, port):* * Attempts to initalize db 
* *create_table(name, column_name, column_type):* * Creates a table in the db with all column names in the vector column_name and their corresponding column_type. The number of column names and types must be equivalent.
* *num_rows(table_name, column_name):* * Returns the number of rows in a column
* *update_column_by_id(table_name, column_name, tweet_id, new_value):* * Updates the specified column name with a new value any time the id is the tweet_id
* *update_column_by_text(table_name, column_name, text, new_value):* * Updates the specified column name with a new value any time the text is equal to the text param
* *insert_tweet(table_name, tweet_id, tweet):* * Inserts a specific tweet
* *insert_tweet_list(table_name, tweet_list):* * Inserts all tweets in order of their storage in tweet_list
* *parse_db_into_tweet_list(name):* * Parses all tweets in the named table into tweet objs and then stores them in a TweetList obj

**PreProccessing**
* *Constructor:* * Builds stop words
* *process_tweets(list_tweets):* * Tokenizes a list of tweets and returns their associated tokenized array and label
* *generate_token_array(token_arr):* * Transforms the multiarray tokenized list of tweets into single dim array for inserting into db

**UserInterface**
* *Constructor(data, db, db_name):* * Initializes Widget Values. Set data equal to training set to classify tweets
* *Classify:* * Creates a ui for easily self-classifying tweets for the training set. Automatically updates DB\

**Plot**
* *constructor(db):* * Sets inital values
* *generate_projections(db_name, column_name):* * Gathers all manually classified tweet scores and assigns values
* *build_projections_histogram:* * Displays a histogram of manually classified results
* *create_classification_plot(pos_score, neg_score, neutral_score, irr_score):* * Displays a histogram of given params. Used to display results from NaiveBayes Classification Tool

