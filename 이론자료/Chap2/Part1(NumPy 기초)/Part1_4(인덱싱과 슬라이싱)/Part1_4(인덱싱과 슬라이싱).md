### 1차원 배열
**출력: 각 코드 행의 주석 참고**
```python
# arr[start:stop:step]

arr = np.array([10, 20, 30, 40, 50])

# arr[index]
print(arr[0])      # 10 (첫 번째)

# arr[negative_index]
print(arr[-1])     # 50 (마지막)

# arr[start:stop]
print(arr[1:4])    # [20 30 40], **인덱스 1, 2, 3 (4는 제외!)**

# arr[start:stop:step]
print(arr[::2])    # [10 30 50] (2칸씩)
```

### 2차원 배열

```python
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
                   
# 특정 요소 접근 [행, 열]
print(arr_2d[0, 0])     # 1
print(arr_2d[1, 2])     # 7
print(arr_2d[-1, -1])   # 12

# 행 전체 선택
print(arr_2d[0])        # [1 2 3 4]
print(arr_2d[0, :])     # 위와 동일

# 열 전체 선택
print(arr_2d[:, 0])     # [1 5 9] (첫 번째 열)
print(arr_2d[:, 1])     # [2 6 10] (두 번째 열)

# 부분 선택
print(arr_2d[0:2, 1:3])  # 0~1행, 1~2열
```

**출력:**

```
1
7
12
[1 2 3 4]
[1 2 3 4]
[1 5 9]
[ 2  6 10]
[[2 3]
 [6 7]]
```

**중요 포인트:**
- 리스트는 `arr[0][0]` 이렇게 접근
- NumPy는 `arr[0, 0]` 이렇게 접근 ⭐