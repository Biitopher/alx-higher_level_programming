#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.dot(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("Invalid matrix dimensions. The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
    except Exception as e:
        raise Exception("An error occurred while multiplying matrices: {}".format(str(e)))
