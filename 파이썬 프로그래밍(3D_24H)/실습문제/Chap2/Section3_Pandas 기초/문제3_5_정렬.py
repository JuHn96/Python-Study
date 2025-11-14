import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. 나이 오름차순
print(df.sort_values('age'))

# 2. 연봉 내림차순
print(df.sort_values('salary', ascending=False))

# 3. 도시, 나이
print(df.sort_values(['city', 'age']))