def one_hot_encode(labels):
    """범주형 데이터를 원-핫 인코딩"""
    # 1. 고유한 레이블 목록
    unique_labels = sorted(list(set(labels)))  # 정렬하면 순서 일정해짐
    # 2. 레이블 → 인덱스 매핑
    label_to_index = {label: idx for idx, label in enumerate(unique_labels)}
    # 3. 각 레이블을 원-핫 벡터로 변환
    encoded = []
    for label in labels:
        vector = [0] * len(unique_labels)
        vector[label_to_index[label]] = 1
        encoded.append(vector)
    return encoded

# 테스트
labels = ["cat", "dog", "cat", "bird", "dog"]
encoded = one_hot_encode(labels)
print(encoded)
