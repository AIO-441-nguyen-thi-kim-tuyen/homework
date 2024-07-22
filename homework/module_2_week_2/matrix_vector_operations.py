import numpy as np

"""
1.1 Length of a vector 
"""


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum([v ** 2 for v in vector]))
    return len_of_vector


def compute_vector_length_v2(vector):
    len_of_vector = np.linalg.norm(vector)
    return len_of_vector


"""
1.2. Dot Product
"""


def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    return dot_product


"""
1.3 Multiplying a vector by a matrix
"""


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


"""
1.4. Multiplying a matrix by a matrix
"""


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


"""
1.5. Matrix inverse
"""


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result
