import numpy as np

# 5명 학생, 3과목 점수
scores = np.array([[85, 90, 88],
                   [92, 88, 95],
                   [78, 82, 80],
                   [88, 85, 90],
                   [95, 92, 98]])
                   
print("점수표:\n", scores)

# 학생별 평균 (axis=1)
student_avg = scores.mean(axis=1)
print(f"\n학생별 평균: {student_avg}")
print(f"최우수 학생: {student_avg.argmax() + 1}번")

# 과목별 평균 (axis=0)
subject_avg = scores.mean(axis=0)
print(f"\n과목별 평균: {subject_avg}")
print(f"가장 어려운 과목: {subject_avg.argmin() + 1}번")

# 전체 통계
print(f"\n전체 평균: {scores.mean():.1f}")
print(f"전체 표준편차: {scores.std():.2f}")