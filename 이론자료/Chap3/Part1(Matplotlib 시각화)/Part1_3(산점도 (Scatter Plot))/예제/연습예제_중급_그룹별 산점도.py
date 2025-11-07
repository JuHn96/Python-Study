import matplotlib.pyplot as plt
import numpy as np

# 성별에 따른 키-몸무게 분포
male_height = [170, 175, 180, 173, 178, 183, 176, 181]
male_weight = [65, 70, 75, 68, 73, 78, 71, 76]
female_height = [130, 165, 162, 168, 163, 166, 161, 164]
female_weight = [50, 55, 52, 58, 53, 56, 51, 54]

plt.figure(figsize=(10, 6))
plt.scatter(male_height, male_weight, c='blue', marker='o',
            s=100, alpha=0.6, label='남성')
plt.scatter(female_height, female_weight, c='red', marker='s',
            s=100, alpha=0.6, label='여성')
            
plt.xlabel('키 (cm)')
plt.ylabel('몸무게 (kg)')
plt.title('성별 키-몸무게 분포')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 그룹별 평균
print(f"남성 평균: 키 {np.mean(male_height):.1f}cm, 몸무게 {np.mean(male_weight):.1f}kg")
print(f"여성 평균: 키 {np.mean(female_height):.1f}cm, 몸무게 {np.mean(female_weight):.1f}kg")