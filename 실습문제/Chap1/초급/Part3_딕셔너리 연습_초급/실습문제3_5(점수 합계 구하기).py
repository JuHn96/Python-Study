scores = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "정지원": 88}
    
# 여기에 코드 작성
# .values() 메서드를 사용하여 점수들만 추출
total_score = sum(scores.values())
average_score = total_score / len(scores) # 위에 총합을 이용해 평균 계산
print(f"총점: {total_score}, 평균: {average_score:.2f}")