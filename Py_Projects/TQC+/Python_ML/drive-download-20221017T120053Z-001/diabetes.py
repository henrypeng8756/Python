# %%
from sklearn import datasets
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
# TODO
diabetes = datasets.load_diabetes()
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.DataFrame(diabetes.target, columns=['target'])

#get x
# TODO 
lm = LinearRegression()
lm.fit(x,y)


#Total number of examples
# TODO 
lm.score(x,y)
pred = lm.predict(x)

print('Total number of examples')
print('MSE=',np.mean((y-pred)**2)        )
print('R-squared=',lm.score(x, y))
#3:1 100
xTrain2, xTest2, yTrain2, yTest2= tts(x,y,test_size=0.25,random_state=100)
lm2=LinearRegression()
lm2.fit(xTrain2,yTrain2)
# TODO 
pred_train = lm2.predict(xTrain2)
pred_test = lm2.predict(xTest2)



print('Split 3:1')
print('train MSE=',np.mean((yTrain2 - pred_train)**2)           )
print('test MSE=', np.mean((yTest2-pred_test)**2)            )
print('train R-squared=', lm2.score(xTrain2,yTrain2)              )
print('test R-squared='                )

# %%
