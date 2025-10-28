scores = [85, 92, 78, 90, 88, 76, 95, 89]
total = sum(scores)
avg = total / len(scores)
max_score = max(scores)
min_score = min(scores)

print(f"총점: {total}, 평균: {avg:.2f}, 최고점: {max_score}, 최저점: {min_score}")