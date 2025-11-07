## 데이터 변경

### 열 추가

```python
# 새 열 추가
df['bonus'] = df['age'] * 100

# 조건부로 추가
df['grade'] = df['age'].apply(lambda x: 'Senior' if x >= 30 else 'Junior')

print(df)
```

### 열 삭제

```python
# 열 삭제
df_dropped = df.drop('bonus', axis=1)

# 여러 열 삭제
df_dropped = df.drop(['bonus', 'grade'], axis=1)

# 원본 수정
df.drop('bonus', axis=1, inplace=True)
```

### 행 삭제

```python
# 인덱스로 삭제
df_dropped = df.drop(0)  # 0번 행 삭제

# 여러 행 삭제
df_dropped = df.drop([0, 1, 2])
```
