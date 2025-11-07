import numpy as np

# 1부터 10까지 배열
numbers = np.arange(1, 11)
print("1~10:", numbers)

# 5x5 단위 행렬
identity = np.eye(5)
print("단위 행렬:\n", identity)

# 3x4 영행렬
zeros = np.zeros((3, 4))
print("영행렬:\n", zeros)