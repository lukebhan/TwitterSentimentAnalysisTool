import nltk


class Model:
    def __init__(self):
        self.word_features = None
        self.classifier = None

    def build_vocabulary(self, processed_multi_arr):
        vocab = []

        for words in processed_multi_arr:
            vocab.extend(words)

        word_list = nltk.FreqDist(vocab)
        self.word_features = word_list.keys()

    def extract_features(self, tweet_text):
        features = {}
        for word in self.word_features:
            features['contains(%s)' % word] = (word in tweet_text)
        return features

    def build_feature_vector(self, tokenized_data):
        feature_vector = nltk.classify.apply_features(self.extract_features, tokenized_data)
        return feature_vector

    def train_classifier(self, feature_vector):
        self.classifier = nltk.NaiveBayesClassifier.train(feature_vector)
        return self.classifier