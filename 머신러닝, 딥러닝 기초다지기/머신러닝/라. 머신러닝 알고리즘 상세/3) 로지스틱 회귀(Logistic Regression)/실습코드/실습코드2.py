# 1. 라이브러리 불러오기
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 2. 데이터 로드
data = load_breast_cancer()
print(data.feature_names)

df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
print(df.head())

sns.countplot(x=data.target, palette="Set2")
plt.xticks([0, 1], data.target_names)
plt.title("Target Distribution")
plt.show()

X = data.data
y = data.target
print("Target classes:", data.target_names)  # ['malignant' 'benign']

# 3. 데이터 스케일링 (정규화)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. 훈련/테스트 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5. 로지스틱 회귀 모델 정의 및 학습
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# 6. 예측
y_pred = model.predict(X_test)

# 7. 평가 출력
print("Accuracy:", accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=data.target_names, yticklabels=data.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
print("Classification Report:\n", classification_report(y_test, y_pred))