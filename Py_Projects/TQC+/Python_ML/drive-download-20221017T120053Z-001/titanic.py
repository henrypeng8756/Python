# %%
import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

# 原始資料
titanic = pd.read_csv("titanic.csv")
print('raw data')
# TODO
titanic.info()
age_median = np.nanmedian(titanic['Age'])
# 將年齡的空值填入年齡的中位數
# TODO
print("年齡中位數=", age_median)
# TODO
new_age = np.where(titanic['Age'].isnull(), age_median, titanic['Age'])
titanic['Age'] = new_age
# 更新後資料
print('new data')
# TODO
# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic['PClass'])
# TODO
x = pd.DataFrame([encoded_class, titanic['SexCode'],titanic['Age']]).T
y = titanic['Survived']

# 建立模型
# TODO
lm = linear_model.LogisticRegression()
lm.fit(x,y)
print('截距=', lm.intercept_)
print('迴歸係數=', lm.coef_)



# 混淆矩陣(Confusion Matrix)，計算準確度
print('Confusion Matrix')
# TODO
preds = lm.predict(x)
print(pd.crosstab(titanic['Survived'],preds))
print(lm.score(x,y))





# %%
