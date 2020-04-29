def cost_elem_(y, y_hat):
    """
    Description:
    Calculates all the elements (1/2*M)*(y_pred - y)^2 of the cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_elem: ndarray, a vector of dimension (number of the training examples).
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    if y.shape != y_hat.shape:
        return None
    return ((y_hat - y) ** 2) / (2 * len(y))


def cost_(y, y_hat):
    """
    Description:
    Calculates the value of cost function.
    Args:
    y: has to be an numpy.ndarray, a vector.
    y_hat: has to be an numpy.ndarray, a vector.
    Returns:
    J_value : has to be a float.
    None if there is a dimension matching problem between X, Y or theta.
    Raises:
    This function should not raise any Exception.
    """
    if y_hat.shape != y.shape:
        return None
    return sum(cost_elem_(y, y_hat))
