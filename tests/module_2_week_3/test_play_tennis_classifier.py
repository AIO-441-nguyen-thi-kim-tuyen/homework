import numpy as np

from homework.module_2_week_3.play_tennis_classifier import (NaiveBayesClassifier, create_train_data,
                                                             get_classes, compute_prior_probability,
                                                             get_index_from_value, prediction_play_tennis)

train_data = create_train_data()


def test_get_classes():
    classes = get_classes(train_data)
    assert classes[0] == 'no'
    assert classes[1] == 'yes'


def test_compute_prior_probability():
    prior_probability = compute_prior_probability(train_data)
    assert prior_probability[0] == 0.4
    assert prior_probability[1] == 0.6


def test_get_index_from_value():
    classifier = NaiveBayesClassifier()
    classifier.fit(train_data)
    outlook = classifier.feature_names[0]
    i1 = get_index_from_value("Overcast", outlook)
    i2 = get_index_from_value("Rain", outlook)
    i3 = get_index_from_value("Sunny", outlook)
    assert i1 == 0
    assert i2 == 1
    assert i3 == 2


def test_compute_conditional_probability():
    classifier = NaiveBayesClassifier()
    classifier.fit(train_data)
    conditional_probability = classifier.conditional_probabilities
    x1 = get_index_from_value("Sunny", classifier.feature_names[0])
    p = np.round(conditional_probability[0][1, x1], 2)
    print("P( 'Outlook'= 'Sunny'| 'Play Tennis'= 'Yes') = ", p)
    assert p == 0.17


def test_predict_naive_bayes_classifier():
    classifier = NaiveBayesClassifier()
    classifier.fit(train_data)

    # Predict a new instance
    new_instance = ['Sunny', 'Cool', 'High', 'Strong']
    result = classifier.predict(new_instance)
    print("Prediction:", result)
    assert result == 'no'
    # Print the model
    classifier.print_model()


def test_predict_play_tennis():
    classifier = NaiveBayesClassifier()
    classifier.fit(train_data)
    X = ['Sunny', 'Cool', 'High', 'Strong']
    result = prediction_play_tennis(X, classifier.feature_names, classifier.class_probabilities, classifier.conditional_probabilities)
    assert result == 'no'
