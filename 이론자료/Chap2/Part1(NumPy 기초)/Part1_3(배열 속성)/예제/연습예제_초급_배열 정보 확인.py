import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
                
print(f"모양: {arr.shape}")
print(f"차원: {arr.ndim}")
print(f"크기: {arr.size}")
print(f"타입: {arr.dtype}")
print(f"바이트 크기: {arr.nbytes}bytes")