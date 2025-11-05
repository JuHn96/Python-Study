import numpy as np

# 다양한 타입의 메모리 사용량 비교
size = 1000000

# 배열 생성 시 데이터 타입 지정
int64_arr = np.arange(size, dtype=np.int64)
int32_arr = np.arange(size, dtype=np.int32)
int16_arr = np.arange(size, dtype=np.int16)
int8_arr = np.arange(size, dtype=np.int8)

print(f"int64: {int64_arr.nbytes / 1024 / 1024:.2f} MB")
print(f"int32: {int32_arr.nbytes / 1024 / 1024:.2f} MB")
print(f"int16: {int16_arr.nbytes / 1024 / 1024:.2f} MB")
print(f"int8: {int8_arr.nbytes / 1024 / 1024:.2f} MB")

# 조건에 따라 적절한 타입 선택
data = np.array([1, 2, 3, 255])

if data.max() < 256:
    optimized = data.astype(np.uint8)  # 0~255    
    print(f"최적화: {optimized.dtype}")