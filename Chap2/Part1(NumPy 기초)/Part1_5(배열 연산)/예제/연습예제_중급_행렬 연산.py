import numpy as np

# 두 행렬
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
              
# 요소별 곱셈
element_wise = A * B
print("요소별 곱셈:\n", element_wise)

# 행렬 곱셈
matrix_mult = np.dot(A, B)  # 또는 A @ B
# [[1*5+2*7  1*6+2*8]     [[19 22]
#  [3*5+4*7  3*6+4*8]]  =  [43 50]]
print("\n행렬 곱셈:\n", matrix_mult)

# 전치
print("\nA 전치:\n", A.T)

# 역행렬
A_inv = np.linalg.inv(A)
print("\nA 역행렬:\n", A_inv)

# 검증: A * A^(-1) = I
identity = np.dot(A, A_inv)
print("\nA * A^(-1):\n", np.round(identity, 2))