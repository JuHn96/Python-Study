import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89, 82, 91])
print("전체 점수:", scores)
print("90점 이상:", scores[scores >= 90])
print("80점 미만:", scores[scores < 80])
print("80~90점:", scores[(scores >= 80) & (scores < 90)])