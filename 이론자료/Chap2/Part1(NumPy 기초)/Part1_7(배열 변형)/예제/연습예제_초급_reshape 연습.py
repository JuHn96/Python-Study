import numpy as np

# 1~24 배열을 다양한 모양으로
arr = np.arange(1, 25)

print("1차원:", arr)
print("\n2x12:\n", arr.reshape(2, 12))
print("\n4x6:\n", arr.reshape(4, 6))
print("\n3x8:\n", arr.reshape(3, 8))
print("\n2x3x4:\n", arr.reshape(2, 3, 4))