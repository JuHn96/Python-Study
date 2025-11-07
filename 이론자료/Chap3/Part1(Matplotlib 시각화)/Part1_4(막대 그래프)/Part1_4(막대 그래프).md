## 막대 그래프 (Bar Plot)

범주형 데이터를 비교할 때 사용합니다.

```python
# 데이터
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

plt.bar(categories, values)
plt.xlabel('카테고리')
plt.ylabel('값')
plt.title('카테고리별 비교')
plt.show()
```

### 가로 막대 그래프

```python
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]
plt.barh(categories, values)
plt.xlabel('값')
plt.ylabel('카테고리')
plt.title('가로 막대 그래프')
plt.show()
```

### 여러 막대 비교

```python
import matplotlib.pyplot as plt
import numpy as np # numpy 임포트 추가

categories = ['A', 'B', 'C', 'D']
values1 = [20, 35, 30, 35]
values2 = [25, 32, 34, 20]

# numpy의 arange 메소드를 사용하여 x축 위치 배열 생성
x = np.arange(len(categories))
width = 0.35

# matplotlib의 bar 메소드를 사용하여 막대 그래프 그리기 (그룹 1)
plt.bar(x - width/2, values1, width, label='그룹1')
# matplotlib의 bar 메소드를 사용하여 막대 그래프 그리기 (그룹 2)
plt.bar(x + width/2, values2, width, label='그룹2')

# matplotlib의 xlabel 메소드를 사용하여 x축 레이블 설정
plt.xlabel('카테고리')
# matplotlib의 ylabel 메소드를 사용하여 y축 레이블 설정
plt.ylabel('값')
# matplotlib의 title 메소드를 사용하여 그래프 제목 설정
plt.title('그룹별 비교')
# matplotlib의 xticks 메소드를 사용하여 x축 눈금을 카테고리 이름으로 설정
plt.xticks(x, categories)
# matplotlib의 legend 메소드를 사용하여 범례 표시
plt.legend()

# matplotlib의 show 메소드를 사용하여 그래프 표시
plt.show()
```