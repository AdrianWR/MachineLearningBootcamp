#!/usr/bin/python3
from plot import plot_with_cost
import numpy as np


if __name__ == "__main__":
    x = np.arange(1, 6)
    y = np.array([11.52434424, 10.62589482, 13.14755699,
                  18.60682298, 14.14329568])
    plot_with_cost(x, y, np.array([18, -1]))
    plot_with_cost(x, y, np.array([14, 0]))
    plot_with_cost(x, y, np.array([12, 0.8]))
