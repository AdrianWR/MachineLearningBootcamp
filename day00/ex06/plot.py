import matplotlib.pyplot as plt
import numpy as np


def plot(x, y, theta):
    """Plot the data and prediction line from three non-empty numpy.ndarray.
    Args:
    x: has to be an numpy.ndarray, a vector of dimension m * 1.
    y: has to be an numpy.ndarray, a vector of dimension m * 1.
    theta: has to be an numpy.ndarray, a vector of dimension 2 * 1.
    Returns:
    Nothing.
    Raises:
    This function should not raise any Exceptions.
    """""""""
    def predict(x, t): return np.vstack((np.ones(len(x)), x)).T @ t
    plt.plot(x, y, 'o')
    plt.plot(x, predict(x, theta))
    plt.show()
