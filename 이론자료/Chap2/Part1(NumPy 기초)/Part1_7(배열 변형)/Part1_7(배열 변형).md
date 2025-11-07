## reshape - 모양 바꾸기
```py
arr = np.arange(12)  # [0 1 2 ... 11]
print(arr)

# 3행 4열로
arr_2d = arr.reshape(3, 4)
print(arr_2d)

# 2행 6열로
arr_2d = arr.reshape(2, 6)
print(arr_2d)

# -1: 자동 계산
arr_2d = arr.reshape(3, -1)  # 3행, 열은 자동
print(arr_2d)

```


## flatten - 1차원으로
```py
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
flat = arr_2d.flatten()
print(flat)  # [1 2 3 4 5 6]
```

## transpose - 전치 (행과 열 바꾸기)
```py
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.shape)  # (2, 3)

arr_t = arr.T  # 또는 arr.transpose()
print(arr_t)
print(arr_t.shape)  # (3, 2)
```