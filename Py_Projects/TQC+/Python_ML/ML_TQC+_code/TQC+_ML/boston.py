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
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.2,random_state=1)
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
