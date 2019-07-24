import tkinter


# UI Class: This class creates a ui for manually scoring tweets
# Written by Luke Bhan
# Last Updated: 7/15/19
class UserInterface:
    # default constructor
    def __init__(self, data, db, db_name):
        # initialize variables for iterating through data
        self.count = 1
        self.data = data
        self.db_name = db_name
        self.db = db

        # create root frame for ui, assign background color and initial size
        self.root = tkinter.Tk()
        self.root.configure(bg="#ebeef3")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=3)
        self.root.geometry('700x200')
        self.root.title("Twitter Sentiment Analysis Tool (TSAT) Training Set Builder")

        # create an upper frame container
        self.upper_frame = tkinter.Frame(self.root)
        self.upper_frame.grid(column=0, row=0)

        # create a lower frame container
        self.lower_frame = tkinter.Frame(self.root)
        self.lower_frame.grid(column=0, row=1)
        self.lower_frame.rowconfigure(0, weight=1)

        # create variables for updating text within labels
        self.text_var = tkinter.StringVar()
        self.count_text = tkinter.StringVar()

    # calls widget and runs it
    def classify(self):
        self.widget()
        self.root.mainloop()

    # lowers count by 1 and updates to go back a tweet
    def go_bck_callback(self):
        self.count -= 1
        self.update_text()

    # updates to next tweet and scores the prev tweet as positive
    def pos_callback(self):
        self.data.get_tweet(self.count).add_given_score(1)
        self.db.update_column_by_text(self.db_name, 'given_score', self.data.get_tweet(self.count).text,
                              self.data.get_tweet(self.count).given_score)
        self.count += 1
        self.update_text()

    # updates to next tweet and scores the prev tweet as negative
    def neg_callback(self):
        self.data.get_tweet(self.count).add_given_score(-1)
        self.db.update_column_by_text(self.db_name, 'given_score', self.data.get_tweet(self.count).text,
                              self.data.get_tweet(self.count).given_score)
        self.count += 1
        self.update_text()

    # updates to next tweet and scores the prev tweet as neutral
    def neutral_callback(self):
        self.data.get_tweet(self.count).add_given_score(0)
        self.db.update_column_by_text(self.db_name, 'given_score', self.data.get_tweet(self.count).text,
                              self.data.get_tweet(self.count).given_score)
        self.count += 1
        self.update_text()

    # updates to next tweet and scores the prev tweet as irrelevant
    def irr_callback(self):
        self.data.get_tweet(self.count).add_given_score(100)
        self.db.update_column_by_text(self.db_name, 'given_score', self.data.get_tweet(self.count).text,
                              self.data.get_tweet(self.count).given_score)
        self.count += 1
        self.update_text()

    # defines a user interface to select score of tweet
    def widget(self):
        # set initial variables
        self.text_var.set(self.data.get_tweet(self.count).text)
        self.count_text.set("Count: " + str(self.count) + "/" + str(self.data.get_size()))

        # print tweet text
        tweet_text = tkinter.Label(self.upper_frame, wraplength='500', textvariable=self.text_var, relief="groove",
                                   fg='#3e4247', borderwidth=2, highlightcolor='#326690', font='Helvetica',
                                   bg='#d6effc')
        tweet_text.grid(column=1, row=0)

        # print counter next to tweet text
        counter = tkinter.Label(self.upper_frame, wraplength='70', textvariable=self.count_text, relief="groove",
                                fg='#3e4247', borderwidth=2, highlightcolor='#326690', font='Helvetica', bg='#d6effc')
        counter.grid(column=2, row=0)

        # create buttons for iterating and choosing scores
        go_bck_button = tkinter.Button(self.lower_frame, text="Go Back", command=self.go_bck_callback, bg='#5b6d7c',
                                       font='Helvetica', fg='white')
        go_bck_button.grid(column=0, row=0)

        pos_button = tkinter.Button(self.lower_frame, text="Positive", command=self.pos_callback, bg='#5b6d7c',
                                    font='Helvetica', fg='white')
        pos_button.grid(column=3, row=0)

        neg_button = tkinter.Button(self.lower_frame, text="Negative", command=self.neg_callback, bg='#5b6d7c',
                                    font='Helvetica', fg='white')
        neg_button.grid(column=1, row=0)

        neutral_button = tkinter.Button(self.lower_frame, text="Neutral", command=self.neutral_callback, bg='#5b6d7c',
                                        font='Helvetica', fg='white')
        neutral_button.grid(column=2, row=0)

        irr_button = tkinter.Button(self.lower_frame, text="Irrelevant", command=self.irr_callback, bg='#5b6d7c',
                                    font='Helvetica', fg='white')
        irr_button.grid(column=4, row=0)

    # exception safety and updating tweets in real time
    def update_text(self):
        # terminate if count = size+1
        if self.count == self.data.get_size() + 1:
            self.text_var.set("Data Training is Comlpete. To edit, use the go back button. Otherwise close the window")
        # check to make sure user does not go to far back
        else:
            # noinspection PyBroadException
            try:
                self.text_var.set(self.data.get_tweet(self.count).text)
                self.count_text.set("Count: " + str(self.count) + "/" + str(self.data.get_size()))
            except IndexError:
                print("Tweet index not available")
