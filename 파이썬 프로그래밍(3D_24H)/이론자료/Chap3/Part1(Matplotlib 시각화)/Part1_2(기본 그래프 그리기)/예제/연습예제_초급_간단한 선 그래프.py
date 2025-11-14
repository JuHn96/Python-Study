import matplotlib.pyplot as plt

# 시간에 따른 온도 변화
hours = [0, 3, 6, 9, 12, 15, 18, 21, 24]
temp = [15, 14, 16, 20, 25, 27, 24, 20, 16]

plt.plot(hours, temp, marker='o')
plt.xlabel('시간')
plt.ylabel('온도 (°C)')
plt.title('하루 동안의 온도 변화')
plt.grid(True)
plt.show()