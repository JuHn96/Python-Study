import matplotlib.pyplot as plt
import numpy as np

# 월별 비용 구조
months = ['1월', '2월', '3월', '4월', '5월', '6월']
labor_cost = [300, 320, 310, 330, 340, 350]
material_cost = [200, 210, 220, 215, 230, 240]
overhead_cost = [150, 155, 160, 158, 165, 170]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 누적 막대 그래프
ax1.bar(months, labor_cost, label='인건비', color='#FF6B6B')
ax1.bar(months, material_cost, bottom=labor_cost,
        label='재료비', color='#4ECDC4')
bottom = [l+m for l,m in zip(labor_cost, material_cost)]
ax1.bar(months, overhead_cost, bottom=bottom,
        label='관리비', color='#45B7D1')
        
ax1.set_ylabel('비용 (만원)')
ax1.set_title('월별 비용 구조 (누적)')
ax1.legend()
ax1.grid(axis='y', alpha=0.3)

# 비율 그래프
total_costs = [l+m+o for l,m,o in zip(labor_cost, material_cost, overhead_cost)]
labor_ratio = [l/t*100 for l,t in zip(labor_cost, total_costs)]
material_ratio = [m/t*100 for m,t in zip(material_cost, total_costs)]
overhead_ratio = [o/t*100 for o,t in zip(overhead_cost, total_costs)]

ax2.bar(months, labor_ratio, label='인건비 %', color='#FF6B6B')
ax2.bar(months, material_ratio, bottom=labor_ratio,
        label='재료비 %', color='#4ECDC4')
bottom2 = [l+m for l,m in zip(labor_ratio, material_ratio)]
ax2.bar(months, overhead_ratio, bottom=bottom2,
        label='관리비 %', color='#45B7D1')
        
ax2.set_ylabel('비율 (%)')
ax2.set_title('월별 비용 구조 (비율)')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

print(f"월평균 총비용: {np.mean(total_costs):.0f}만원")
print(f"인건비 평균 비율: {np.mean(labor_ratio):.1f}%")