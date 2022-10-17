# %%
import pandas as pd
from sklearn.model_selection import train_test_split as tts
from sklearn import datasets, neighbors
from sklearn import tree
iris = datasets.load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.DataFrame(iris.target, columns=['target'])
k = 50
knn = neighbors.KNeighborsClassifier(n_neighbors=k)
knn.fit(X,y)
dtree = tree.DecisionTreeClassifier(max_depth=4)
dtree.fit(X,y)
print('KNN模型訓練的R_Squared: %.2f \n\
    Tree模型訓練的R_Squared: %.2f' % (knn.score(X, y),dtree.score(X, y)))
# print(f'{knn.score(X,y)},{dtree.score(X,y)}')
XTrain, XTest, yTrain, yTest = tts(X,y,test_size=0.4, random_state=50)
guess_k = 3
knn_1 = neighbors.KNeighborsClassifier(n_neighbors=guess_k)
guess = knn_1.fit(XTrain, yTrain)
print(knn_1.score(XTest, yTest))
pred_list = []
for best_k in range(1,61):
   knn_1 = neighbors.KNeighborsClassifier(n_neighbors=best_k)
   knn_1.fit(XTrain, yTrain)
   pred_list.append(knn_1.score(XTest, yTest))

print(sorted(pred_list)[0])

#print(f'{knn.score(X,y)},{dtree.score(X,y)}')
# for i in range(guess_list):
#     for j in range(pred_list):
#         if abs(guess_list[i]) > abs(pred_list[j]):
#             pred_list.remove(pred_list[j])
#             pred_list.append(guess_list[i])
#         break



# %%
