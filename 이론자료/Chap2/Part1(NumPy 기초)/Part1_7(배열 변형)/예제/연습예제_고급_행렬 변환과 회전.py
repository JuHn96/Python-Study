import numpy as np

# 4x4 배열
matrix = np.arange(1, 17).reshape(4, 4)
print("원본:\n", matrix)

# 90도 회전 (시계 반대방향)
rot90 = np.rot90(matrix)
print("\n90도 회전:\n", rot90)

# 180도 회전
rot180 = np.rot90(matrix, 2)
print("\n180도 회전:\n", rot180)

# 좌우 반전
fliplr = np.fliplr(matrix)
print("\n좌우 반전:\n", fliplr)

# 상하 반전
flipud = np.flipud(matrix)
print("\n상하 반전:\n", flipud)

# 전치
transpose = matrix.T
print("\n전치:\n", transpose)

# 대각선 추출
main_diag = np.diag(matrix)
anti_diag = np.diag(np.fliplr(matrix))
print(f"\n주 대각선: {main_diag}")
print(f"부 대각선: {anti_diag}")