import numpy as np
# 슬라이싱 기본 문법
# 배열[start:stop:step]

# 체스판 패턴 (8x8)
chess = np.zeros((8, 8))
chess[::2, 1::2] = 1  # 짝수 행, 홀수 열
chess[1::2, ::2] = 1  # 홀수 행, 짝수 열
print("체스판:\n", chess)

# 대각선 배열
diag = np.diag([1, 2, 3, 4, 5])
print("대각 행렬:\n", diag)

# 랜덤 정수 배열 (1~100)
random_int = np.random.randint(1, 101, size=(5, 5))
print("랜덤 배열:\n", random_int)
'''
np.random.randint(low, high, size)

각 파라미터 설명
low=1: 최솟값 (포함)
생성될 난수의 최소 범위

high=101: 최댓값 (제외!)
생성될 난수의 최대 범위

⚠️ 주의: 101은 포함 안 됨 (1~100만 나옴)

size=(5, 5): 배열 크기

5×5 2차원 배열 생성
(3,) → 1차원 3개
(2, 3, 4) → 3차원 배열도 가능
'''