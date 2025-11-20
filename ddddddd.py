from sklearn.datasets import load_iris, load_breast_cancer, load_digits # 붓꽃 데이터
from sklearn.ensemble import RandomForestClassifier # RandomForest 모델
from xgboost import XGBClassifier # xgboost 모델
from lightgbm import LGBMClassifier # LGB 모델
from sklearn.model_selection import train_test_split # 손글씨 숫자 이미지 데이터
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score # 유방암 데이터

# 데이터 딕셔너리
datas = {
    "iris": load_iris(),
    "bc" : load_breast_cancer(),
    "digits" : load_digits()
}

# 모델 딕셔너리 – 생성 함수로 저장
mds = {
    "RF" : lambda: RandomForestClassifier(n_estimators=100, random_state=42),
    "XGB": lambda: XGBClassifier(use_label_encoder=False, eval_metric='mlogloss'),
    "LGB": lambda: LGBMClassifier(verbose=-1)
}

for name, data in datas.items():
    X = data.data
    y = data.target

    # target_names 준비
    target_names = data.target_names if hasattr(data, "target_names") else None
    if target_names is not None and not isinstance(target_names[0], str):
        # digits처럼 숫자인 경우 문자열로 변환
        target_names = [str(t) for t in target_names]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\n==============================")
    print("데이터셋:", name)
    print("==============================")

    for mname, model_builder in mds.items():
        model = model_builder()

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        print(f"\n--- 모델: {mname} ---")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))

        print("\nClassification Report:")
        if target_names is not None:
            print(classification_report(y_test, y_pred, target_names=target_names))
        else:
            print(classification_report(y_test, y_pred))

        print("Accuracy:", acc)
        print("\n" + "-"*90 + "\n")
