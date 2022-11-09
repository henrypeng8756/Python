#%% 
from sklearn.datasets import load_diabetes 
import pandas as pd 
import sklearn.linear_model as lm 
import numpy as np 
from sklearn.model_selection import train_test_split as tts 
# TODO 
dia=load_diabetes() 
x=pd.DataFrame(dia.data) 
y=pd.DataFrame(dia.target) 
#Total number of examples 
# TODO  
line=lm.LinearRegression() 
line.fit(x,y) 
y_pred=line.predict(x) 
 
print('MSE=',np.mean((y-y_pred)**2).round(4)                 ) 
print('R-squared=',line.score(x,y).round(4)           ) 
#3:1 100 
x0,x1,y0,y1=tts(x,y,test_size=0.25,random_state=100) 
line.fit(x0,y0) 
y0_pred=line.predict(x0) 
y1_pred=line.predict(x1) 
 
 
print('train MSE=',np.mean((y0-y0_pred)**2).round(4)            ) 
print('test MSE=',np.mean((y1-y1_pred)**2).round(4)             ) 
 
 
# %%
