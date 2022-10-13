# %%
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts 
diabetes = datasets.load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['Target'])
y = target['Target']
lm = LinearRegression()
lm.fit(X,y)
pred = lm.predict(X)
MSE = np.mean((y-pred)**2)
print('原始資料')
print('MSE: ', MSE)
print('R-Square: ', lm.score(X,y))
print()
XTrain, XTest, yTrain, yTest = tts(X,y,test_size= 0.33, random_state=100)
lm1 = LinearRegression()
lm1.fit(XTrain, yTrain)
pred_train1 = lm1.predict(XTrain)
pred_test1 = lm1.predict(XTest)
MSE_train1 = np.mean((yTrain-pred_train1)**2)
MSE_test1 = np.mean((yTest-pred_test1)**2)
print('3:1, random_state=100')
print('訓練資料的MSE: ', MSE_train1)
print('測試資料的MSE: ', MSE_test1)
print('訓練資料的R-Square: ', lm1.score(XTrain,yTrain))
print('測試資料的R-Square: ', lm1.score(XTest, yTest))
print()

ZTrain, ZTest, aTrain, aTest = tts(X,y,test_size= 0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(ZTrain,aTrain)
pred_train2 = lm2.predict(ZTrain)
pred_test2 = lm2.predict(ZTest)
MSE_train2 = np.mean((aTrain-pred_train2)**2)
MSE_test2 = np.mean((aTest-pred_test2)**2)
print('4:1, random_state=100')
print('訓練資料的MSE: ', MSE_train)
print('測試資料的MSE: ', MSE_test)
print('訓練資料的R-Square: ', lm2.score(ZTrain, aTrain))
print('測試資料的R-Square: ', lm2.score(ZTest, aTest))

# %%
