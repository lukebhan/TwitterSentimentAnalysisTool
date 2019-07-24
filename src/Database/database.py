import psycopg2


# Class Database: Adds and removes objects from postgres
class Database:
    # constructor to initialize connection
    def __init__(self, user, password, host, port):
        self.connection = psycopg2.connect(user=user, password=password, host=host, port=port)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT version();")
        record = self.cursor.fetchone()
        print("Your are connect to - ", record)

    # destructor to commit changes to database
    def __del__(self):
        self.connection.commit()
        self.connection.close()
        self.cursor.close()

    # creates a tables with the input name and with the vector size of the name and type params
    # Takes in a string and two lists of string
    def create_table(self, name, column_name, column_type):
        if len(column_name) != len(column_type):
            raise ValueError("column names must match size of column types")
        table_command = "CREATE TABLE " + name + " ("
        for i in range(len(column_name)):
            table_command += column_name[i] + " " + column_type[i] + ", "
        table_command = table_command[:-2]
        table_command += ");"
        print(table_command)
        self.cursor.execute(table_command)

    # Returns number of rows in a specific column
    # Takes in two strings
    def num_rows(self, table_name, column_name):
        table_command = "SELECT COUNT(" + column_name + ") FROM " + table_name
        return self.cursor.execute(table_command)

    # updates a column based on id
    def update_column(self, table_name, column_name, id, new_value):
        table_command = "UPDATE " + table_name + " SET " + column_name + " = " + new_value + \
                        " WHERE id = " + id
        self.cursor.execute(table_command)

    # creates a new column and adds data in form of a data object to it into it
    def create_column(self, table_name, column_name, data, type_data):
        table_command = "ALTER TABLE " + table_name + " ADD COLUMN " + column_name + " " + type_data
        self.cursor.execute(table_command)
        for tweet in data:
            self.insert_tweet(table_name, column_name, tweet)

    # deletes a row
    def delete_row(self, table_name, id):
        table_command = "DELETE FROM " + table_name + " WHERE id =" + id
        self.cursor.execute(table_command)

    # gets column data and returns as list
    def get_column_data(self, table_name, column_name):
        table_command = "SELECT " + column_name + " FROM " + table_name
        self.cursor.execute(table_command)
        return self.cursor.fetchall()

    # gets row data and returns as a tweet
    def get_row_data(self, table_name, id):
        table_command = "SELECT * WHERE id = " + id
        self.cursor.execute(table_command)
        print(self.cursor.fetchall)

    # inserts a tweet object into a table
    def insert_tweet(self, table_name, id, tweet):
        if tweet.follower_count > 2000:
            table_command = "INSERT into {0}" \
                            " VALUES ({1}, '{2}', '{3}', {4}, {5}, {6}, '{7}', '{8}', '{9}')".format(table_name, str(id),
                                                                                      self.check_none(tweet.text).replace(
                                                                                          "'", ""),
                                                                                      self.check_none(tweet.user),
                                                                                      self.check_none(tweet.retweet_count),
                                                                                      self.check_none(tweet.favorite_count),
                                                                                      self.check_none(tweet.follower_count),
                                                                                      self.check_none(tweet.date),
                                                                                      self.check_none(tweet.nlp_score),
                                                                                      self.check_none(tweet.given_score))
            print(table_command)
            self.cursor.execute(table_command)

    # inserts a list of tweet objects
    def insert_tweet_list(self, table_name, tweet_list):
        for value in tweet_list.data:
            self.insert_tweet(table_name, value, tweet_list.data[value])

    # inserts a general list
    def insert_list(self, table_name, list):
        for value in list:
            table_command = "INSERT into {0} VALUES ('{1}')".format(table_name, value)
            self.cursor.execute(table_command)

    # helper method for insert_data
    @staticmethod
    def check_none(value):
        if value is None:
            return "-10"
        else:
            return value

    def commit(self):
        self.connection.commit()

