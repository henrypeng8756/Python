#%% 
import numpy as np 
# TODO 
import pandas as pd 
from sklearn.cluster import DBSCAN 
from sklearn.metrics import silhouette_score as ss 
# Load data 載入資料 
# TODO 
x=pd.read_table('data_perf.txt',header=None,sep=',') 
 
# Find the best epsilon  
eps_grid = np.linspace(0.3,1.2,10            ) 
sil_max=0 
# TODO 
for i in eps_grid: 
    clu=DBSCAN(eps=i,min_samples=5) 
    clu.fit(x) 
    sil=ss(x,clu.labels_).round(4) 
    if sil_max<sil: 
        sil_max=sil 
        best_eps=i 
        clu_num=len(set(clu.labels_))-1 
print(best_eps,sil_max,clu_num) 
 
x=pd.read_table('data_perf_add.txt',header=None,sep=',') 
 
# Find the best epsilon  
eps_grid = np.linspace(0.3,1.2,10            ) 
sil_max=0 
# TODO 
for i in eps_grid: 
    clu=DBSCAN(eps=i,min_samples=5) 
    clu.fit(x) 
    sil=ss(x,clu.labels_).round(4) 
    if sil_max<sil: 
        sil_max=sil 
        best_eps=i 
        clu_num=len(set(clu.labels_))-1 
print(sil_max)
