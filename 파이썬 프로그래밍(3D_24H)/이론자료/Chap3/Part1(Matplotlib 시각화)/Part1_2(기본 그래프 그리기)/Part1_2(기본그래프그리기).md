## 기본 그래프 그리기

### 선 그래프 (Line Plot)

```python
import matplotlib.pyplot as plt

# 데이터
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 그래프 그리기
plt.plot(x, y)
plt.show()
```

### 그래프 꾸미기

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X축 이름')        # x축 레이블
plt.ylabel('Y축 이름')        # y축 레이블
plt.title('그래프 제목')       # 제목
plt.grid(True)               # 격자 표시
plt.show()
```

### 여러 선 그리기

```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label='제곱')
plt.plot(x, y2, label='선형')
plt.xlabel('x')
plt.ylabel('y')
plt.title('두 함수 비교')
plt.legend()  # 그래프에 범례(legend)를 표시

plt.show()
```

### 선 스타일과 색상

```python
x = range(10)
y = [i**2 for i in x]

# 색상: 'r'(red), 'g'(green), 'b'(blue), 'k'(black)
# 스타일: '-'(실선), '--'(점선), ':'(점), '-.'(일점쇄선)
# 마커: 'o'(원), 's'(사각형), '^'(삼각형), '*'(별)
plt.plot(x, y, 'ro-', label='빨간 원')  # 빨간색 원 마커
plt.plot(x, [i*10 for i in x], 'bs--', label='파란 사각형')  # 파란색 사각형 점선
plt.legend()
plt.show()
```