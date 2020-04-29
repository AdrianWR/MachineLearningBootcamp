import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from other_costs import mse_, rmse_, mae_, r2score_
from math import sqrt

x = np.array([0, 15, -9, 7, 12, 3, -21])
y = np.array([2, 14, -13, 5, 12, 4, -19])

print(f"\nOTHER_COSTS")
print(f"MSE:\t{mse_(x, y)}")
print(f"RMSE:\t{rmse_(x, y)}")
print(f"MAE:\t{mae_(x, y)}")
print(f"R2:\t{r2score_(x, y)}")


print(f"\nSKLEARN")
print(f"MSE:\t{mean_squared_error(x, y)}")
print(f"RMSE:\t{sqrt(mean_squared_error(x, y))}")
print(f"MAE:\t{mean_absolute_error(x, y)}")
print(f"R2:\t{r2_score(x, y)}")
