# # 코드실행정상 빨간줄로 인해 전체 주석처리(전체선택 후 주석처리 해제하여 코드 실행)

# from sklearn.datasets import load_iris
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import classification_report
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib
# import pandas as pd

# iris = load_iris()
# X, y = iris.data, iris.target
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# # 데이터프레임으로 변환하여 확인
# df = pd.DataFrame(X, columns=iris.feature_names)
# df['target'] = y
# print(df.head())

# # 한글 폰트 설정 (윈도우 기본 폰트 사용)
# matplotlib.rc('font', family='Malgun Gothic')
# plt.rcParams['axes.unicode_minus'] = False

# model = SVC(kernel='linear')
# model.fit(X_train, y_train)
# print(classification_report(y_test, model.predict(X_test)))

# # 결과 시각화 (Confusion Matrix)
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(y_test, model.predict(X_test))
# plt.figure(figsize=(6,5))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
# plt.xlabel('예측값')
# plt.ylabel('실제값')
# plt.title('Confusion Matrix')
# plt.show()