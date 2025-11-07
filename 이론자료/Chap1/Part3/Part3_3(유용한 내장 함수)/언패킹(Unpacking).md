# 언패킹(Unpacking) 연산자 *

## 역할 1: 펼치기 (Unpacking)
```py
리스트나 튜플을 개별 요소로 펼쳐줌
numbers = [1, 2, 3]

# 일반 출력
print(numbers)    # [1, 2, 3]

# 언패킹 출력
print(*numbers)   # 1 2 3 (개별 요소로 펼쳐짐)
```

### 함수 인자로 전달
```py
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

# 방법 1: 하나씩 전달
result = add(numbers[0], numbers[1], numbers[2])

# 방법 2: 언패킹 (훨씬 간단!)
result = add(*numbers)  # add(1, 2, 3)과 동일
print(result)  # 6
```

## 역할 2: 나머지 모으기 (Packing)
일부를 제외한 나머지를 리스트로 모음

### 기본 패킹
```py
a, *rest = [1, 2, 3, 4, 5]
print(a)     # 1
print(rest)  # [2, 3, 4, 5]
```

### 중간에 패킹
```py
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### 앞에서 패킹
```py
*start, last = [1, 2, 3, 4, 5]
print(start)  # [1, 2, 3, 4]
print(last)   # 5
```