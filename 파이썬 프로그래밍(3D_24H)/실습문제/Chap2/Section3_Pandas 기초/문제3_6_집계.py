import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. 평균 나이
print(df['age'].mean())

# 2. 평균 연봉
print(df['salary'].mean())

# 3. 도시별 평균 연봉
print(df.groupby('city')['salary'].mean())

# 4. 도시별 인원
print(df['city'].value_counts())