import numpy as np
from homework.module_2_week_2.eigenvector_eigenvalue import compute_eigenvalues_eigenvectors
import numpy.testing as npt
import sys

epsilon = sys.float_info.epsilon

# Question 11
def test_eigenvector_eigenvalue():
    matrix = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
    print(eigenvectors)
    print(eigenvalues)
    # print(npt.assert_array_almost_equal(eigenvalues, np.array([1.0, 0.7]), decimal=2))
    # assert (eigenvectors == np.array([[0.89442719, -0.70710678], [0.4472136, 0.70710678]])).all()
    assert abs(round(eigenvalues[0],  1) - 1) < epsilon
    assert abs(round(eigenvalues[1],  1) - 0.7) < epsilon
    assert abs(round(eigenvectors[0][0], 2) - 0.89) < epsilon