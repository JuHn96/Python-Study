import matplotlib.pyplot as plt
import numpy as np

# 시험 점수
scores = np.random.randint(50, 100, 100)

plt.hist(scores, bins=10, edgecolor='black', color='skyblue')
plt.xlabel('점수')
plt.ylabel('학생 수')
plt.title('시험 점수 분포')
plt.axvline(scores.mean(), color='red', linestyle='--',
            label=f'평균: {scores.mean():.1f}')
plt.legend()
plt.show()

print(f"평균: {scores.mean():.1f}")
print(f"표준편차: {scores.std():.1f}")
print(f"중앙값: {np.median(scores):.1f}")