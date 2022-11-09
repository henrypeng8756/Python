# %%
from sklearn.datasets import load_diabetes
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
# TODO
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data)
y = pd.DataFrame(diabetes.target)
lm = LinearRegression()
lm.fit(X,y)
y_pred = lm.predict(X)
#get x
# TODO 


#Total number of examples
# TODO 


print('Total number of examples')
print('MSE=',mse(y,y_pred).round(4)                 )
print('R-squared=', lm.score(X,y).round(4)       )
#3:1 100
xTrain2, xTest2, yTrain2, yTest2= tts(X,y,test_size=0.25, random_state=100)
lm2=LinearRegression()
lm2.fit(xTrain2,yTrain2)
yTrain2_pred= lm2.predict(xTrain2)
yTest2_pred= lm2.predict(xTest2)

# TODO 



print('Split 3:1')
print('train MSE=', mse(yTrain2,yTrain2_pred).round(4)          )
print('test MSE=', mse(yTest2,yTest2_pred).round(4)            )
print('train R-squared='               )
print('test R-squared='                )

# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data)
y = pd.DataFrame(diabetes.target)
lm = LinearRegression()
lm.fit(X,y)
y_pred = lm.predict(X)
print('MSE', mse(y,y_pred).round(4))
print('RSqur', lm.score(X,y).round(4))
XTrain, XTest, yTrain, yTest = tts(X,y, test_size=0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(XTrain, yTrain)
yTrain_pred = lm2.predict(XTrain)
yTest_pred = lm2.predict(XTest)
print('Trained_MSE', mse(yTrain,yTrain_pred).round(4))
print('Test_MSE', mse(yTest, yTest_pred).round(4))

# %%
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data)
y = pd.DataFrame(diabetes.target)
lm = LinearRegression()
lm.fit(X,y)
y_pred = lm.predict(X)
print('MSE', mse(y, y_pred).round(4))
print('Rsqur', lm.score(X,y).round(4))
XTrain, XTest, yTrain, yTest= tts(X,y,test_size=0.25, random_state=100)
lm2 = LinearRegression()
lm2.fit(XTrain,yTrain)
yTrain_pred = lm2.predict(XTrain)
yTest_pred = lm2.predict(XTest)
print('Train_MSE', mse(yTrain, yTrain_pred).round(4))
print('Test_MSE', mse(yTest, yTest_pred).round(4))

# %%
