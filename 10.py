import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Age': [23, 45, 31, 35, 40, 22, 29, 60, 55, 47],
    'SpendingScore': [77, 40, 60, 65, 35, 90, 75, 20, 25, 30],
    'Income': [30, 80, 50, 60, 70, 25, 45, 100, 90, 85]
})

X_scaled = StandardScaler().fit_transform(df)
X_pca = PCA(n_components=2).fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.title("Customer Data PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()