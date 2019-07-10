import psycopg2

# Database for handling postgres communication
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
    def create_table(self, name, column_name, column_type):
        if len(column_name) != len(column_type):
            raise ValueError("column names must match size of column types")
        table_command = "CREATE TABLE " + name + " ("
        for i in range(len(column_name)):
            table_command += column_name[i] + " " + column_type[i] + ", "
        table_command = table_command[:-2]
        table_command += ");"
        self.cursor.execute(table_command)

    # inserts data into a table
    def insert_data(self, name, column_name, data):


    # Returns number of rows in a specific column
    def num_rows(self, table_name, column_name):
        table_command = "SELECT COUNT(" + column_name + ") FROM " + table_name
        return self.cursor.execute(table_command)

    # updates column with a data score. Takes data in as a list of dictionaries
    def update_column(self, table_name, column_name, data):
        for value in data:
            print(value)
            table_command = "UPDATE " + table_name + " SET " + column_name + " = " + value["updated_text"] + \
                            " WHERE text = " + value["text"]
            self.cursor.execute(table_command)

    # creates a new column and adds data into it
    def create_column(self, table_name, column_name, data, type_data):
        table_command = "ALTER TABLE " + table_name + " ADD COLUMN " + column_name + " " + type_data
        self.cursor.execute(table_command)
        if type(data) is list:
            for value in data:
                self.insert_array(table_name,column_name, value)
        else:
            for value in data:
                self.insert_data(table_name, column_name, value)

    # deletes a row (helper method for updating column's with nlp scores)
    def delete_row(self, table_name, text):
        table_command = "DELETE FROM " + table_name + " WHERE text=" + text
        self.cursor.execute(table_command)

    def get_column_data(self, table_name, column_name):
        table_command = "SELECT " + column_name + " FROM " + table_name
        self.cursor.execute(table_command)
        return self.cursor.fetchall()
