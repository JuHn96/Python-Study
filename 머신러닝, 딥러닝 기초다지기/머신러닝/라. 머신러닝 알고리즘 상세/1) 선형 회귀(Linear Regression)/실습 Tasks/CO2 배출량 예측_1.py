import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 데이터 로드 (미국 EPA 차량 연비 데이터)
#df = pd.read_csv("https://www.fueleconomy.gov/feg/epadata/vehicles.csv", low_memory=False)
df = pd.read_csv("./머신러닝, 딥러닝 기초다지기/머신러닝/라. 머신러닝 알고리즘 상세/1) 선형 회귀(Linear Regression)/실습 Tasks/vehicles.csv", low_memory=False)

# 올바른 컬럼명 사용: 'displ'이 엔진 배기량
df = df[['displ', 'cylinders', 'city08', 'co2TailpipeGpm']].dropna()

# 설명 변수 및 타겟 지정
X = df[['displ', 'cylinders', 'city08']]
y = df['co2TailpipeGpm']

# 데이터 분할 및 학습
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# 결과 출력
print("R² score:", model.score(X_test, y_test))