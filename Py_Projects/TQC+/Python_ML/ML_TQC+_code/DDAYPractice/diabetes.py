# %%
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_diabetes  
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split as tts 
diabetes = load_diabetes()
x = pd.DataFrame(diabetes.data)
y = pd.DataFrame(diabetes.target)
lm = LinearRegression()
lm.fit(x,y)
y_pred = lm.predict(x)
print('MSE: ', mse(y, y_pred).round(4))
print('RSqur: ', lm.score(x,y).round(4))
xTrain2, xTest2, yTrain2, yTest2 = tts(x,y,test_size=0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(xTrain2, yTrain2)
yTest_pred = lm2.predict(xTest2)
yTrain_pred = lm2.predict(xTrain2)
print('Train_MSE: ', mse(yTrain2, yTrain_pred).round(4))
print('Test_MSE: ', mse(yTest2, yTest_pred).round(4))

# %%
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split as tts 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target
xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.25, random_state=100)
lm = LinearRegression()
lm.fit(x,y)
y_pred = lm.predict(x)
print('MSE: ', mse(y,y_pred).round(4))
print('Rsqr: ', lm.score(x,y).round(4))
lm2 = LinearRegression()
lm2.fit(xTrain,yTrain)
yTest_pred = lm2.predict(xTest)
yTrain_pred = lm2.predict(xTrain)
print('Train_MSE: ', mse(yTrain, yTrain_pred).round(4))
print('Test_MSE: ', mse(yTest, yTest_pred).round(4))

# %%
