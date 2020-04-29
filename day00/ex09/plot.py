import matplotlib.pyplot as plt
import numpy as np


def plot_with_cost(x, y, theta):
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
    y_hat = predict(x, theta)
    plt.plot(x, y, 'o')
    plt.plot(x, y_hat)
    for i in range(len(x)):
        plt.plot([x[i], x[i]], [y_hat[i], y[i]], 'r--')
    cost = np.dot(y_hat - y, y_hat - y) / len(y)
    plt.title(f"Cost: {round(cost, 6)}")
    plt.show()
