## 집계 함수

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(np.sum(arr))      # 55 (합계)
print(np.mean(arr))     # 5.5 (평균)
print(np.max(arr))      # 10 (최대)
print(np.min(arr))      # 1 (최소)
print(np.std(arr))      # 2.87... (표준편차)

# 메서드로도 가능
print(arr.sum())
print(arr.mean())
print(arr.max())
```

### 축(axis) 기준 연산 ⭐ 중요

```python
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
                   
# axis=0: 세로 방향 (열 기준)
print(arr_2d.sum(axis=0))  # [12 15 18]

# axis=1: 가로 방향 (행 기준)
print(arr_2d.sum(axis=1))  # [6 15 24]

# axis 없으면 전체
print(arr_2d.sum())  # 45
```

**주요 집계 함수**

```python
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
```

**기본 통계 함수**

```python
arr_2d.sum(axis=0)    # [5 7 9] - 열 합계
arr_2d.mean(axis=0)   # [2.5 3.5 4.5] - 열 평균
arr_2d.std(axis=0)    # [1.5 1.5 1.5] - 열 표준편차
arr_2d.var(axis=0)    # [2.25 2.25 2.25] - 열 분산
arr_2d.min(axis=0)    # [1 2 3] - 열 최솟값
arr_2d.max(axis=0)    # [4 5 6] - 열 최댓값
```

**순위/정렬 관련**

```python
arr_2d.argmin(axis=0) # [0 0 0] - 최솟값의 인덱스
arr_2d.argmax(axis=0) # [1 1 1] - 최댓값의 인덱스
arr_2d.sort(axis=0)   # 각 열을 정렬
```

**누적 함수**

```python
arr_2d.cumsum(axis=0) # [[1 2 3]    - 누적 합
                      #  [5 7 9]]
arr_2d.cumprod(axis=0) # [[1  2  3]  - 누적 곱
                       #  [4 10 18]]
```

**기타 유용한 함수**

```python
arr_2d.prod(axis=0)   # [4 10 18] - 열 곱
arr_2d.median(axis=0) # [2.5 3.5 4.5] - 열 중앙값 (np.median 사용)
arr_2d.any(axis=0)    # [True True True] - 하나라도 True인지
arr_2d.all(axis=0)    # [True True True] - 모두 True인지
```

- **다른 함수도 가능**

```python
arr_2d.sum(axis=0)    # [5 7 9] - 열 합계
arr_2d.mean(axis=0)   # [2.5 3.5 4.5] - 열 평균
arr_2d.std(axis=0)    # [1.5 1.5 1.5] - 열 표준편차
arr_2d.var(axis=0)    # [2.25 2.25 2.25] - 열 분산
arr_2d.min(axis=0)    # [1 2 3] - 열 최솟값
arr_2d.max(axis=0)    # [4 5 6] - 열 최댓값
```

## 기억하기:
- `axis=0`: 세로로 내려가며 계산 (열별 합)
- `axis=1`: 가로로 가며 계산 (행별 합)