# [행렬 공식 Click](/이론자료/Chap2/행렬공식.md)

### Chap1 이후 Chap2부터 중급문제 없이 실습문제로 통합

### 그래프에 글자 표시할때 글자가 깨진다면 아래 코드를 `import` 밑에 추가

```py
from matplotlib import rcParams

# 한글 폰트 설정 (설치된 폰트명으로 변경 가능)
rcParams['font.family'] = 'Malgun Gothic'  # 또는 'NanumGothic'
rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지
```