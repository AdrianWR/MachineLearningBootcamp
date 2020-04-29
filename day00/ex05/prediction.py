import numpy as np


def predict_(x, theta):
    """Computes the vector of prediction y_hat from
    two non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    y_hat as a numpy.ndarray, a vector of dimension m * 1.
    None if x or theta are empty numpy.ndarray.
    None if x or theta dimensions are not appropriate.
    Raises:
    This function should not raise any Exceptions.
    """""""""
    if len(x) == 0 or len(theta) == 0:
        return None
    elif theta.shape != (2,) or len(x.shape) != 1:
        return None
    ones = np.ones(len(x))
    X = np.vstack((ones, x))
    X = X.T
    return X @ theta
