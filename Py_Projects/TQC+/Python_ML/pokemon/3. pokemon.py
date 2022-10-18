# %%
import pandas as pd

# 載入寶可夢資料集
# TODO
content = pd.read_csv('pokemon.csv')
# 處理遺漏值
features = ['Attack', 'Defense']
# TODO
content.dropna(axis=0, subset=features, inplace=True)
# 取出目標寶可夢的 Type1 與兩個特徵欄位
# TODO
filter1 = content['Type1']=='Ghost'
filter2 = content['Type1']=='Normal'
filter3 = content['Type1']=='Fighting'
content_data = content[filter1|filter2|filter3]
X_train, y_train = content_data[features],content_data['Type1']

# 編碼 Type1
from sklearn.preprocessing import LabelEncoder
# TODO
le = LabelEncoder()
y_train = le.fit_transform(y_train)

# 特徵標準化
from sklearn.preprocessing import StandardScaler
# TODO
scaler = StandardScaler()
scaler.fit(X_train)
X_train_std = scaler.transform(X_train)

# 建立線性支援向量分類器，除以下參數設定外，其餘為預設值
# #############################################################################
# C=0.1, dual=False, class_weight='balanced'
# #############################################################################
from sklearn.svm import LinearSVC
# TODO
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(X_train_std,y_train)
# 計算分類錯誤的數量
# TODO
y_pred = model.predict(X_train_std)
print('Misclassified Samples: %d' % (y_train != y_pred).sum())
# 計算準確度(accuracy)
from sklearn.metrics import accuracy_score
print('Accuracy: %.4f' % (accuracy_score(y_train,y_pred))           )

# 計算有加權的 F1-score (weighted)
from sklearn.metrics import f1_score
# TODO
f1 = f1_score(y_train,y_pred,average='weighted')
print('F1-score: %.4f' % (f1))

# 預測未知寶可夢的 Type1
# TODO
new_data = [[100,75]]
new_data = scaler.transform(new_data)
label = le.inverse_transform(model.predict(new_data))
print(label)


# %%
