# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression
breast_cancer = datasets.load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
# print(breast_cancer.feature_names)
# print(breast_cancer.target)
target = pd.DataFrame(breast_cancer.target, columns=['Target'])
y = target['Target']
lm = LogisticRegression
lm.fit(X,y)


XTrain, Xtest, yTrain, yTest = tts(X,y, test_size=0.30, random_state=10)
lm1 = LogisticRegression
pred_train = 
pred_test = 

# %%
