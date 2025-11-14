## 조건 필터링

```python
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 5보다 큰 값만
print(arr[arr > 5])  # [6 7 8 9 10]

# 짝수만
print(arr[arr % 2 == 0])  # [2 4 6 8 10]

# 여러 조건
print(arr[(arr > 3) & (arr < 8)])  # [4 5 6 7]
```

**주의:** `and` 말고 `&` 사용!