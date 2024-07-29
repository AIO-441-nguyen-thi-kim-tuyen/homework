import numpy as np


class NaiveBayesClassifier:
    def __init__(self):
        self.classes = None
        self.class_probabilities = None
        self.conditional_probabilities = None
        self.feature_names = None

    def fit(self, data):
        self.classes = self._get_classes(data)
        self.class_probabilities = self._compute_prior_probability(data)
        self.conditional_probabilities, self.feature_names = self._compute_conditional_probability(data)

    def _get_classes(self, data):
        return np.unique(data[:, -1])

    def _compute_prior_probability(self, data):
        classes = self._get_classes(data)
        prior_probability = np.zeros(len(classes))
        data_len = len(data)

        for i, c in enumerate(classes):
            prior_probability[i] = len(np.where(data[:, -1] == c)[0]) / data_len

        return prior_probability

    def _compute_conditional_probability(self, data):
        y_unique = self.classes
        conditional_probability = []
        list_x_name = []

        for i in range(data.shape[1] - 1):
            x_unique = np.unique(data[:, i])
            list_x_name.append(x_unique)

            x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

            for j in range(len(y_unique)):
                for k in range(len(x_unique)):
                    x_conditional_probability[j, k] = len(
                        np.where((data[:, i] == x_unique[k]) & (data[:, -1] == y_unique[j]))[0]
                    ) / len(np.where(data[:, -1] == y_unique[j])[0])

            conditional_probability.append(x_conditional_probability)

        return conditional_probability, list_x_name

    def _get_index_from_value(self, feature_name, list_features):
        return np.where(list_features == feature_name)[0][0]

    def predict(self, instance):
        indexes = [self._get_index_from_value(instance[i], self.feature_names[i]) for i in range(len(instance))]
        p = np.log(self.class_probabilities)

        for c in range(len(self.classes)):
            for i in range(len(instance)):
                p[c] += np.log(self.conditional_probabilities[i][c, indexes[i]])

        return self.classes[np.argmax(p)]

    def print_model(self):
        print("Class Probabilities:")
        for c, prob in zip(self.classes, self.class_probabilities):
            print(f"{c}: {prob}")

        print("\nFeature Probabilities:")
        for c in range(len(self.classes)):
            print(f"Class {self.classes[c]}:")
            for i in range(len(self.feature_names)):
                print(f"  Feature {i} ({self.feature_names[i]}):")
                for val, prob in zip(self.feature_names[i], self.conditional_probabilities[i][c]):
                    print(f"    {val}: {prob}")


# Function to create training data
def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Sunny', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes'],
        ['Sunny', 'Mild', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Strong', 'yes'],
        ['Overcast', 'Hot', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Strong', 'no']
    ]
    return np.array(data)


# Function to compute prior probabilities
def compute_prior_probablity(train_data):
    y_unique = np.unique(train_data[:, -1])
    prior_probability = np.zeros(len(y_unique))
    train_data_len = len(train_data)

    for i in range(len(prior_probability)):
        prior_probability[i] = len(np.where(train_data[:, -1] == y_unique[i])[0]) / train_data_len

    return prior_probability


# Function to compute conditional probabilities
def compute_conditional_probability(train_data):
    y_unique = np.unique(train_data[:, -1])
    conditional_probability = []
    list_x_name = []

    for i in range(train_data.shape[1] - 1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))

        for j in range(len(y_unique)):
            for k in range(len(x_unique)):
                x_conditional_probability[j, k] = len(
                    np.where((train_data[:, i] == x_unique[k]) & (train_data[:, -1] == y_unique[j]))[0]
                ) / len(np.where(train_data[:, -1] == y_unique[j])[0])

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


# Function to predict play tennis
def prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability):
    indexes = [get_index_from_value(X[i], list_x_name[i]) for i in range(len(X))]

    p0 = prior_probability[0]
    p1 = prior_probability[1]

    for i in range(len(indexes)):
        p0 *= conditional_probability[i][0, indexes[i]]
        p1 *= conditional_probability[i][1, indexes[i]]

    return 'no' if p0 > p1 else 'yes'


def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


# Main function to run the classifier
if __name__ == "__main__":
    train_data = create_train_data()

    classifier = NaiveBayesClassifier()
    classifier.fit(train_data)

    # Predict a new instance
    new_instance = ['Sunny', 'Cool', 'High', 'Strong']
    print("Prediction:", classifier.predict(new_instance))

    # Print the model
    classifier.print_model()
