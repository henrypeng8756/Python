# %%
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.linear_model import LogisticRegression
breast_cancer = datasets.load_breast_cancer()
X = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
# print(breast_cancer.feature_names)
# print(breast_cancer.target)
target = pd.DataFrame(breast_cancer.target, columns=['Target'])
y = target['Target']
lm = LogisticRegression()
lm.fit(X,y)
print(f'全部資料的R_Squared: {lm.score(X,y)}')
print('--------')
XTrain, XTest, yTrain, yTest = tts(X,y, test_size=0.3, random_state=10)
lm1 = LogisticRegression()
lm1.fit(XTrain,yTrain)
print(f'全部資料訓練7比測試3的R_Squared: {lm1.score(XTest,yTest)}')
print('--------')
# print()
# print(abs(lm.coef_))
# print(abs(lm.coef_).shape)
# print(breast_cancer.feature_names)
# print((breast_cancer.feature_names).shape)
X1 = pd.DataFrame(abs(lm.coef_).T,breast_cancer.feature_names, columns=['coef'] )
# print(X1)
top5causes = X1.sort_values('coef', ascending=False).head(5)
# print(top5causes)
X2 = pd.DataFrame([X['worst radius'],X['mean radius'],X['worst concavity'],X['worst compactness'],X['worst texture']]).T
lm2 = LogisticRegression()
lm2.fit(X2,y)
print(f'全部資料前五高關聯性的R_Squared: {lm2.score(X2,y)}')
print('--------')

 # %%
