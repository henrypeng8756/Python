# %%
# #############################################################################
# 本題參數設定，請勿更改
seed = 0    # 亂數種子數
# #############################################################################
# TODO

import numpy as np
from sklearn.datasets import load_digits
digits = load_digits()
# 載入手寫數字資料集
X_digits = digits.data   #TODO    數值特徵
y_digits = digits.target   #TODO    數字類別

# 特徵標準化(scale/StandardScaler)
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler
# TODO
x_std = scale(X_digits)

# 取出資料集的數字類別數
n_digits = 10


# 建立兩個 K-Means 模型，除以下參數設定外，其餘為預設值
# #############################################################################
# kmean1: init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed
# kmean2: init='random', n_clusters=n_digits, n_init=10, random_state=seed
# #############################################################################
from sklearn.cluster import KMeans
# TODO
kmean1 = KMeans(init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed)
kmean2 = KMeans(init='random', n_clusters=n_digits, n_init=10, random_state=seed)
# 利用 PCA 結果建立 K-Means 模型，除以下參數設定外，其餘為預設值
# #############################################################################
# pca: n_components=n_digits, random_state=seed
# kmean3: init=pca.components_, n_clusters=n_digits, n_init=1, random_state=seed
# #############################################################################
from sklearn.decomposition import PCA
# TODO
pca = PCA(n_components=n_digits, random_state=seed).fit(x_std)
kmean3 = KMeans(init=pca.components_, n_clusters=n_digits, n_init=1, random_state=seed)

# 分別計算上述三個 K-Means 模型的輪廓係數(Silhouette coefficient)與
# 分類準確率(accuracy)，除以下參數設定外，其餘為預設值
# #############################################################################
# silhouette_score: metric='euclidean'
# #############################################################################
from sklearn.metrics import silhouette_score as ss
from sklearn.metrics import accuracy_score as acc
lst_name = ['K-Mean (k-means++)', 'K-Means (random)', 'K-Means (PCA-based)']
# TODO
lst_model = [kmean1,kmean2,kmean3]
for name, model in zip(lst_name, lst_model):
    model.fit(x_std)
    pred = model.predict(x_std)
    print(name, 'ss', ss(x_std, model.labels_, metric='euclidean').round(4))
    print(name, 'acc', acc(y_digits, pred).round(4))
# 進行 PCA 降維後再做 K-Means，除以下參數設定外，其餘為預設值
# #############################################################################
# kmeans: init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed
# PCA: n_components=2, random_state=seed
# #############################################################################
# TODO
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10, random_state=seed)
reduct = PCA(n_components=2, random_state=seed).fit_transform(x_std)
kmeans.fit(reduct)
pred2 = kmeans.predict(reduct)
print('PCA+KMeans Silhouette=   ', ss(reduct, kmeans.labels_).round(4)     )
print('Accuracy=    ', acc(y_digits, pred2).round(4)                 )

# %%
