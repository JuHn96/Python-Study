## 결측치 처리 ⭐ 중요

### 결측치 확인

```python
# 결측치 있는지 확인
print(df.isnull())

# 결측치 개수
print(df.isnull().sum())

# 결측치가 있는 행
print(df[df.isnull().any(axis=1)])
```

### 결측치 처리

```python
# 결측치가 있는 행 제거
df_dropped = df.dropna()

# 결측치를 특정 값으로 채우기
df_filled = df.fillna(0)

# 열별로 다르게 채우기
df_filled = df.fillna({'age': 0, 'city': 'Unknown'})

# 평균으로 채우기
df['age'].fillna(df['age'].mean(), inplace=True)
```

**inplace=True:** 원본 수정