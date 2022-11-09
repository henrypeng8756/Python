# %%
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split as tts 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data)
y = pd.DataFrame(diabetes.target)
lm = LinearRegression()
lm.fit(X,y)
y_pred = lm.predict(X)
print('MSE', mse(y,y_pred).round(4))
print('RSqur', lm.score(X,y).round(4))
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(XTrain,yTrain)
yTrain_pred = lm2.predict(XTrain)
yTest_pred = lm2.predict(XTest)
print('Train_MSE', mse(yTrain, yTrain_pred).round(4))
print('Test_MSE', mse(yTest, yTest_pred).round(4))



# %%
