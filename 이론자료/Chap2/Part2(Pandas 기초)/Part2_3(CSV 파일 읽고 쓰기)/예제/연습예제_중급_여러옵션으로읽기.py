import pandas as pd

# 샘플 CSV 생성,CSV 형식의 멀티라인 문자열(Multi-line String) 데이터
data = """id,name,age,score
1,Kim,25,85
2,Lee,30,92
3,Park,35,78
4,Choi,28,90"""

with open('sample.csv', 'w') as f:
    f.write(data)
    
# 기본 읽기
df1 = pd.read_csv('sample.csv')
print("기본:\n", df1)

# 특정 열만 읽기
df2 = pd.read_csv('sample.csv', usecols=['name', 'score'])
print("\n특정 열만:\n", df2)

# 인덱스 열 지정
df3 = pd.read_csv('sample.csv', index_col='id')
print("\nid를 인덱스로:\n", df3)

# 조건부 읽기 (nrows)
df4 = pd.read_csv('sample.csv', nrows=2)
print("\n처음 2개만:\n", df4)