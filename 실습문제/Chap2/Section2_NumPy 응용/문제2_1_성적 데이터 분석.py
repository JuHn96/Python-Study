import numpy as np

scores = np.array([[85, 90, 78],
                   [92, 88, 95],
                   [78, 82, 80],
                   [88, 85, 90],
                   [95, 92, 98]])
                   
# 1. 각 학생의 평균
student_avg = scores.mean(axis=1)
print("학생별 평균:", student_avg)

# 2. 각 과목의 평균
subject_avg = scores.mean(axis=0)
print("과목별 평균:", subject_avg)

# 3. 전체 평균
total_avg = scores.mean()
print("전체 평균:", total_avg)

# 4. 최고점
print("최고점:", scores.max())

# 5. 평균이 가장 높은 학생
best_student = student_avg.argmax() #최고값의 인덱스 반환
print(f"최우수 학생: {best_student}번 (평균 {student_avg[best_student]:.2f})")