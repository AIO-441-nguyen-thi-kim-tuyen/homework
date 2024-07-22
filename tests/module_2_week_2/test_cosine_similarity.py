import numpy as np
from homework.module_2_week_2.cosine_similarity import compute_cosine


def test_compute_cosine_similarity():
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 0, 3, 0])
    result = compute_cosine(x, y)
    print(round(result, 3))
