# 정렬

```py
# 나이 기준 오름차순
df_sorted = df.sort_values('age')
print(df_sorted)
# 내림차순
df_sorted = df.sort_values('age', ascending=False)
print(df_sorted)
# 여러 열 기준
df_sorted = df.sort_values(['score', 'age'])
```