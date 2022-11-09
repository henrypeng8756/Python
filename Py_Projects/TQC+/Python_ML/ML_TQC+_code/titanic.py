#%% 
import pandas as pd 
import numpy as np 
from sklearn import preprocessing 
from sklearn import linear_model as lm 
# 原始資料 
tita = pd.read_csv("待編修檔/titanic.csv") 
age_namedian=np.nanmedian(tita['Age']) 
 
print(age_namedian) 
# TODO 
new_age=np.where(tita['Age'].isnull(),age_namedian,tita['Age']) 
# 更新後資料 
 
# TODO 
 
# 轉換欄位值成為數值 
label_encoder = preprocessing.LabelEncoder() 
encoded_class = label_encoder.fit_transform(tita['PClass']) 
# TODO 
x=pd.DataFrame([tita['SexCode'],new_age,encoded_class]).T 
y=pd.DataFrame(tita['Survived']) 
# 建立模型 
# TODO 
logi=lm.LogisticRegression() 
logi.fit(x,y) 
 
print('截距=',logi.intercept_.round(4)          ) 
print('迴歸係數=',logi.coef_[0][0].round(4)       ) 
 
 
# 混淆矩陣(Confusion Matrix)，計算準確度 
print(logi.score(x,y).round(4)) 
# TODO 
# %%
