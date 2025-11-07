## 조건 필터링 ⭐ 매우 중요

```python
# 나이가 30 이상인 사람
print(df[df['age'] >= 30])

# 서울에 사는 사람
print(df[df['city'] == 'Seoul'])

# 여러 조건 (and)
print(df[(df['age'] >= 30) & (df['city'] == 'Seoul')])

# 여러 조건 (or)
print(df[(df['city'] == 'Seoul') | (df['city'] == 'Busan')])

# in 조건
cities = ['Seoul', 'Busan']
print(df[df['city'].isin(cities)])
```

**주의:** `and`, `or` 말고 `&`, `|` 사용!