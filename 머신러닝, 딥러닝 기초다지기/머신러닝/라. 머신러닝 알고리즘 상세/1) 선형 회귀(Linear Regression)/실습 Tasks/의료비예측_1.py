import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 데이터 로드
df = pd.read_csv(
    "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
)

# 범주형 변수 원-핫 인코딩
df = pd.get_dummies(df, drop_first=True)

# 특성과 타겟 분리
X = df.drop("charges", axis=1)
y = df["charges"]

# 학습 / 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 모델 생성 및 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 성능 출력
print("테스트 데이터 R^2 score:", model.score(X_test, y_test))
