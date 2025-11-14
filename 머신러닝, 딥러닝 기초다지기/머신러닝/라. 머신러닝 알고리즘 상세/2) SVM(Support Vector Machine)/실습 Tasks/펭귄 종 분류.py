

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.font_manager as fm

df = sns.load_dataset("penguins").dropna()
print("데이터프레임 샘플:")
print(df.head())
X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

X = StandardScaler().fit_transform(X)
y = y.astype('category').cat.codes  # 문자열을 숫자로 변환

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = SVC(kernel='rbf')
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

# 한글 폰트 설정 (윈도우 기본 폰트 사용)
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False)

# Confusion Matrix 시각화
pred = model.predict(X_test)
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=np.unique(y), yticklabels=np.unique(y))
plt.xlabel('예측값')
plt.ylabel('실제값')
plt.title('Confusion Matrix')
plt.show()