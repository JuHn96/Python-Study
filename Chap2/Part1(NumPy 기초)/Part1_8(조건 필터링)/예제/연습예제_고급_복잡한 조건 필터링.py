import numpy as np

# 학생 데이터 (점수, 출석률)
scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 82, 91])
attendance = np.array([95, 90, 85, 100, 88, 70, 95, 92, 80, 98])
print("점수:", scores)
print("출석률:", attendance)

# 조건: 점수 85점 이상 AND 출석률 90% 이상
condition = (scores >= 85) & (attendance >= 90)
excellent = scores[condition]
print(f"\n우수 학생 점수: {excellent}")
print(f"우수 학생 수: {excellent.size}명")

# where 사용 (조건에 따라 다른 값)
# np.where(조건, 참일 때 값, 거짓일 때 값)
grade = np.where(scores >= 90, 'A',
         np.where(scores >= 80, 'B',
         np.where(scores >= 70, 'C', 'F')))
print(f"\n학점: {grade}")

# 점수 상위 30%
# 데이터를 크기 순으로 정렬했을 때, 하위 n%에 해당하는 값
percentile_70 = np.percentile(scores, 70)
top_30 = scores[scores >= percentile_70]
print(f"\n상위 30%: {top_30}")

# 조건별 집계
print(f"\nA학점 평균: {scores[grade == 'A'].mean():.1f}")
print(f"B학점 평균: {scores[grade == 'B'].mean():.1f}")