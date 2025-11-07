## 집계와 그룹화

### 기본 집계

```python
print(df['age'].sum())    # 합계
print(df['age'].mean())   # 평균
print(df['age'].max())    # 최대
print(df['age'].min())    # 최소
print(df['age'].count())  # 개수
```

### 그룹화 ⭐

```python
# 도시별 평균 나이
grouped = df.groupby('city')['age'].mean()
print(grouped)

# 도시별 여러 통계
grouped = df.groupby('city')['age'].agg(['mean', 'max', 'min'])
print(grouped)

# 도시별 개수
print(df['city'].value_counts())
```