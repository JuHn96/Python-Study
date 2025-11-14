

# # 참고용 구조 (실제 경로와 파일 구조 필요)
# import librosa
# import os
# import numpy as np
# from sklearn.svm import SVC
# from sklearn.model_selection import train_test_split

# X, y = [], []
# for label, folder in enumerate(["happy", "sad", "angry"]):
#     files = os.listdir(f"./RAVDESS/{folder}")
#     for file in files:
#         signal, sr = librosa.load(f"./RAVDESS/{folder}/{file}")
#         mfccs = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=13)
#         X.append(np.mean(mfccs.T, axis=0))
#         y.append(label)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = SVC(kernel='rbf')
# model.fit(X_train, y_train)
# print("Accuracy:", model.score(X_test, y_test))