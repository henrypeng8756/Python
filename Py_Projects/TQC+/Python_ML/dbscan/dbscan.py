# %%
import numpy as np
import pandas as pd
# TODO
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score as ss
# input_file = ('data_perf.txt')
# Load data 載入資料
# TODO
content = pd.read_table('data_perf.txt','r',s)



# Find the best epsilon 
eps_grid = np.linspace(0.3,1.2,num=10)
silhouette_scores = []
# TODO
eps_best = eps_grid[0]
print(eps_best)
silhouette_score_max = -1
labels_best = None
for eps in eps_grid:
    # Train DBSCAN clustering model 訓練DBSCAN分群模型
    model = DBSCAN(eps=eps, min_samples=5)
    model.fit(content)
    # ################
    # min_samples = 5
    # ################
    # Extract labels 提取標籤
    labels = model.labels_
    # Extract performance metric 提取性能指標
    silhouette_score = round(ss(content,labels),4)
    silhouette_score.append(silhouette_score)
    print("Epsilon:", eps, " --> silhouette score:", silhouette_score)
    if silhouette_score == silhouette_score_max:
        silhouette_score_max = silhouette_score
        eps_best = eps
        model_best = model
        labels_best = labels
    # TODO
    
    

# Best params
print("Best epsilon = %.4f" % (eps_best))

# Associated model and labels for best epsilon
model = model_best  # TODO
labels = labels_best # TODO

# Check for unassigned datapoints in the labels
# TODO


# Number of clusters in the data 
# TODO
print("Estimated number of clusters ="           )

# Extracts the core samples from the trained model
# TODO




# %%
