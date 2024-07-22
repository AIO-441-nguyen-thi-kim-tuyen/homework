import numpy as np
from homework.module_2_week_2.eigenvector_eigenvalue import compute_eigenvalues_eigenvectors


# Question 11
def test_eigenvector_eigenvalue():
    matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
    # print(eigenvectors)
    assert (eigenvalues == np.array([1.0, 0.7])).all()
    assert (eigenvectors == np.array([[0.89442719, -0.70710678], [0.4472136, 0.70710678]])).all()
