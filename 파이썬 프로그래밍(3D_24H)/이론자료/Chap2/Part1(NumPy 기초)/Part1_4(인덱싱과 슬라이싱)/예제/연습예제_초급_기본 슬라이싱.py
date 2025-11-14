import numpy as np

arr = np.arange(1, 21)  # 1~20

print("원본:", arr)
print("앞 5개:", arr[:5])
print("뒤 5개:", arr[-5:])
print("중간 10개:", arr[5:15])
print("홀수 인덱스:", arr[1::2])
print("역순:", arr[::-1])