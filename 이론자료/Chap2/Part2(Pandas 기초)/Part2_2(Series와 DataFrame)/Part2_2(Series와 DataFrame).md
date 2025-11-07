# Series와 DataFrame

### Series - 1차원 데이터

```py
import pandas as pd

# 리스트에서 Series 만들기
s = pd.Series([10, 20, 30, 40, 50])
print(s)
```

```
출력:
0    10
1    20
2    30
3    40
4    50
dtype: int64

```

```
# 인덱스 지정
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
print(s['b'])  # 20
```

### DataFrame - 2차원 데이터 (표) ⭐ 가장 많이 사용
```py
# 딕셔너리에서 만들기
data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi'],
    'age': [25, 30, 35, 28],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu']
}

df = pd.DataFrame(data)
print(df)
```
```
출력:
   name  age   city
0   Kim   25  Seoul
1   Lee   30  Busan
2  Park   35  Seoul
3  Choi   28  Daegu
```