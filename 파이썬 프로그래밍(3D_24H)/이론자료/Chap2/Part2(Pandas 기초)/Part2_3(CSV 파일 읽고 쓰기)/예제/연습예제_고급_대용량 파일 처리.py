import pandas as pd
import numpy as np


# 대용량 파일 샘플 생성
large_data = pd.DataFrame({
    'id': range(1000),
    'value': np.random.randn(1000),
    'category': np.random.choice(['A', 'B', 'C'], 1000)
})
large_data.to_csv('large_file.csv', index=False)

# 청크로 나눠서 읽기
chunk_size = 100
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    # 각 청크 처리    
    processed = chunk[chunk['value'] > 0]
    chunks.append(processed)
    
# 합치기
result = pd.concat(chunks, ignore_index=True)
print(f"원본: {len(large_data)}개")
print(f"처리 후: {len(result)}개")

# 메모리 효율적으로 읽기 (타입 최적화)
df_optimized = pd.read_csv('large_file.csv', dtype={
    'id': 'int32',
    'value': 'float32',
    'category': 'category'})
    
print(f"\n메모리 사용량:")
print(large_data.memory_usage(deep=True).sum() / 1024, "KB")
print(df_optimized.memory_usage(deep=True).sum() / 1024, "KB")