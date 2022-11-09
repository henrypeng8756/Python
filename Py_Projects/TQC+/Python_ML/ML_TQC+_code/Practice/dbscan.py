# %%
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN  
from sklearn.metrics import silhouette_score as ss
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid= np.linspace(0.3, 1.2, num=10)
sil_max = -1
for i in eps_grid:
    model= DBSCAN(eps= i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1
print(best_eps, sil_max, model_num)

# %%
