from homework.module_2_week_3.iris_classifier import GaussianNaiveBayes, create_train_data_iris

train_data = create_train_data_iris()


def test_predict_example_1():
    classifier = GaussianNaiveBayes()
    classifier.fit(train_data)

    # Example 1
    X = [6.3, 3.3, 6.0, 2.5]
    pred = classifier.predict(X)
    print("Prediction:", pred)
    assert pred == "Iris-virginica"


def test_predict_example_2():
    classifier = GaussianNaiveBayes()
    classifier.fit(train_data)
    # Example 2
    X = [5.0, 2.0, 3.5, 1.0]
    pred = classifier.predict(X)
    print("Prediction:", pred)
    # Print the model
    classifier.print_model()
    assert pred == "Iris-versicolor"


def test_predict_example_3():
    classifier = GaussianNaiveBayes()
    classifier.fit(train_data)
    # Example 2
    X = [4.9, 3.1, 1.5, 0.1]
    pred = classifier.predict(X)
    print("Prediction:", pred)
    assert pred == "Iris-setosa"
