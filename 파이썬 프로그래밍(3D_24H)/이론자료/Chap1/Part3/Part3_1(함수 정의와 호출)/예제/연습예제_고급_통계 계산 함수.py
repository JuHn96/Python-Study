def calculate_statistics(data):
    """데이터의 기본 통계량 계산"""    
    n = len(data)
    
    # 평균   
    mean = sum(data) / n
    
    # 중앙값
    sorted_data = sorted(data)    # 항상 리스트 형태로 반환    
    if n % 2 == 0:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) / 2    
    else:
        median = sorted_data[n//2]
        
    # 분산과 표준편차    
    variance = sum((x - mean)**2 for x in data) / n
    std_dev = variance ** 0.5    
    
    # 최소, 최대, 범위    
    min_val = min(data)
    max_val = max(data)
    range_val = max_val - min_val
    
    return {
        "count": n,
        "mean": mean,
        "median": median,
        "std_dev": std_dev,
        "variance": variance,
        "min": min_val,
        "max": max_val,
        "range": range_val
    }
    
# 테스트
scores = [85, 92, 78, 90, 88, 76, 95, 89, 82, 91]
stats = calculate_statistics(scores)

print("=== 통계 분석 결과 ===")
for key, value in stats.items():
    print(f"{key}: {value:.2f}")
    
# 표준점수(Z-score) 계산 함수
def calculate_z_scores(data):
    """각 데이터의 표준점수 계산"""    
    stats = calculate_statistics(data)
    mean = stats["mean"]
    std = stats["std_dev"]
    
    z_scores = [(x - mean) / std for x in data]
    return z_scores
    
z_scores = calculate_z_scores(scores)

print("\n=== 표준점수 ===")
for i, (score, z) in enumerate(zip(scores, z_scores)):
    print(f"점수 {score}: Z = {z:.2f}")