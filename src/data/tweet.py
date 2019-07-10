class tweet:
    def __init__(self):
        self.tweet = {}

    def insert_data(self, name, value):
        self.tweet[name] = value

    def remove_data(self, name):
        del self.tweet[name]



