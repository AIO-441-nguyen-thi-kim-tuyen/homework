import numpy as np
from homework.module_2_week_2.matrix_vector_operations import compute_dot_product, compute_vector_length


def compute_cosine(v1, v2):
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return cos_sim


def compute_cosine_v2(v1, v2):
    cos_sim = compute_dot_product(v1, v2) / (compute_vector_length(v1) * compute_vector_length(v2))
    return cos_sim
