## Matplotlib이란?

Matplotlib은 파이썬에서 **그래프와 차트**를 그리는 라이브러리.
데이터를 시각적으로 표현하여 패턴을 쉽게 파악.

### 설치 및 import

```python
# 설치 (터미널에서)
pip install matplotlib

# import
import matplotlib.pyplot as plt

```

### plot에서 한글깨질때(colab에서)

```python
# 폰트 설치
!apt-get -qq -y install fonts-nanum
```

첫번째 셀에서 폰트 지정

```python
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# 시스템에 있는 한글 폰트 찾기
font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')
nanum_fonts = [f for f in font_list if 'Nanum' in f or 'nanum' in f]
print("설치된 나눔 폰트:", nanum_fonts)

# 폰트 직접 로드
if nanum_fonts:
    fm.fontManager.addfont(nanum_fonts[0])
    font_name = fm.FontProperties(fname=nanum_fonts[0]).get_name()
    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False
```

### VScode에서 글자가 깨진다면 아래 코드를 `import` 밑에 추가
```py
from matplotlib import rcParams

# 한글 폰트 설정 (설치된 폰트명으로 변경 가능)
rcParams['font.family'] = 'Malgun Gothic'  # 또는 'NanumGothic'
rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지
```