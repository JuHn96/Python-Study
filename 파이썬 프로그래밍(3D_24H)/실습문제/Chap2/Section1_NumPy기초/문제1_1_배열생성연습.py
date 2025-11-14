import numpy as np

# 1부터 20까지의 배열
arr = np.array(range(1, 21))
print(arr)

# 0으로 채워진 3x4 배열
zeros_arr = np.zeros((3, 4))
print(zeros_arr)

# 1로 채워진 5x5 배열
ones_arr = np.ones((5, 5))
print(ones_arr)

# 10으로 채워진 2x3 배열
full = np.full((2, 3), 10)
print(full)