# %%
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import mean_squared_error as mse
diabetes = load_diabetes()
x = diabetes.data
y = diabetes.target
xTrain, xTest, yTrain, yTest = tts(x,y, test_size=0.25, random_state=100)
lm = LinearRegression()
lm.fit(x,y)
y_pred = lm.predict(x)
print('MSE:', mse(y,y_pred).round(4))
print('RSqur:', lm.score(x,y).round(4))
lm2 = LinearRegression()
lm2.fit(xTrain,yTrain)
yTrain_pred = lm2.predict(xTrain)
yTest_pred = lm2.predict(xTest)
print('Train MSE:', mse(yTrain, yTrain_pred).round(4))
print('Test MSE:', mse(yTest, yTest_pred).round(4))
