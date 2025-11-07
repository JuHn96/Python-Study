import matplotlib.pyplot as plt
import numpy as np

# 2D 히스토그램 (키와 몸무게의 분포)
np.random.seed(42)
height = np.random.normal(170, 10, 1000)
weight = height * 0.5 + np.random.normal(20, 5, 1000)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. 산점도
axes[0, 0].scatter(height, weight, alpha=0.3)
axes[0, 0].set_xlabel('키 (cm)')
axes[0, 0].set_ylabel('몸무게 (kg)')
axes[0, 0].set_title('산점도')

# 2. 2D 히스토그램
axes[0, 1].hist2d(height, weight, bins=30, cmap='YlOrRd')
axes[0, 1].set_xlabel('키 (cm)')
axes[0, 1].set_ylabel('몸무게 (kg)')
axes[0, 1].set_title('2D 히스토그램')

# 3. 키 분포
axes[1, 0].hist(height, bins=30, edgecolor='black', color='skyblue')
axes[1, 0].set_xlabel('키 (cm)')
axes[1, 0].set_ylabel('빈도')
axes[1, 0].set_title('키 분포')
axes[1, 0].axvline(height.mean(), color='red', linestyle='--')

# 4. 몸무게 분포
axes[1, 1].hist(weight, bins=30, edgecolor='black', color='lightcoral')
axes[1, 1].set_xlabel('몸무게 (kg)')
axes[1, 1].set_ylabel('빈도')
axes[1, 1].set_title('몸무게 분포')
axes[1, 1].axvline(weight.mean(), color='red', linestyle='--')

plt.tight_layout()
plt.show()

# 상관관계
correlation = np.corrcoef(height, weight)[0, 1]
print(f"키-몸무게 상관계수: {correlation:.3f}")