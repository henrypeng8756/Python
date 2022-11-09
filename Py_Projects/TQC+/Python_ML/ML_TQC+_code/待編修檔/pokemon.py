# %%
import pandas as pd

# 載入寶可夢資料集
# TODO
pokemon = pd.read_csv('pokemon.csv')
# 處理遺漏值
features = ['Attack', 'Defense']
# TODO
pokemon.dropna(subset=features, inplace=True)
# 取出目標寶可夢的 Type1 與兩個特徵欄位
# TODO
filter1 = pokemon['Type1']=='Ghost'
filter2 = pokemon['Type1']=='Normal'
filter3 = pokemon['Type1']=='Fighting'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']
# 編碼 Type1
from sklearn.preprocessing import LabelEncoder
# TODO
le = LabelEncoder()
y = le.fit_transform(y)
# 特徵標準化
from sklearn.preprocessing import StandardScaler
# TODO
std = StandardScaler()
std.fit(x)
x_std=std.transform(x)

# 建立線性支援向量分類器，除以下參數設定外，其餘為預設值
# #############################################################################
# C=0.1, dual=False, class_weight='balanced'
# #############################################################################
from sklearn.svm import LinearSVC
# TODO
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
# 計算分類錯誤的數量
# TODO
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y!=y_pred).sum())

# 計算準確度(accuracy)
from sklearn.metrics import accuracy_score
print('Accuracy: ', accuracy_score(y,y_pred).round(4)          )

# 計算有加權的 F1-score (weighted)
from sklearn.metrics import f1_score
# TODO
print('F1-score: ', f1_score(y,y_pred,average='weighted').round(4)         )

# 預測未知寶可夢的 Type1
# TODO
new = [[100,75]]    
new_std= std.transform(new)
new_pred= model.predict(new_std)
print(le.inverse_transform(new_pred))


# %%
import pandas as pd
pokemon = pd.read_csv('pokemon.csv')
features = ['Attack','Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1'] == 'Normal'
filter2 = pokemon['Type1'] == 'Fighting'
filter3 = pokemon['Type1'] == 'Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
std.fit(x)
x_std = std.transform(x)

from sklearn.svm import LinearSVC
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y != y_pred).sum())

from sklearn.metrics import accuracy_score
print('Accuracy:', accuracy_score(y,y_pred).round(4))

from sklearn.metrics import f1_score
print('Score:', f1_score(y,y_pred,average='weighted').round(4))

new=[[100,75]]
new_std= std.transform(new)
new_pred = model.predict(new_std)
print(le.inverse_transform(new_pred))

# %%
import pandas as pd
pokemon = pd.read_csv('pokemon.csv')
features = ['Attack','Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1']=='Normal'
filter2 = pokemon['Type1']=='Fighting'
filter3 = pokemon['Type1']=='Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
std.fit(x)
x_std = std.transform(x)

from sklearn.svm import LinearSVC
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y!=y_pred).sum())

from sklearn.metrics import accuracy_score
print('Accuracy:', accuracy_score(y, y_pred).round(4))

from sklearn.metrics import f1_score
print('f1-score:', f1_score(y, y_pred, average='weighted').round(4))

new = [[100,75]]
new_std = std.transform(new)
new_pred = model.predict(new_std)
print(le.inverse_transform(new_pred))

# %%
import pandas as pd
pokemon = pd.read_csv('pokemon.csv')
features = ['Attack', 'Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1'] == 'Normal'
filter2 = pokemon['Type1'] == 'Fighting'
filter3 = pokemon['Type1'] == 'Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
std.fit(x)  
x_std = std.transform(x)

from sklearn.svm import LinearSVC
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y != y_pred).sum())

from sklearn.metrics import accuracy_score
print('Accuracy: ', accuracy_score(y, y_pred).round(4) )

from sklearn.metrics import f1_score
print('f1-score: ', f1_score(y, y_pred, average='weighted').round(4))

new = [[100,75]]
new_std = std.transform(new)
new_pred = model.predict(new_std)
print(le.inverse_transform(new_pred))

# %%
