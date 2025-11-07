# 여러 좌표 변환
points = [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# 각 좌표를 (x, y, x+y) 형태로 변환
transformed = []
for x, y in points:
    new_point = (x, y, x + y)
    transformed.append(new_point)
    
print("원본 좌표:", points)
print("변환된 좌표:", transformed)

# 극좌표로 변환 (r, θ)
import math

polar_coords = []
for x, y in points:
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x) * 180 / math.pi  # 라디안을 도로    
    polar_coords.append((r, theta))
    
print("극좌표:", [(f"{r:.2f}", f"{theta:.1f}°") for r, theta in polar_coords])