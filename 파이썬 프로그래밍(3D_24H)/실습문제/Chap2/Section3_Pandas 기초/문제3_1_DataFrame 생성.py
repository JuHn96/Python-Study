import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'age': [25, 30, 35, 28, 32],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Seoul'],
    'salary': [3000, 3500, 4000, 3200, 3800]
}
df = pd.DataFrame(data)
print(df.head(3))
print(df.info())
print(df.describe())