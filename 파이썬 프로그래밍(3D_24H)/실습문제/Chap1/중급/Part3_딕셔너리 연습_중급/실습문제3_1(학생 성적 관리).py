students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88,
    "최동욱": 95
    }

# 평균 80점 이상인 학생 찾기
passed_students = [name for name, score in students.items() if score >= 80]

# 가장 높은 점수와 학생 이름 찾기
top_student = max(students.items(), key=lambda x: x[1])

# 평균이 가장 높은 학생 찾기
avg_score = sum(students.values()) / len(students)
top_avg_students = [name for name, score in students.items() if score > avg_score]

# 결과 출력
print("--- 결과 ---")
print(f"80점 이상인 학생: {passed_students}")
print(f"가장 높은 점수: {top_student[0]} ({top_student[1]}점)")

# 추가 시도
print(f"전체 평균 점수: {avg_score:.2f}")
print(f"전체 평균 이상 점수인 학생: {top_avg_students}")
