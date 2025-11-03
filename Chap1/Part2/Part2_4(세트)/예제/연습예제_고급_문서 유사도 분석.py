# 두 문서
doc1 = "machine learning is great for data analysis"
doc2 = "deep learning is powerful for data processing"

# 단어 집합으로 변환
words1 = set(doc1.lower().split())
words2 = set(doc2.lower().split())
print("문서1 단어:", words1)
print("문서2 단어:", words2)

# 공통 단어
common_words = words1 & words2
print(f"\n공통 단어: {common_words}")

# 각 문서만의 고유 단어
unique_to_doc1 = words1 - words2
unique_to_doc2 = words2 - words1
print(f"문서1만의 단어: {unique_to_doc1}")
print(f"문서2만의 단어: {unique_to_doc2}")

# 자카드 유사도
all_words = words1 | words2
jaccard = len(common_words) / len(all_words)
print(f"\n자카드 유사도: {jaccard:.3f}")

# 코사인 유사도 계산을 위한 전체 단어 목록
vocabulary = sorted(all_words)
print(f"\n전체 어휘: {vocabulary}")

# 각 문서의 벡터 생성
vec1 = [1 if word in words1 else 0 for word in vocabulary]
vec2 = [1 if word in words2 else 0 for word in vocabulary]
print(f"문서1 벡터: {vec1}")
print(f"문서2 벡터: {vec2}")