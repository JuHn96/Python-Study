import numpy as np

# 정수 배열
int_arr = np.array([1, 2, 3, 4, 5])
print(f"원본 타입: {int_arr.dtype}")
print(f"값: {int_arr}")

# 실수로 변환
float_arr = int_arr.astype(np.float64) # .astype(np.float64): float64로 변환
print(f"실수 타입: {float_arr.dtype}")
print(f"값: {float_arr}")

# 불리언으로 변환
bool_arr = int_arr.astype(bool) #0이 아닌 모든 값은 참
print(f"불리언: {bool_arr}")

# 문자열로
str_arr = int_arr.astype(str)
print(f"문자열: {str_arr}, 타입: {str_arr.dtype}")