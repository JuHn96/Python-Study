import numpy as np

# 1. 랜덤 데이터 생성
data = np.random.randint(0, 101, 30)

# 2. reshape
data_2d = data.reshape(5, 6)

# 3. 50 이상 값들의 평균
high_values = data[data >= 50].mean()
print(data_2d)
print(f"50 이상 값들의 평균: {high_values:.2f}")