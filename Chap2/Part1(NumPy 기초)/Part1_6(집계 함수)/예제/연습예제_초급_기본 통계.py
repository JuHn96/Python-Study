import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89])

print(f"평균: {scores.mean():.1f}")
print(f"중앙값: {np.median(scores):.1f}")
print(f"최고점: {scores.max()}")
print(f"최저점: {scores.min()}")
print(f"표준편차: {scores.std():.2f}")
print(f"범위: {scores.max() - scores.min()}")
print(f"총점: {scores.sum()}")