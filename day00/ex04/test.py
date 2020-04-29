#!/usr/bin/python3

import numpy as np
from tools import add_intercept

if __name__ == "__main__":
    print(repr(add_intercept(np.arange(1, 6))))
    print(repr(add_intercept(np.arange(1, 10).reshape(3, 3))))
