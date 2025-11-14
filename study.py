# 데이터
from sklearn.datasets import load_iris # 붓꽃 데이터
from sklearn.datasets import load_breast_cancer # 유방암 데이터
# from sklearn.datasets import fetch_california_housing # 캘리포니아 주택 가격 데이터
from sklearn.datasets import load_digits

from sklearn.ensemble import RandomForestClassifier # 랜덤포레스트 모델
from xgboost import XGBClassifier # xgboost 모델
from lightgbm import LGBMClassifier # LGB모델
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt # 그래프 그리기

# 데이터 딕셔너리
datas = {
    "iris": load_iris(),
    "bc" : load_breast_cancer(),
    "ch" : load_digits()
}
# 모델 딕셔너리
mds = {
    "RF" : RandomForestClassifier(n_estimators=100, random_state=42),
    "XGB" : XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'),
    "LGB" : LGBMClassifier()
}

for name, data in datas.items():
    X = data.data
    y = data.target

    # ch(캘리포니아)는 회귀 데이터 → 이진 분류용으로 라벨 변환
    if name == "ch":
        median = np.median(y)
        y = (y > median).astype(int)   # 0 = 저가, 1 = 고가
        target_names = ["low_price", "high_price"]
    else:
        # iris, bc는 원래 target_names가 들어있음
        if hasattr(data, "target_names"):
            target_names = data.target_names
        else:
            target_names = None


    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
    )
    print(name)
    for mname, model in mds.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        print("Accuracy:", acc)
        print("\n---------------------------------------------------------------------------------------\n")  
