from cost import cost_elem_, cost_
from prediction import predict_
import numpy as np


x1 = np.arange(0, 5)
theta1 = np.array([2, 4])
y_hat1 = predict_(x1, theta1)
y1 = np.array([2, 7, 12, 17, 22])
print(repr(cost_elem_(y1, y_hat1)))
print(repr(cost_(y1, y_hat1)))
