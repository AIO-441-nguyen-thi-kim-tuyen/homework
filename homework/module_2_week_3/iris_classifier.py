import os.path

import numpy as np
import math


class GaussianNaiveBayes:
    def __init__(self):
        self.classes = None
        self.class_probabilities = None
        self.conditional_probabilities = None

    def fit(self, data):
        self.classes = np.unique(data[:, -1])
        self.class_probabilities = self._compute_prior_probability(data)
        self.conditional_probabilities = self._compute_conditional_probability(data)

    def _compute_prior_probability(self, data):
        prior_probability = np.zeros(len(self.classes))
        for i, c in enumerate(self.classes):
            prior_probability[i] = len(np.where(data[:, -1] == c)[0]) / len(data)
        return prior_probability

    def _compute_conditional_probability(self, data):
        conditional_probability = []
        for i in range(data.shape[1] - 1):
            feature_probs = np.zeros((len(self.classes), 2))
            for j, c in enumerate(self.classes):
                feature_data = (data[:, i][np.where(data[:, -1] == c)]).astype(float)
                mean = np.mean(feature_data)
                sigma = np.var(feature_data)
                feature_probs[j] = [mean, sigma]
            conditional_probability.append(feature_probs)
        return conditional_probability

    def _gaussian(self, x, mean, sigma):
        return (1.0 / (np.sqrt(2 * math.pi * sigma))) * np.exp(-(float(x) - mean) ** 2 / (2 * sigma))

    def predict(self, X):
        posteriors = np.log(self.class_probabilities)
        for i in range(len(self.classes)):
            for j in range(len(X)):
                posteriors[i] += np.log(self._gaussian(X[j], self.conditional_probabilities[j][i][0],
                                                       self.conditional_probabilities[j][i][1]))
        return self.classes[np.argmax(posteriors)]

    def print_model(self):
        print("Class Probabilities:")
        for c, prob in zip(self.classes, self.class_probabilities):
            print(f"{c}: {prob}")

        print("\nFeature Probabilities:")
        for i, c in enumerate(self.classes):
            print(f"Class {c}:")
            for j, (mean, sigma) in enumerate(self.conditional_probabilities):
                print(f"  Feature {j}: Mean = {mean[i][0]}, Variance = {mean[i][1]}")


def create_train_data_iris():
    # Assuming iris.data.txt is in the same directory with the following format
    # sepal length, sepal width, petal length, petal width, class
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, "tests", "module_2_week_3", "iris.data.txt"))
    data = np.loadtxt(file_path, delimiter=",", dtype=str)
    return data


# Main function to run the classifier
if __name__ == "__main__":
    train_data = create_train_data_iris()

    classifier = GaussianNaiveBayes()
    classifier.fit(train_data)

    # Example 1
    X = [6.3, 3.3, 6.0, 2.5]
    print("Prediction:", classifier.predict(X))

    # Example 2
    X = [5.0, 2.0, 3.5, 1.0]
    print("Prediction:", classifier.predict(X))

    # Example 3
    X = [4.9, 3.1, 1.5, 0.1]
    print("Prediction:", classifier.predict(X))

    # Print the model
    classifier.print_model()
