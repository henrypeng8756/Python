#%% 
#from sklearn import datasets 
#from sklearn.model_selection import cross_val_predict 
from sklearn import linear_model as lm 
from sklearn.model_selection import train_test_split as tts 
# TODO 
from sklearn.datasets import load_boston 
import pandas as pd 
import numpy as np 
bos = load_boston() 
x=pd.DataFrame(bos.data) 
y=pd.DataFrame(bos.target) 
#分出20%的資料作為test set 
# TODO 
x0,x1,y0,y1=tts(x,y,test_size=0.2,random_state=1) 
 
#Fit linear model 配適線性模型 
line=lm.LinearRegression() 
line.fit(x0,y0) 
y_pred=line.predict(x1) 
# TODO 
print('MAE:', np.mean(abs(y1-y_pred)).round(4)             ) 
print('MSE:' ,np.mean((y1-y_pred)**2).round(4)             ) 
print('RMSE:' ,np.mean((y1-y_pred)**2)**0.5             ) 
 
X_new=([[0.00632, 18.00, 2.310, 0, 0.5380, 6.5750, 65.20, 4.0900, 1, 296.0, 15.30, 396.90 , 4.98]]) 
prediction = line.predict(X_new).round(4) 
print(prediction) 
 
# %%
