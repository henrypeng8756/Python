# %%
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
diabetes = datasets.load_diabetes()
x = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=['Target'])
y = target['Target']
lm = LinearRegression()
lm.fit(x,y)
predicted_slv = lm.predict(x)
plt.figure(1)
plt.scatter(y,predicted_slv)
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.title('Quatitative Measure vs Predicted Quantitative Measure')
plt.show()

x2 = x[['age','sex','bmi','bp']]
lm2 = LinearRegression()
lm2.fit(x2,y)
predicted_slv2 = lm2.predict(x2)
plt.figure(2)
plt.scatter(y,predicted_slv2)
plt.xlabel('Quantitative Measure')
plt.ylabel('Predicted Quantitative Measure')
plt.title('Quatitative Measure vs Predicted Quantitative Measure')
plt.show()
# %%

# %%
