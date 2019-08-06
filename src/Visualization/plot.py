import matplotlib.pyplot as plt


# Plot Class: Class is used to visualize classification and projection data
class Plot:
    # initialize variables to 0
    def __init__(self, db):
        self.db = db
        self.pos_count = 0
        self.neg_count = 0
        self.irr_count = 0
        self.neutral_count = 0

    # from db, gather given scores and assign variables
    def generate_projections(self, db_name, column_name):
        data = self.db.get_column_data(db_name, column_name)
        print(data)
        for value in data:
            if value[0] == 1:
                self.pos_count += 1
            if value[0] == 100:
                self.irr_count += 1
            if value[0] == -1:
                self.neg_count += 1
            if value[0] == 0:
                self.neutral_count += 1

    # create a histogram with the given scores
    def build_projections_histogram(self):
        x_values = ['Negative', 'Neutral', 'Positive', 'Irrelevant']
        y_values = [self.neg_count, self.neutral_count, self.pos_count, self.irr_count]

        fig, ax = plt.subplots()
        ax.bar(x_values, y_values, color='orange')
        plt.title("Given Scores for Training Set")
        plt.ylabel("Count")
        plt.xlabel("Given_Score")

        plt.show()

    # creates a histogram with the classified scores
    @staticmethod
    def create_classification_plot(pos_score, neg_score, neutral_score, irr_score):
        x_values = ['Negative', 'Neutral', 'Positive', 'Irrelevant']
        y_values = [neg_score, neutral_score, pos_score, irr_score]

        fig, ax = plt.subplots()
        ax.bar(x_values, y_values, color='orange')
        plt.title("Given Scores for Classifying Test Set")
        plt.ylabel("Count")
        plt.xlabel("Given_Score")
