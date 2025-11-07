import matplotlib.pyplot as plt

# 키와 몸무게 관계
height = [160, 165, 170, 175, 180, 162, 168, 173, 178, 183]
weight = [50, 55, 60, 70, 75, 52, 58, 68, 73, 78]

plt.scatter(height, weight)
plt.xlabel('키 (cm)')
plt.ylabel('몸무게 (kg)')
plt.title('키와 몸무게의 관계')
plt.grid(True, alpha=0.3)
plt.show()