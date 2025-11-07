import numpy as np

# RGB 이미지 (3x3 픽셀, 3채널)
image = np.random.randint(0, 256, (3, 3, 3))
print("원본 이미지 (3x3x3):\n", image)

# 채널 분리
r = image[:, :, 0]
g = image[:, :, 1]
b = image[:, :, 2]
print("\nRed:\n", r)
print("Green:\n", g)
print("Blue:\n", b)

# 그레이스케일 변환
gray = 0.299 * r + 0.587 * g + 0.114 * b
print("\nGrayscale:\n", gray.astype(int))

# 1차원으로 펼치기
flat = image.flatten()
print(f"\nFlattened shape: {flat.shape}")

# 다시 복원
restored = flat.reshape(3, 3, 3)
print("\n복원 확인:", np.array_equal(image, restored))