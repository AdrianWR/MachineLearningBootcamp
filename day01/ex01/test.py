from cost import cost_elem_, cost_, mse
from prediction import predict_
import numpy as np


X = np.array([0, 15, -9, 7, 12, 3, -21])
Y = np.array([2, 14, -13, 5, 12, 4, -19])

print(cost_(X, Y))
