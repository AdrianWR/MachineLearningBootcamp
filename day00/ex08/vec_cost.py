def cost_(y, y_hat):
    """Computes the mean squared error of two non-empty numpy.ndarray,
    without any for loop.
    The two arrays must have the same dimensions.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    The mean squared error of the two vectors as a float.
    None if y or y_hat are empty numpy.ndarray.
    None if y and y_hat does not share the same dimensions.
    Raises:
    This function should not raise any Exceptions.
    """""""""
    if not len(y) or not len(y_hat):
        return None
    if y.shape != y_hat.shape:
        return None
    return np.dot(y_hat - y, y_hat - y) / len(y)


if __name__ == "__main__":
    import numpy as np
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    print(repr(cost_(X, Y)))
    print(repr(cost_(X, X)))
