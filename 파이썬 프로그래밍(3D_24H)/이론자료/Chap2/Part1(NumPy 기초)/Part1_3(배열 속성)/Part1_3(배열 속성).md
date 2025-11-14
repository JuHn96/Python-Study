## 배열 속성

```py
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
                
print(arr.shape)   # 배열의 형태, 3행 4열
print(arr.ndim)    # 차원 수, 2차원
print(arr.size)    # 총 요소 개수, 12
print(arr.dtype)   # 데이터 타입, int64
```

**출력:**
```
(3, 4)
2
12
int64
```
