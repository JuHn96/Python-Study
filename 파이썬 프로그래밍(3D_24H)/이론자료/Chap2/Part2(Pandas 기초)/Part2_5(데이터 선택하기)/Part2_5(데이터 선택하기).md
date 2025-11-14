# 데이터 선택하기

### 열 선택

```python

df = pd.read_csv('sample.csv')
print(df)
# 한 개 열
print(df['name'])

# 여러 열
print(df[['name', 'age']])

# 새로운 열 추가
df['score1'] = [85, 92, 78, 88]
print(df)
```

### 행 선택

```python
# 처음 3개 행
print(df[:3])

# 특정 범위
print(df[1:4])
```

### loc와 iloc ⭐ 중요

```python
# loc: 이름으로 선택
print(df.loc[0])           # 0번 행
print(df.loc[0, 'name'])   # 0번 행의 name
print(df.loc[0:2, ['name', 'age']])  # 0~2행, name과 age열

# iloc: 위치(인덱스)로 선택
print(df.iloc[0])          # 0번 행
print(df.iloc[0, 1])       # 0행 1열
print(df.iloc[0:3, 0:2])   # 0~2행, 0~1열
```

**차이점:** ⭐
- `loc`: 라벨(이름) 기반, 끝 포함
- `iloc`: 정수 위치 기반, 끝 미포함