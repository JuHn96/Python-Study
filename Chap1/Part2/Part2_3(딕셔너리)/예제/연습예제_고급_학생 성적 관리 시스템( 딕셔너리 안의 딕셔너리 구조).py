# 학생별 과목 점수
students = {
    "김철수": {"math": 85, "english": 90, "science": 88},
    "이영희": {"math": 92, "english": 88, "science": 95},
    "박민수": {"math": 78, "english": 85, "science": 82}
}

# 각 학생의 평균 계산
print("=== 학생별 평균 ===")
student_averages = {}
for name, scores in students.items():
    avg = sum(scores.values()) / len(scores)
    student_averages[name] = avg
    print(f"{name}: {avg:.1f}점")
    
# 과목별 평균 계산
print("\n=== 과목별 평균 ===")
subjects = ["math", "english", "science"]
for subject in subjects:
    total = sum(student[subject] for student in students.values())
    avg = total / len(students)
    print(f"{subject}: {avg:.1f}점")
    
# 최우수 학생 찾기
best_student = max(student_averages, key=student_averages.get)
print(f"\n최우수 학생: {best_student} ({student_averages[best_student]:.1f}점)")

# 각 과목별 1등
print("\n=== 과목별 1등 ===")
for subject in subjects:
    best = max(students.items(), key=lambda x: x[1][subject])
    '''
     `x`: 각 튜플 (이름, 점수딕셔너리)
     `x[1]`: 점수 딕셔너리 부분
     `x[1][subject]`: 해당 과목의 점수
    '''
    print(f"{subject}: {best[0]} ({best[1][subject]}점)")