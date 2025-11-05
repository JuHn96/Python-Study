import numpy as np

# 두 벡터 연산
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

print("덧셈:", v1 + v2)
print("뺄셈:", v1 - v2)
print("곱셈:", v1 * v2)
print("나눗셈:", v2 / v1)

# 내적 (dot product)
dot = np.dot(v1, v2) # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
print(f"내적: {dot}")

# 벡터 크기 계산
'''
linalg: Linear Algebra (선형대수)
norm: 노름(Norm), 벡터의 길이/크기 측정
'''
magnitude = np.linalg.norm(v1) # 각 요소를 제곱하고, 합한 후, 루트
print(f"v1 크기: {magnitude:.2f}")

# 행렬 곱셈 (2차원)
A = np.array([[1, 2],
              [3, 4]])  # (2, 2)

B = np.array([[5, 6],
              [7, 8]])  # (2, 2)

print(np.dot(A, B))
'''
[[1*5+2*7  1*6+2*8]     [[19 22]
[3*5+4*7  3*6+4*8]]  =  [43 50]]
'''

### 계산 과정
'''
A의 1행 · B의 1열 = 1*5 + 2*7 = 19
A의 1행 · B의 2열 = 1*6 + 2*8 = 22
A의 2행 · B의 1열 = 3*5 + 4*7 = 43
A의 2행 · B의 2열 = 3*6 + 4*8 = 50
'''