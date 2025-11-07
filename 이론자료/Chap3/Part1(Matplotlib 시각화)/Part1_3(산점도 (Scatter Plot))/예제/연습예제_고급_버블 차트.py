import matplotlib.pyplot as plt
import numpy as np

# 도시별 인구, GDP, 면적
cities = ['서울', '부산', '대구', '인천', '광주', '대전', '울산']
population = [9.7, 3.4, 2.4, 2.9, 1.5, 1.5, 1.1]  # 백만명
gdp = [400, 95, 52, 85, 35, 38, 72]  # 조원
area = [605, 770, 884, 1063, 501, 540, 1061]  # km²

# 버블 크기는 면적에 비례하도록 설정 (너무 크지 않게 적절히 조절)
sizes = [a/2 for a in area]
plt.figure(figsize=(12, 8))
# 산점도 그래프 생성 (버블 차트)
# population: x축 데이터 (인구)
# gdp: y축 데이터 (GDP)
# s=sizes: 버블의 크기 (면적에 비례)
# alpha=0.6: 버블의 투명도
# c=range(len(cities)): 버블 색상 (도시별로 다르게)
# cmap='viridis': 사용할 색상 맵
scatter = plt.scatter(population, gdp, s=sizes, alpha=0.6,
                     c=range(len(cities)), cmap='viridis')

# 각 버블에 도시 이름 표시
for i, city in enumerate(cities):
    # annotate(텍스트, (x좌표, y좌표))
    plt.annotate(city, (population[i], gdp[i]),
                fontsize=10, ha='center') # ha='center': 텍스트 정렬 (가운데)

plt.xlabel('인구 (백만명)') # x축 레이블 설정
plt.ylabel('GDP (조원)') # y축 레이블 설정
plt.title('도시별 인구-GDP-면적 비교\n(버블 크기 = 면적)') # 그래프 제목 설정 (\n으로 줄바꿈)
plt.colorbar(scatter, label='도시 순서') # 색상 바 (컬러맵 설명) 추가
plt.grid(True, alpha=0.3) # 격자 표시 (투명도 설정)
plt.show() # 그래프 표시

# 1인당 GDP 계산
gdp_per_capita = [g/p for g, p in zip(gdp, population)]
print("\n1인당 GDP (억원):")
for city, gpc in zip(cities, gdp_per_capita):
    print(f"{city}: {gpc:.1f}")