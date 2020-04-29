#!/usr/bin/python3
import numpy as np
from prediction import predict_

x = np.arange(1, 6)

print(repr(predict_(x, np.array([5, 0]))))
print(repr(predict_(x, np.array([0, 1]))))
print(repr(predict_(x, np.array([5, 3]))))
print(repr(predict_(x, np.array([-3, 1]))))
