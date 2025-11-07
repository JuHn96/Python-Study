# 기본 DataFrame 생성

import pandas as pd
# 학생 명단
students = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수'],
    'age': [20, 21, 22],
    'grade': ['A', 'B', 'A']
})

print(students)
print("\n컬럼:", students.columns.tolist())
print("인덱스:", students.index.tolist())
print("크기:", students.shape)