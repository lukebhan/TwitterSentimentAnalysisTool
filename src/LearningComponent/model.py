import nltk

# Class Model: A model for classifying tweets using Naive Bayes
class Model:
    # set inital classifier to none
    def __init__(self):
        self.word_features = None
        self.classifier = None

    # build a vocabulary of all tweets in training set
    def build_vocabulary(self, processed_multi_arr):
        vocab = []

        for (words, sentiment) in processed_multi_arr:
            vocab.extend(words)

        word_list = nltk.FreqDist(vocab)
        self.word_features = word_list.keys()

    # create a count of each word
    def extract_features(self, tweet_text):
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in tweet_text)
        return features

    # build feature vector with relative labeling
    def build_feature_vector(self, tokenized_data):
        feature_vector = nltk.classify.apply_features(self.extract_features, tokenized_data)
        return feature_vector

    # trains the classifier
    def train_classifier(self, feature_vector):
        self.classifier = nltk.NaiveBayesClassifier.train(feature_vector)
        return self.classifier

    # tests the classifier on a tweet (helper method for classify_test_set)
    def test_classifier(self, tweet):
        test = self.classifier.classify(self.extract_features(tweet))
        print(test)
        return test

    # classifies an entire test set
    def classify_test_set(self, test_set):
        return_labels = [self.test_classifier(test_set.data[index].tokenized_text) for index in test_set.data]
        return return_labels

