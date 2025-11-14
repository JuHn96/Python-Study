# 1. 라이브러리 불러오기
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 2. 데이터 불러오기
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = diabetes.target

# 3. 특정 특성만 사용해서 단순 선형 회귀 (예: 'bmi')
X_bmi = X[['bmi']]  # body mass index

# 4. 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_bmi, y, test_size=0.2, random_state=42)

# 5. 모델 학습
model = LinearRegression()
model.fit(X_train, y_train)

# 6. 예측
y_pred = model.predict(X_test)

# 7. 성능 평가
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# 8. 회귀선 시각화
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('BMI')
plt.ylabel('Disease Progression')
plt.title('Linear Regression on BMI')
plt.legend()
plt.grid(True)
plt.show()
