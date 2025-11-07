import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}

df = pd.DataFrame(data)

# 1. bonus
df['bonus'] = df['salary'] * 0.1

# 2. total
df['total'] = df['salary'] + df['bonus']

# 3. age_group
df['age_group'] = df['age'].apply(lambda x: 'Senior' if x >= 30 else 'Junior')

print(df)