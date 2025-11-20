from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 라이브러리 추가
import pandas as pd  # 데이터프레임 형태로 데이터 확인을 위해 추가
import matplotlib.font_manager as fm  # 한글 폰트 설정을 위해 추가

data = load_breast_cancer()  # 유방암 데이터셋 로드
X, y = data.data, data.target  # 특성과 타겟 분리

# 데이터프레임으로 변환하여 상위 5개 데이터 확인
# (데이터 컬럼명은 data.feature_names 사용)
df = pd.DataFrame(X, columns=data.feature_names)
print('데이터 샘플 확인:')
print(df.head())
print('타겟 샘플 확인:')
print(y[:5])

# 한글 폰트 설정 (폰트가 깨지지 않도록)
font_path = fm.findSystemFonts(fontpaths=None, fontext='ttf')
# 윈도우의 경우 'Malgun Gothic'이 기본적으로 설치되어 있음
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

X = StandardScaler().fit_transform(X)  # 특성 표준화
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 데이터 분할

model = LogisticRegression()  # 로지스틱 회귀 모델 생성
model.fit(X_train, y_train)  # 모델 학습
print(classification_report(y_test, model.predict(X_test)))  # 분류 리포트 출력

# 결과 시각화: 실제값과 예측값의 분포를 막대그래프로 표시
pred = model.predict(X_test)  # 예측값
plt.figure(figsize=(8,4))  # 그래프 크기 설정
plt.hist([y_test, pred], bins=2, label=['실제값', '예측값'], rwidth=0.8)
plt.xticks([0,1], ['악성', '양성'])  # x축 라벨 한글로 표시
plt.xlabel('클래스')  # x축 이름
plt.ylabel('샘플 수')  # y축 이름
plt.title('실제값과 예측값 분포 비교')  # 그래프 제목
plt.legend()  # 범례 표시
plt.show()  # 그래프 출력