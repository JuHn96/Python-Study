def calculate_statistics(data):
    """통계 계산 함수
    Returns: (평균, 분산, 표준편차)
    """
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std = variance ** 0.5
    return mean, variance, std


# 테스트
data = [10, 20, 30, 40, 50]
mean, variance, std = calculate_statistics(data)
print(f"평균: {mean}, 분산: {variance}, 표준편차: {std:.2f}")