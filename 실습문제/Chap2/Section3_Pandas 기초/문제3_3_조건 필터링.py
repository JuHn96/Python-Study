import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. 나이 30 이상
print(df[df['age'] >= 30])

# 2. 서울
print(df[df['city'] == 'Seoul'])

# 3. 연봉 3500 이상 and 서울
print(df[(df['salary'] >= 3500) & (df['city'] == 'Seoul')])

# 4. 서울 or 부산
print(df[df['city'].isin(['Seoul', 'Busan'])])