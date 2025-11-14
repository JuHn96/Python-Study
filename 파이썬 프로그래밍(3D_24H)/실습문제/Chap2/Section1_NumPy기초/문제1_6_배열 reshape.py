import numpy as np

arr = np.arange(24)

# 1. 4행 6열
arr1 = arr.reshape(4, 6)
print(arr1)

# 2. 3행 8열
arr2 = arr.reshape(3, 8)
print(arr2)

# 3. 2x3x4 (3차원)
arr3 = arr.reshape(2, 3, 4)
print(arr3)