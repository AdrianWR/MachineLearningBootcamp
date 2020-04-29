#!/usr/bin/python3
import numpy as np
from prediction import simple_predict

x = np.arange(1, 6)

print(simple_predict(x, np.array([5, 0])))
print(simple_predict(x, np.array([0, 1])))
print(simple_predict(x, np.array([5, 3])))
print(simple_predict(x, np.array([-3, 1])))
