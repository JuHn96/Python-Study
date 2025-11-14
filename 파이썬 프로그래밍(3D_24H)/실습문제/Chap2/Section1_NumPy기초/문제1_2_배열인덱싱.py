import numpy as np

# 아래 배열에서 조건에 맞는 값 출력시키기
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 첫 번째 행 출력
print(arr[0])

# 마지막 열 출력
print(arr[:, -1])
# print(arr[:, 3]) # 같은 값 출력

# 7이라는 값 출력
print(arr[1, 2])

# 2행 2열부터 3행 3열까지 출력
print(arr[1:3, 1:3])