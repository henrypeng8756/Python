# %%
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
temperatures = np.array(
    [29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])
drink_sales = np.array([7.7, 6.2, 9.3, 8.4, 5.9, 6.4,
                       8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4])
x = pd.DataFrame(temperatures, columns=['Temperatures'])
y = pd.DataFrame(drink_sales, columns=['Drink_Sales'])
lm = LinearRegression()
lm.fit(x, y)
print('迴歸係數:', lm.coef_)
print('截距:', lm.intercept_)
new_temperatures = pd.DataFrame(np.array([26, 30]), columns=['Temperatures'])
predicted_sales = lm.predict(new_temperatures)
print(predicted_sales)
plt.scatter(temperatures, drink_sales)
regression_sales = lm.predict(x)
plt.plot(temperatures, regression_sales, color='blue')
plt.plot(new_temperatures, predicted_sales,
         color='red', marker='o', markersize=10)
plt.show()

# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
waist_heights = np.array([[67, 160], [68, 165], [70, 167], [65, 170], [80, 165],
                          [85, 167], [78, 178], [79, 182], [95, 175], [89, 172]])
weights = np.array([50, 60, 65, 65, 70, 75, 80, 85, 90, 81])
x = pd.DataFrame(waist_heights, columns=['Waist', 'Height'])
y = pd.DataFrame(weights, columns=['Weights'])
lm = LinearRegression()
lm.fit(x, y)
print('迴歸係數: ', lm.coef_)
print('截距: ', lm.intercept_)
new_waist_heights = pd.DataFrame(np.array([[66, 164], [82, 172]]))
predicted_weights = lm.predict(new_waist_heights)
print(predicted_weights)

# %%
from sklearn import datasets
# use of regressions
boston = datasets.load_boston()
diabetes = datasets.load_diabetes()
# use of catagorized
iris = datasets.load_iris()
digits = datasets.load_digits()

print(boston.keys())
print(diabetes.keys())
print(iris.keys())
print(iris.target)
print(digits.keys())
print(boston['target'])
print(boston.DESCR)
print(boston.values())

# %%
from sklearn import datasets
boston = datasets.load_boston()
print(boston.keys())
print(boston.data.shape)
print(boston.feature_names)
print(boston.DESCR)

# %%
import pandas as pd
from sklearn import datasets
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
print(x.head())
target = pd.DataFrame(boston.target, columns=['MEDV'])
print(target.head())

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數: ',lm.coef_)
print('截距: ', lm.intercept_)
coef = pd.DataFrame(boston.feature_names, columns=['features'])
coef['estimatedCoefficients'] = lm.coef_
print(coef)
plt.scatter(x.RM,y)
plt.xlabel('Average number of rooms per dwelling(RM)')
plt.ylabel('Housing Price(MEDV)')
plt.title('Relationship between RM and Price')
plt.show()

# %%
# print multiple df testing
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)
print('迴歸係數: ',lm.coef_)
print('截距: ', lm.intercept_)
coef = pd.DataFrame(boston.feature_names, columns=['features'])
coef['estimatedCoefficients'] = lm.coef_
print(coef)
for i in coef:
    plt.scatter(x[i],y)
    plt.xlabel('Average number of rooms per dwelling(RM)')
    plt.ylabel('Housing Price(MEDV)')
    plt.title('Relationship between RM and Price')
    plt.show()

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
boston = datasets.load_boston()

x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
lm = LinearRegression()
lm.fit(x,y)

predicted_price = lm.predict(x)
print(predicted_price[0:5])

plt.scatter(y, predicted_price)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain,yTrain)
pred_test = lm.predict(xTest)
plt.scatter(yTest, pred_test)
plt.xlabel('Price')
plt.ylabel('Predicted Price')
plt.title('Price vs Predicted Price')
plt.show()

# %%
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split as tts
iris_data = load_iris()
data = iris_data.data
target =iris_data.target
x_train, x_test, y_train, y_test = tts(data, target, test_size=0.25)

# %%
import random
for i in range(5):
    print(random.randint(1,100))

# %%
import random
random.seed(101)
for i in range(5):
    print(random.randint(1,100))

# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np 
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']
xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain, yTrain)
pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)
MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
print('訓練資料的MSE: ', MSE_train)
print('測試資料的MSE: ', MSE_test)
print('訓練資料的R-Square: ', lm.score(xTrain, yTrain))
print('測試資料的R-Square: ', lm.score(xTest, yTest))


# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as tts
import matplotlib.pyplot as plt
import numpy as np 
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
target = pd.DataFrame(boston.target, columns=['MEDV'])
y = target['MEDV']

xTrain, xTest, yTrain, yTest = tts(x,y,test_size=0.33, random_state=5)
lm = LinearRegression()
lm.fit(xTrain, yTrain)

pred_train = lm.predict(xTrain)
pred_test = lm.predict(xTest)

plt.scatter(pred_train,yTrain-pred_train, c='b', s=40, alpha=0.5, label='Training Data')
plt.scatter(pred_test, yTest-pred_test, c='r', s=40, label='Test Data')
plt.title('Residual Plot')
plt.ylabel('Residual Value')
plt.legend()
plt.show()

# %%
