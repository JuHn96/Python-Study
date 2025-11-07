import pandas as pd

students = {
    'student_id': [1, 2, 3, 4, 5],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
    'math': [85, 92, 78, 88, 95],
    'english': [90, 88, 95, 85, 92],
    'science': [88, 90, 82, 92, 98]
}
df = pd.DataFrame(students)

# 1. CSV 저장
df.to_csv('students.csv', index=False)

# 2. 읽기
df_loaded = pd.read_csv('students.csv')

# 3. 처음 3개
print(df_loaded.head(3))