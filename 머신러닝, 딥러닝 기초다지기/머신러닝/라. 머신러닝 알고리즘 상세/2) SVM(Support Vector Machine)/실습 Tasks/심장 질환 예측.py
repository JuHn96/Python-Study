

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

url = "https://gist.githubusercontent.com/trantuyen082001/1fc2f5c0ad1507f40e721e6d18b34138/raw/heart.csv"
df = pd.read_csv(url)

X = df.drop('output', axis=1)
y = df['output']

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SVC(kernel='rbf', C=1, random_state=42)
model.fit(X_train, y_train)

# 데이터 일부 확인
print("\n[데이터 샘플]")
print(df.head())

# 한글 폰트 설정 (Windows 기준)
matplotlib.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

print(classification_report(y_test, model.predict(X_test)))

# 결과 시각화: Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, model.predict(X_test))
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['0(음성)', '1(양성)'], yticklabels=['0(음성)', '1(양성)'])
plt.xlabel('예측값')
plt.ylabel('실제값')
plt.title('Confusion Matrix')
plt.show()
