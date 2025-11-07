import matplotlib.pyplot as plt
import numpy as np

# 요일별 방문자 수
days = ['월', '화', '수', '목', '금', '토', '일']
visitors = [120, 135, 128, 142, 156, 210, 198]

plt.bar(days, visitors, color='steelblue')
plt.xlabel('요일')
plt.ylabel('방문자 수')
plt.title('요일별 방문자 현황')
plt.grid(axis='y', alpha=0.3)
plt.show()

# 평균과 비교
avg = np.mean(visitors)
print(f"평균 방문자: {avg:.0f}명")
print(f"최다 방문 요일: {days[np.argmax(visitors)]}")