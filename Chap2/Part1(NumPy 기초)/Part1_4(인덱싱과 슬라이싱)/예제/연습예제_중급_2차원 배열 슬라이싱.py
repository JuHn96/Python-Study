import numpy as np

# 5x5 배열 생성
arr = np.arange(1, 26).reshape(5, 5)
print("전체:\n", arr)

# 다양한 슬라이싱
print("\n첫 2행:", arr[:2])
print("\n마지막 2열:\n", arr[:, -2:])
print("\n중앙 3x3:\n", arr[1:4, 1:4])
print("\n대각선:", np.diag(arr))
print("\n역대각선:", np.diag(np.fliplr(arr)))

# 테두리 추출
border = np.concatenate([
    arr[0, :],      # 첫 행    
    arr[-1, :],     # 마지막 행    
    arr[1:-1, 0],   # 첫 열 (모서리 제외)    
    arr[1:-1, -1]   # 마지막 열 (모서리 제외)]
    ])
print("\n테두리:", border)