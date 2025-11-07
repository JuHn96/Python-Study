import numpy as np

# 간단한 이미지를 행렬로 표현 (3x3 grayscale)
image = np.array([[100, 150, 200],
                  [120, 180, 220],
                  [140, 190, 240]])
print("원본:\n", image)

# 밝기 조정 (+50)
brighter = np.clip(image + 50, 0, 255)
'''
np.clip(배열, 최솟값, 최댓값)
배열의 값을 특정 범위로 제한
최솟값보다 작으면 → 최솟값으로
최댓값보다 크면 → 최댓값으로
'''
print("\n밝게:\n", brighter)

# 명암 조정 (대비 증가)
contrast = np.clip((image - 128) * 1.5 + 128, 0, 255)
print("\n대비:\n", contrast.astype(int))

# 흑백 반전
inverted = 255 - image
print("\n반전:\n", inverted)

# 블러 효과 (간단한 평균 필터)
padded = np.pad(image, 1, mode='edge')
blurred = np.zeros_like(image)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        kernel = padded[i:i+3, j:j+3]
        blurred[i, j] = kernel.mean()
        
print("\n블러:\n", blurred.astype(int))