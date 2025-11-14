import matplotlib.pyplot as plt
import numpy as np

# 분기별 제품 판매량
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
product_a = [120, 145, 160, 175]
product_b = [135, 128, 155, 168]
product_c = [110, 122, 138, 152]

x = np.arange(len(quarters))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
# fig: 전체 그림판 (Figure)
# ax: 그림을 그리는 영역 (Axes)
# 여러 개의 서브플롯을 만들 때 특히 유용
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1행 2열
# ax1.plot([1, 2, 3])
# ax2.bar([1, 2, 3], [4, 5, 6])

ax.bar(x - width, product_a, width, label='제품 A', color='#FF6B6B')
ax.bar(x, product_b, width, label='제품 B', color='#4ECDC4')
ax.bar(x + width, product_c, width, label='제품 C', color='#45B7D1')

ax.set_xlabel('분기')
ax.set_ylabel('판매량')
ax.set_title('분기별 제품 판매량 비교')
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.legend()
ax.grid(axis='y', alpha=0.3)
plt.show()

# 분기별 총 판매량
total_sales = [a+b+c for a,b,c in zip(product_a, product_b, product_c)]
print("\n분기별 총 판매량:", total_sales)
print(f"최고 실적 분기: {quarters[np.argmax(total_sales)]}")