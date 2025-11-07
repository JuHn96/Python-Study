# 여러 과목 점수
subjects = ["수학", "영어", "과학", "사회", "국어"]
student1 = [85, 90, 88, 92, 87]
student2 = [92, 88, 95, 89, 91]
student3 = [78, 85, 82, 80, 84]

students_scores = [student1, student2, student3]
''' 
[[85, 90, 88, 92, 87], [92, 88, 95, 89, 91], [78, 85, 82, 80, 84]] 
'''
student_names = ["김철수", "이영희", "박민수"]

# 1. 각 학생의 총점과 평균
print("=== 학생별 통계 ===")
for name, scores in zip(student_names, students_scores):
    print(name)
    print(scores)
    total = sum(scores)
    avg = total / len(scores)
    print(f"{name}: 총점 {total}, 평균 {avg:.1f}")
    
'''
김철수
[85, 90, 88, 92, 87]
김철수: 총점 442, 평균 88.4
이영희
[92, 88, 95, 89, 91]
이영희: 총점 455, 평균 91.0
박민수
[78, 85, 82, 80, 84]
박민수: 총점 409, 평균 81.8
'''
    
# 2. 과목별 평균
print("\n=== 과목별 평균 ===")
for subject, *scores in zip(subjects, *students_scores): #언패킹 연산자 *
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.1f}점")
    
# 3. 각 학생의 최고/최저 과목
print("\n=== 최고/최저 과목 ===")
for name, scores in zip(student_names, students_scores):
    subject_scores = list(zip(subjects, scores))
    best = max(subject_scores, key=lambda x: x[1])
    worst = min(subject_scores, key=lambda x: x[1])
    print(f"{name}: 최고 {best[0]}({best[1]}점), 최저 {worst[0]}({worst[1]}점)")

# 4. 전체 1등 과목
print("\n=== 과목별 1등 ===")
for subject, *scores in zip(subjects, *students_scores):
    print(subjects)
    print(*students_scores)  
    print(*scores)
    max_score = max(scores)
    max_idx = scores.index(max_score) #주어진 값의 인덱스
    winner = student_names[max_idx]
    print(f"{subject}: {winner} ({max_score}점)")
    
'''
=== 과목별 1등 ===
['수학', '영어', '과학', '사회', '국어']
[85, 90, 88, 92, 87] [92, 88, 95, 89, 91] [78, 85, 82, 80, 84]
85 92 78
수학: 이영희 (92점)
['수학', '영어', '과학', '사회', '국어']
[85, 90, 88, 92, 87] [92, 88, 95, 89, 91] [78, 85, 82, 80, 84]
90 88 85
영어: 김철수 (90점)
['수학', '영어', '과학', '사회', '국어']
[85, 90, 88, 92, 87] [92, 88, 95, 89, 91] [78, 85, 82, 80, 84]
88 95 82
과학: 이영희 (95점)
['수학', '영어', '과학', '사회', '국어']
[85, 90, 88, 92, 87] [92, 88, 95, 89, 91] [78, 85, 82, 80, 84]
92 89 80
사회: 김철수 (92점)
['수학', '영어', '과학', '사회', '국어']
[85, 90, 88, 92, 87] [92, 88, 95, 89, 91] [78, 85, 82, 80, 84]
87 91 84
국어: 이영희 (91점)
'''
# 5. 전교 1등
print("\n=== 전교 1등 ===")
averages = [sum(scores)/len(scores) for scores in students_scores]
best_student_idx = averages.index(max(averages))
best_student = student_names[best_student_idx]
best_avg = averages[best_student_idx]
print(f"{best_student} (평균 {best_avg:.1f}점)")

