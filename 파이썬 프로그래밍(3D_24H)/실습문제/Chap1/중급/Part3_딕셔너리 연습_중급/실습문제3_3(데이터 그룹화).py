students = [
    {"name": "김철수", "grade": 1, "score": 85},
    {"name": "이영희", "grade": 2, "score": 92},
    {"name": "박민수", "grade": 1, "score": 78},
    {"name": "정지원", "grade": 2, "score": 88},
    {"name": "최동욱", "grade": 1, "score": 95}
]
# 여기에 코드 작성
# 결과: {1: [...], 2: [...]}

grouped_students = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped_students:
        grouped_students[grade] = []
    grouped_students[grade].append(student)

print("\n기대 출력:")
print(grouped_students)

print("\n각 학년별로 그룹 표시")
for grade, members in grouped_students.items():
    print(f"--- {grade}학년 ---")
    for member in members:
        print(f"{member['name']}: {member['score']}점")
