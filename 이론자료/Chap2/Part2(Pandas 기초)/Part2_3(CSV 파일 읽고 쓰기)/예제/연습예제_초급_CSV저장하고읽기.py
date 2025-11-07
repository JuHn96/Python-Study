import pandas as pd

# 데이터 생성
students = pd.DataFrame({
    'name': ['김철수', '이영희', '박민수'],
    'math': [85, 92, 78],
    'english': [90, 88, 95]
})

# CSV로 저장
students.to_csv('students.csv', index=False, encoding='utf-8-sig')
print("저장 완료!")

# 다시 읽기
loaded = pd.read_csv('students.csv', encoding='utf-8-sig')
print("\n읽어온 데이터:\n", loaded)