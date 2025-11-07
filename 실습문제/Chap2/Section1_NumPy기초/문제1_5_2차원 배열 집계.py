import numpy as np

data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
                 
# 1. 각 행의 합
print(data.sum(axis=1))  # [ 6 15 24]

# 2. 각 열의 평균
print(data.mean(axis=0))  # [4. 5. 6.]

# 3. 전체 합
print(data.sum())  # 45