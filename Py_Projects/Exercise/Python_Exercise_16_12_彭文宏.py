# %%
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
sHeight = np.array([147,163,159,155,163,158,172,161,153,161])
sWeight = np.array([41,60,47,53,48,55,58.5,49,46,52.5])
x = pd.DataFrame(sWeight, columns=['Weight'])
y = pd.DataFrame(sHeight, columns=['Height'])
wlm = LinearRegression()
wlm.fit(y,x)
print('迴歸係數: ', wlm.coef_)
print('截距: ', wlm.intercept_)
ssHeight2predict = pd.DataFrame(np.array([155,165,170]),columns=['Height'])
predicted_weight = wlm.predict(ssHeight2predict)
for wFormat in predicted_weight:
    print('%.1f' %wFormat)

hlm = LinearRegression()
hlm.fit(x,y)
ssWeight2predict = pd.DataFrame(np.array([55,65,70]),columns=['Weight'])
predicted_height = hlm.predict(ssWeight2predict)
plt.scatter(sWeight,sHeight)
regression_height = hlm.predict(x)
plt.plot(sWeight,regression_height,color='blue')
plt.plot(ssWeight2predict, predicted_height, color='red', marker='o', markersize='10')
plt.show()

# %%
