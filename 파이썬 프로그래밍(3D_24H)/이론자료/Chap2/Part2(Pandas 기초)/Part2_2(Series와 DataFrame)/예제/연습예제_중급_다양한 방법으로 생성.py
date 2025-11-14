# 1. 리스트의 리스트
data1 = [
    ['Kim', 25, 'Seoul'],
    ['Lee', 30, 'Busan'],
    ['Park', 35, 'Seoul']
]

df1 = pd.DataFrame(data1, columns=['name', 'age', 'city'])
print("리스트로:\n", df1)

# 2. 딕셔너리의 리스트
data2 = [
    {'name': 'Kim', 'age': 25, 'city': 'Seoul'},
    {'name': 'Lee', 'age': 30, 'city': 'Busan'},
    {'name': 'Park', 'age': 35, 'city': 'Seoul'}
]
df2 = pd.DataFrame(data2)
print("\n딕셔너리 리스트로:\n", df2)

# 3. NumPy 배열
import numpy as np
data3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df3 = pd.DataFrame(data3, columns=['A', 'B', 'C'])
print("\nNumPy로:\n", df3)