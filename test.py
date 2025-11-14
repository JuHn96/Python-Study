from sklearn.datasets import load_iris  # iris 데이터셋 불러오기
from sklearn.model_selection import train_test_split # 데이터 학습/테스트용 나누는 함수 가져오기
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report # 모델 성능평가 함수 가져오기
import matplotlib.pyplot as plt # 그래프 그리기 위해 plt로 함수 쓰기위해 가져오기
from sklearn.naive_bayes import GaussianNB # Naive Bayes 모델 가져오기
from sklearn.tree import DecisionTreeClassifier, plot_tree # DecisionTree 모델 가져오기


iris = load_iris() # 불러온 iris 데이터 통째로 불러오기
X = iris.data 
y = iris.target


# 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


models = {
    "Naive Bayes": GaussianNB(),
    "Decision tree": DecisionTreeClassifier()
}


results = {}

for name, model in models.items():

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc


    if name == "Naive Bayes":
        print(">>>>-- Naive Bayes --<<<<")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred, target_names=iris.target_names))
        print("Accuracy:", acc)
        print()


    elif name == "Decision tree":
        print("((((Decision Tree))))")
        print("Accuracy:", acc)
        plt.figure(figsize=(18, 10))
        plot_tree(
            model,
            feature_names=iris.feature_names,
            class_names=iris.target_names,
            filled=True,
            rounded=True,
            fontsize=10
        )
        plt.title("((((--  Decision Tree Visualization  --))))")
        plt.show()