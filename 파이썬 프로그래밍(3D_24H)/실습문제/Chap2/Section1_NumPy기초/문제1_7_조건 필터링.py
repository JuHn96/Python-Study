import numpy as np

data = np.array([15, 23, 8, 42, 16, 30, 7, 19, 25, 31])

# 1. 20 이상
print(data[data >= 20])  # [23 42 30 25 31]

# 2. 10 이하
print(data[data <= 10])  # [8 7]

# 3. 15와 25 사이
print(data[(data >= 15) & (data <= 25)])  # [15 23 16 19 25]