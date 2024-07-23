import numpy as np
from homework.module_2_week_2.matrix_vector_operations import compute_vector_length, compute_vector_length_v2, \
    compute_dot_product, matrix_multi_vector, matrix_multi_matrix, inverse_matrix
from homework.module_2_week_2.multiple_choice_question import question_3_multiply_matrix_vector, \
    question_4_multiply_matrix_vector, \
    question_7_multiply_matrix_matrix, question_8_multiply_vector_matrix, question_9_multiply_vector_matrix


# Question 1
def test_compute_vector_length():
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length([vector])
    assert round(result, 2) == 23.28


def test_compute_vector_length_v2():
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length_v2([vector])
    assert round(result, 2) == 23.28


# Question 2
def test_compute_dot_product():
    v1 = np.array([0, 1, -1, 2])
    v2 = np.array([2, 5, 1, 0])
    result = compute_dot_product(v1, v2)
    print(round(result, 2))
    assert round(result, 2) == 4


# Question 3
def test_compute_dot_product_2():
    arr = question_3_multiply_matrix_vector()
    assert all(arr == np.array([5, 11]))


# Question 4
def test_compute_dot_product_3():
    arr = question_4_multiply_matrix_vector()
    assert (arr == np.array([3, -5])).all()


# Question 5
def test_matrix_multi_vector():
    m = np.array([[-1, 1, 1], [0, -4, 9]])
    v = np.array([0, 2, 1])
    result = matrix_multi_vector(m, v)
    # print(result)
    assert (result == np.array([3, 1])).all()


# Question 6
def test_matrix_multi_matrix():
    m1 = np.array([[0, 1, 2], [2, -3, 1]])
    m2 = np.array([[1, -3], [6, 1], [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    # print(result)
    assert (result == np.array([[6, -1], [-16, -10]])).all()


# Question 7
def test_matrix_multi_matrix_2():
    result = question_7_multiply_matrix_matrix()
    assert (result == np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])).all()


# Question 8
def test_matrix_multi_matrix_3():
    result = question_8_multiply_vector_matrix()
    assert (result == np.array([5, 5, 5, 5])).all()


# Question 9
def test_matrix_multi_matrix_4():
    result = question_9_multiply_vector_matrix()
    assert (result == np.array([29, 29, 29, 29])).all()


# Question 10
def test_inverse_matrix():
    m1 = np.array([[-2, 6], [8, -4]])
    result = inverse_matrix(m1)
    # print(result)
    assert (result == np.array([[0.1, 0.15], [0.2, 0.05]])).all()
