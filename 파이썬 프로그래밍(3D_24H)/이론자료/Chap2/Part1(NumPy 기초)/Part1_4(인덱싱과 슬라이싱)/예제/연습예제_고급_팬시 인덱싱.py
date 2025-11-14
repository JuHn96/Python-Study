import numpy as np

arr = np.arange(0, 100, 10)
print("배열:", arr)

# 특정 인덱스들만 선택
indices = [1, 3, 5, 7]
selected = arr[indices]
print("선택:", selected)

# 2차원에서 특정 좌표들 선택
arr_2d = np.arange(1, 26).reshape(5, 5)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]]
'''
rows = [0, 1, 2]
cols = [0, 2, 4]
values = arr_2d[rows, cols]
print("\n대각선 값:", values)

# 조건부 인덱싱 (불리언 마스크)
arr = np.random.randint(1, 100, 20)
print("\n원본:", arr)
print("50 이상:", arr[arr >= 50])
print("짝수:", arr[arr % 2 == 0])
print("30~70:", arr[(arr >= 30) & (arr <= 70)])