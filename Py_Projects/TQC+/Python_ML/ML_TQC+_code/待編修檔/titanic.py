# %%
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression

# 原始資料
titanic = pd.read_csv("titanic.csv")

print('raw data')
# TODO
age_nanmedian = np.nanmedian(titanic['Age'])
# 將年齡的空值填入年齡的中位數
# TODO

print("年齡中位數=", age_nanmedian        )
# TODO
new_age = np.where(titanic['Age'].isnull(),age_nanmedian, titanic['Age'] )
# 更新後資料
print('new data')
# TODO

# 轉換欄位值成為數值
label_encoder = preprocessing.LabelEncoder()
encoded_class = label_encoder.fit_transform(titanic['PClass']        )
# TODO
x = pd.DataFrame([titanic['SexCode'], new_age, encoded_class]).T
y = pd.DataFrame(titanic['Survived'])

# 建立模型
# TODO
lm = LogisticRegression()
lm.fit(x,y)
print('截距=', lm.intercept_.round(4)         )
print('迴歸係數=', lm.coef_[0][0].round(4)       )


# 混淆矩陣(Confusion Matrix)，計算準確度
print('Confusion Matrix')
# TODO
print(lm.score(x,y).round(4))






# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

titanic = pd.read_csv('titanic.csv')
age_nanmedian = np.nanmedian(titanic['Age'])
print(age_nanmedian)
new_age = np.where(titanic['Age'].isnull(), age_nanmedian, titanic['Age'])
le = LabelEncoder()
encoded_class = le.fit_transform(titanic['PClass'])
x = pd.DataFrame([titanic['SexCode'], new_age, encoded_class]).T
y = pd.DataFrame(titanic['Survived'])
lm = LogisticRegression()
lm.fit(x,y)
print('Intercept: ', lm.intercept_.round(4))
print('Coef: ', lm.coef_[0][0].round(4))
print(lm.score(x,y).round(4))   


# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
titanic = pd.read_csv('titanic.csv')
age_nanmedian = np.nanmedian(titanic['Age'])
print(age_nanmedian)
new_age = np.where(titanic['Age'].isnull(), age_nanmedian, titanic['Age'])
le = LabelEncoder()
encoded_class = le.fit_transform(titanic['PClass'])
x = pd.DataFrame([titanic['SexCode'], new_age, encoded_class ]).T
y = pd.DataFrame(titanic['Survived'])
lm = LogisticRegression()
lm.fit(x,y)
print('Intercept: ', lm.intercept_.round(4))
print('Coef: ', lm.coef_[0][0].round(4))
print(lm.score(x,y).round(4))

# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
titanic = pd.read_csv('titanic.csv')
age_nanmedian = np.nanmedian(titanic['Age'])
print(age_nanmedian)
new_age = np.where(titanic['Age'].isnull(), age_nanmedian, titanic['Age'])
le = LabelEncoder()
encoded_class = le.fit_transform(titanic['PClass'])
lm = LogisticRegression()
x = pd.DataFrame([titanic['SexCode'], new_age, encoded_class]).T
y = pd.DataFrame(titanic['Survived'])
lm.fit(x,y)
print('Intercept: ',lm.intercept_.round(4))
print('Coef: ', lm.coef_[0][0].round(4))
print(lm.score(x,y).round(4))

# %%
