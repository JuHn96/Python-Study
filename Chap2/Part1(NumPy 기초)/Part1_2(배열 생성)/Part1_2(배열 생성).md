## 기본 배열 만들기

```py
import numpy as np

# 리스트에서 배열 만들기
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 2차원 배열
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
print(arr_2d)
```

**출력:**
```
[1 2 3 4 5]
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]]
 ```

## 특수한 배열 만들기

```py
# 0으로 채워진 배열
zeros = np.zeros(5)
print(zeros)  # [0. 0. 0. 0. 0.]

# 1로 채워진 배열
ones = np.ones((3, 4))  # 3행 4열
print(ones)

# 특정 값으로 채우기
full = np.full((2, 3), 7)
print(full)  # 모든 값이 7

# 연속된 숫자 배열
arange = np.arange(0, 10, 2)  # 0부터 10까지 2씩
print(arange)  # [0 2 4 6 8]

# 균등한 간격의 배열
linspace = np.linspace(0, 1, 5)  # 0~1 사이를 5개로
print(linspace)  # [0. 0.25 0.5 0.75 1.]

# 랜덤 배열
random = np.random.rand(3, 3)  # 0~1 사이 랜덤
print(random)
```

**출력:**

```
[0. 0. 0. 0. 0.]

[[1. 1. 1. 1.]
[1. 1. 1. 1.]
[1. 1. 1. 1.]]

[[7 7 7]
[7 7 7]]

[0 2 4 6 8]

[0.   0.25  0.5  0.75  1.  ]

[[0.41777328 0.72716062 0.82196145]
[0.73588731 0.58176431 0.48584637]
[0.16781649 0.34433255 0.09740085]]
```

