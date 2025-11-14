import matplotlib.pyplot as plt

# 두 제품의 월별 판매량
months = range(1, 13)
product_a = [120, 135, 140, 155, 165, 180, 190, 185, 195, 205, 210, 220]
product_b = [100, 110, 125, 140, 150, 165, 170, 180, 175, 185, 190, 200]

plt.figure(figsize=(10, 6)) # 그래프의 전체 크기(가로 × 세로)인치
plt.plot(months, product_a, marker='o', label='제품 A', linewidth=2)
plt.plot(months, product_b, marker='s', label='제품 B', linewidth=2)
# 기본 색상 팔레트(color cycle) 적용, 첫번째 Plot 파란색, 두번째 주황색, 세번째 초록색, 네번째 빨간색
# 직접 색상 지정
# plt.plot(months, product_a, marker='o', label='제품 A', linewidth=2, color='red')
plt.xlabel('월')
plt.ylabel('판매량')
plt.title('제품별 월간 판매량 추이')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(months)
plt.show()

# 격차 분석
gap = [a - b for a, b in zip(product_a, product_b)]
avg_gap = sum(gap) / len(gap)
print(f"평균 판매 격차: {avg_gap:.1f}개")