from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 한글 폰트 설정 (윈도우 기본 폰트 사용)
matplotlib.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

data = load_breast_cancer()
X, y = data.data, data.target

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SVC(kernel='rbf')
model.fit(X_train, y_train)

# 데이터 확인
print('데이터 shape:', X.shape)
print('타겟 shape:', y.shape)
print('특성 이름:', data.feature_names)
print('타겟 이름:', data.target_names)
print('첫 5개 데이터 샘플:\n', X[:5])
print('첫 5개 타겟 값:', y[:5])

print(classification_report(y_test, model.predict(X_test)))

# 예측 결과 시각화
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_test_2d = pca.fit_transform(X_test)
y_pred = model.predict(X_test)

plt.figure(figsize=(8,6))
for label, color, name in zip([0,1], ['red','blue'], data.target_names):
    plt.scatter(X_test_2d[y_pred==label,0], X_test_2d[y_pred==label,1],
                c=color, label=f'예측: {name}', alpha=0.5, marker='o')
plt.title('SVM 예측 결과 (PCA 2D 투영)')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.legend()
plt.show()