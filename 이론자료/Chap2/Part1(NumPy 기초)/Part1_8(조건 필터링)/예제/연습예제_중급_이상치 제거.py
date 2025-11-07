import numpy as np

data = np.array([10, 12, 11, 13, 10, 9, 100, 11, 12, 10,
                 13, 14, 11, 2, 12, 13, 11, 10])
print("원본:", data)
print(f"평균: {data.mean():.2f}, 표준편차: {data.std():.2f}")

# 이상치 판별 (평균 ± 2*표준편차 범위 밖)
mean = data.mean()
std = data.std()
lower = mean - 2 * std
upper = mean + 2 * std

# 정상 범위 데이터만
normal_data = data[(data >= lower) & (data <= upper)]
print(f"\n정상 데이터: {normal_data}")
print(f"제거된 이상치: {data[(data < lower) | (data > upper)]}")
print(f"정제 후 평균: {normal_data.mean():.2f}")