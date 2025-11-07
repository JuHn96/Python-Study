CSV 읽기

```py
# CSV 파일 읽기
df = pd.read_csv('data.csv')

# 인코딩 지정 (한글 깨질 때)
df = pd.read_csv('data.csv', encoding='utf-8')

# 또는
df = pd.read_csv('data.csv', encoding='cp949')
```

```py
CSV 쓰기
# CSV로 저장
df.to_csv('output.csv', index=False)

# 인덱스 포함
df.to_csv('output.csv')

# 한글 인코딩
df.to_csv('output.csv', encoding='utf-8-sig', index=False)
```