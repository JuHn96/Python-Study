import matplotlib.pyplot as plt
import numpy as np

# 판매량과 수익률을 함께 표시
months = range(1, 13)
sales = [120, 135, 140, 155, 165, 180, 190, 185, 195, 205, 210, 220]
profit_rate = [12, 13, 14, 15, 14, 15, 16, 15, 17, 16, 18, 19]

fig, ax1 = plt.subplots(figsize=(12, 6)) # Figure(도화지)와 Axes(그래프 틀)를 동시에 반환

# 첫 번째 y축 (판매량)
color = 'tab:blue'
ax1.set_xlabel('월')
ax1.set_ylabel('판매량', color=color)
ax1.plot(months, sales, color=color, marker='o', linewidth=2, label='판매량')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, alpha=0.3)

# 두 번째 y축 (수익률)
ax2 = ax1.twinx() # 오른쪽에 두 번째 y축 생성
color = 'tab:red'
ax2.set_ylabel('수익률 (%)', color=color)
ax2.plot(months, profit_rate, color=color, marker='s', linewidth=2, label='수익률')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('판매량과 수익률 추이')
fig.tight_layout()
plt.show()

# 상관관계 분석
correlation = np.corrcoef(sales, profit_rate)[0, 1]
print(f"판매량-수익률 상관계수: {correlation:.3f}")