# 학생들의 점수
scores = [85, 92, 78, 90, 88]

# 첫 번째와 마지막 점수
print(f"첫 번째 점수: {scores[0]}")
print(f"마지막 점수: {scores[-1]}")

# 점수 추가
scores.append(95)
print(f"점수 추가 후: {scores}")

# 총점과 평균
total = sum(scores)
average = total / len(scores)
print(f"총점: {total}, 평균: {average:.1f}")