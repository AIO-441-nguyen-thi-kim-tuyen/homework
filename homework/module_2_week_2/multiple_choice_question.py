import numpy as np


# . Question 3
def question_3_multiply_matrix_vector():
    x = np.array([[1, 2], [3, 4]])
    k = np.array([1, 2])
    arr = x.dot(k)
    print('result \n', arr)
    return arr


# Question_4
def question_4_multiply_matrix_vector():
    x = np.array([[-1, 2], [3, -4]])
    k = np.array([1, 2])
    arr = x @ k
    print('result \n', arr)
    return arr


# Question 7
def question_7_multiply_matrix_matrix():
    m1 = np.eye(3)
    m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    result = m1 @ m2
    print(result)
    return result


# Question 8
def question_8_multiply_vector_matrix():
    m1 = np.eye(2)
    m1 = np.reshape(m1, (-1, 4))[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1 @ m2
    print(result)
    return result


# Question 9
def question_9_multiply_vector_matrix():
    m1 = np.array([[1, 2], [3, 4]])
    m1 = np.reshape(m1, (-1, 4), "F")[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1 @ m2
    print(result)
    return result
