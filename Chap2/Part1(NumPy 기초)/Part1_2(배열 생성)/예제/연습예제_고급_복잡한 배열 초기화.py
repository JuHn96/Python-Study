import numpy as np

# 그리드 생성 (좌표 배열)
x = np.linspace(-5, 5, 11) 
y = np.linspace(-5, 5, 11) 
X, Y = np.meshgrid(x, y) 
# X 행렬: x 배열을 행 방향으로 반복
# Y 행렬: y 배열을 열 방향으로 반복
'''
np.linspace(start, stop, num)
균등하게 나눈 숫자 생성

np.linspace(-5, 5, 11) → -5부터 5까지 11개로 균등 분할
결과: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
'''
'''
X, Y = np.meshgrid(x, y)
1D 배열 2개를 2D 격자로 확장
모든 (x, y) 좌표 조합을 만듦
'''
print("X 좌표:\n", X[:3, :3])  # 일부만 출력
print("Y 좌표:\n", Y[:3, :3])

# 거리 배열 (원점으로부터의 거리)
distance = np.sqrt(X**2 + Y**2)
print("거리:\n", distance[:3, :3])

# 가우시안 분포
mean = 0
std = 1
gaussian = np.random.normal(mean, std, 1000)
print(f"평균: {gaussian.mean():.2f}, 표준편차: {gaussian.std():.2f}")