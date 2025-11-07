# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.xlabel('X축 이름')        # x축 레이블
# plt.ylabel('Y축 이름')        # y축 레이블
# plt.title('그래프 제목')       # 제목
# plt.grid(True)               # 격자 표시
# plt.show()

import matplotlib.pyplot as plt
from matplotlib import rcParams

# 한글 폰트 설정 (설치된 폰트명으로 변경 가능)
rcParams['font.family'] = 'Malgun Gothic'  # 또는 'NanumGothic'
rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel('X축 이름')
plt.ylabel('Y축 이름')
plt.title('그래프 제목')
plt.grid(True)
plt.show()
