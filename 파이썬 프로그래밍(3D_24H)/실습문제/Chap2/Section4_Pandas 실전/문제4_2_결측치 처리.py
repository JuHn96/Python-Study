import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, None, 35, 28, None],
    'salary': [3000, 3500, None, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. 결측치 확인
print(df.isnull())

# 2. 각 열의 결측치 개수
print(df.isnull().sum())

# 3. age 평균으로 채우기
df['age'].fillna(df['age'].mean(), inplace=True)

# 4. salary 0으로 채우기
df['salary'].fillna(0, inplace=True)
print(df)