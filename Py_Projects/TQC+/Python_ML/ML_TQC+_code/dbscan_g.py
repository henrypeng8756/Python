import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

input_file = ('data_perf.txt')
# Load data 載入資料
# TODO
x = []
with open(input_file) as f:
for line in f.readlines():
data = [float(i) for i in line.split(",")]
x.append(data)
x = np.array(x)


# Find the best epsilon
eps_grid = np.linspace(0.3,1.2,10)
epsB = eps_grid[0]
labelB = None
ssmax = -1
silhouette_scores = []
# TODO
for eps in eps_grid:
# Train DBSCAN clustering model 訓練DBSCAN分群模型
# ################
# min_samples = 5
# ################
model = DBSCAN(eps=eps, min_samples = 5).fit(x)

# Extract labels 提取標籤
labels = model.labels_

# Extract performance metric 提取性能指標
sc = round(silhouette_score(x,labels),4)
silhouette_scores.append(sc)


print("Epsilon:", eps, " --> silhouette score:", sc)

# TODO
if sc > ssmax:
ssmax = sc
modelB = model
labelB = labels
epsB = eps


# Best params
print("Best epsilon =", epsB)

# Associated model and labels for best epsilon
model = modelB # TODO
labels = labelB # TODO

# Check for unassigned datapoints in the labels
# TODO
offset = 0
if -1 in set(labels):
offset = 1

# Number of clusters in the data
# TODO
print("Estimated number of clusters =", len(set(labels))-offset)

# Extracts the core samples from the trained model
# TODO

input_file2 = ('data_perf_add.txt')
# Load data 載入資料
# TODO
x2 = []
with open(input_file2) as f:
for line in f.readlines():
data2 = [float(i) for i in line.split(",")]
x2.append(data2)
x2 = np.array(x2)

new = model.fit(x2)
print("silhoutte score :", silhouette_score(x2,new.labels_))
