#!/usr/bin/python3
from plot import plot
import numpy as np


if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287,
                  4.66793434, 5.95585554])
    plot(x, y, np.array([4.5, -0.2]))
    plot(x, y, np.array([-1.5, 2]))
    plot(x, y, np.array([3, 0.3]))
