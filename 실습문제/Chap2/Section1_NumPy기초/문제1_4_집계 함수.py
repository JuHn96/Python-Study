import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89])

print(f"평균: {scores.mean()}")
print(f"최고점: {scores.max()}")
print(f"최저점: {scores.min()}")
print(f"표준편차: {scores.std():.2f}")
print(f"총점: {scores.sum()}")