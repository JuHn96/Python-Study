import matplotlib.pyplot as plt
import numpy as np

# 두 반의 점수 비교
class_a = np.random.normal(75, 10, 100)  # 평균 75, 표준편차 10
class_b = np.random.normal(70, 15, 100)  # 평균 70, 표준편차 15

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(class_a, bins=20, alpha=0.7, label='A반', color='blue')
# bins=50이면 데이터 범위를 50개의 구간으로 나눔
plt.hist(class_b, bins=20, alpha=0.7, label='B반', color='red')
plt.xlabel('점수')
plt.ylabel('학생 수')
plt.title('두 반의 점수 분포 비교')
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(class_a, bins=20, alpha=0.5, label='A반',
         color='blue', density=True)
plt.hist(class_b, bins=20, alpha=0.5, label='B반',
         color='red', density=True)
plt.xlabel('점수')
plt.ylabel('확률 밀도')
plt.title('정규화된 분포')
plt.legend()

plt.tight_layout()
plt.show()

print(f"A반 - 평균: {class_a.mean():.1f}, 표준편차: {class_a.std():.1f}")
print(f"B반 - 평균: {class_b.mean():.1f}, 표준편차: {class_b.std():.1f}")