#from sklearn import datasets
#from sklearn.model_selection import cross_val_predict
#from sklearn import linear_model
# %%
#  TODO
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split as tts 
from sklearn.linear_model import LinearRegression 
from sklearn.datasets import load_boston
boston = load_boston()
#df = pd.DataFrame(boston.data.T, ['CRIM','ZN','INDUS','CHAS','NOX','RM' ,'AGE','DIS','RAD','TAX', 'PTRATIO','B','LSTAT']) #有13個feature
# TODO
# MEDV即預測目標向量
# TODO
#df = df.T
#X = df[['CRIM','ZN','INDUS','CHAS','NOX','RM' ,'AGE','DIS','RAD','TAX', 'PTRATIO','B','LSTAT']]
#y = df['MEDV']
X = pd.DataFrame(boston.data)
y = pd.DataFrame(boston.target)
#分出20%的資料作為test set
# TODO
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.2, random_state=1)

#Fit linear model 配適線性模型
lm = LinearRegression()
lm.fit(XTrain, yTrain)
y_pred = lm.predict(XTest)

# TODO
print('MAE:', np.mean(abs(yTest-y_pred)).round(4))
print('MSE:', np.mean((yTest-y_pred)**2).round(4))
print('RMSE:', np.mean((yTest-y_pred)**2)**0.5)

X_new = ([[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90 , 4.98]])
prediction = lm.predict(X_new).round(4)
print(prediction)

# %%
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import pandas as pd
import numpy as np
boston = load_boston()
X = pd.DataFrame(boston.data)
y = pd.DataFrame(boston.target)
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.2, random_state=1)
lm = LinearRegression()
lm.fit(XTrain, yTrain)
y_pred = lm.predict(XTest)
print('MAE', np.mean(abs(yTest-y_pred)).round(4))
print('MSE', np.mean((yTest-y_pred)**2).round(4))
print('RMSE', np.mean((yTest-y_pred**2)**0.5))
X_new = ([[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750,
         65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]])
prediction = lm.predict(X_new).round(4)
print(prediction)

# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LinearRegression
boston = load_boston()
X = pd.DataFrame(boston.data)
y = pd.DataFrame(boston.target) 
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.2, random_state=1)
lm = LinearRegression()
lm.fit(XTrain, yTrain)
y_pred= lm.predict(XTest)
print('MAE', np.mean(abs(yTest-y_pred)).round(4))
print('MSE', np.mean((yTest-y_pred)**2).round(4))
print('RMSE', np.mean(((yTest-y_pred)**2)**0.5).round(4))    
X_new = ([[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750,
         65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]])
prediction = lm.predict(X_new).round(4)
print(prediction)

# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split as tts 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
boston = load_boston()
X = pd.DataFrame(boston.data)
y = pd.DataFrame(boston.target)
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.2, random_state=1)
lm = LinearRegression()
lm.fit(XTrain, yTrain)
y_pred = lm.predict(XTest)
print('MAE', mae(yTest, y_pred).round(4))
print('MSE', mse(yTest, y_pred).round(4))
print('RMSE', (mse(yTest, y_pred)**0.5).round(4))
X_new = ([[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750,
         65.20, 4.0900, 1, 296.0, 15.30, 396.90, 4.98]])
prediction = lm.predict(X_new).round(4)
print(prediction)

# %%
