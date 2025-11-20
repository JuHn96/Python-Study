import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.csv"
# 현재 외부 csv not found로 실행 X
df = pd.read_csv(url, sep=';')
df = pd.get_dummies(df, drop_first=True)  # 범주형 처리

X = df.drop('y_yes', axis=1, errors='ignore')
y = df['y'].map({'yes': 1, 'no': 0}) if 'y' in df.columns else df['y_yes']

X = StandardScaler().fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))