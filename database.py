import psycopg2


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
        self.connection.commit();
        self.connection.close();
        self.cursor.close();

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

    def insert_data(self, name, column_name, data):
        if len(data.shape) > 1:
            for vector in data:
                table_command = "INSERT INTO " + name + "("
                for item in column_name:
                    table_command += item + ", "
                table_command = table_command[:-2]
                table_command += ") VALUES ('"
                for value in vector:
                    table_command += str(value).replace("'", "") + "', '"
                table_command = table_command[:-3]
                table_command += ");"
                self.cursor.execute(table_command)
        elif len(data.shape) == 0:
            print("no tweets in data")
        else:
            table_command = "INSERT INTO " + name + "("
            for name in column_name:
                table_command += name + ", "
            table_command = table_command[:-2]
            table_command += ") VALUES ('"
            for value in data:
                table_command += str(value) + "', '"
            print(table_command)
            table_command = table_command[:-3]
            table_command += ");"
            self.cursor.execute(table_command)
