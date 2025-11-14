def preprocess_data(data):
    # """결측치 제거 → 이상치 제거(평균±2*표준편차) → 0~1 정규화(+소수 둘째자리 반올림)"""
    # 1) 결측치 제거
    cleaned = [x for x in data if x is not None]
    if not cleaned:
        return []

    # 2) 평균, 표준편차
    n = len(cleaned)
    mean = sum(cleaned) / n
    variance = sum((x - mean) ** 2 for x in cleaned) / n
    std = variance ** 0.5

    # 3) 이상치 제거
    lower, upper = mean - 2 * std, mean + 2 * std
    filtered = [x for x in cleaned if lower <= x <= upper]
    if not filtered:
        return []

    # 4) 정규화 (0~1 스케일)
    min_v, max_v = min(filtered), max(filtered)
    if max_v == min_v:
        normalized = [0.0 for _ in filtered]
    else:
        normalized = [(x - min_v) / (max_v - min_v) for x in filtered]

    # 5) 소수 둘째자리로 반올림
    normalized = [round(x, 2) for x in normalized]
    return normalized


# 테스트
raw_data = [10, 20, None, 30, 40, 50, 200, 60, 70, None, 80]
processed = preprocess_data(raw_data)
print(f"원본: {raw_data}")
print(f"전처리 후: {processed}")
