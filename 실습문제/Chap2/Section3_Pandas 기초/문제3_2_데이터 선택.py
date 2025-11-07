import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. name 열
print(df['name'])

# 2. name과 salary
print(df[['name', 'salary']])

# 3. 2번째 행
print(df.iloc[2])

# 4. 0~2행의 name과 age
print(df.loc[0:2, ['name', 'age']])