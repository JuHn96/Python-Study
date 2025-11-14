# 데이터 확인하기

**설명보다는 아래 코드를 실행시켜보면서 눈으로 확인하는 파트 그래서 예제X**
> large_file.csv는 이전 2_3 예제에서 만들어짐


```py
df = pd.read_csv('large_file.csv')

# 처음 5개 행
print(df.head())

# 처음 10개 행
print(df.head(10))

# 마지막 5개 행
print(df.tail())

# 데이터 정보
print(df.info())

# 통계 요약
print(df.describe())

# 크기 확인
print(df.shape)  # (행, 열)

# 열 이름
print(df.columns)

# 데이터 타입
print(df.dtypes)
```