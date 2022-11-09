# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
titanic = pd.read_csv('../DDAYPractice/titanic.csv')
age_nanmedian = np.nanmedian(titanic['Age'])
print(age_nanmedian)
new_age = np.where(titanic['Age'].isnull(), age_nanmedian, titanic['Age'])
le = LabelEncoder()
encoded_class = le.fit_transform(titanic['PClass'])
x = pd.DataFrame([titanic['SexCode'], new_age, encoded_class]).T
y = pd.DataFrame(titanic['Survived'])
lm = LogisticRegression()
lm.fit(x,y)
print('Intercept: ', lm.intercept_.round(4))
print('Coef: ', lm.coef_[0][0].round(4))
print('Score: ', lm.score(x,y).round(4))


# %%
