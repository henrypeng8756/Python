# %%
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score as ss 
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3,1.2, num=10)
sil_max = -1 
for i in eps_grid:
    model= DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1
print(best_eps, sil_max, model_num)

# %%
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN  
from sklearn.metrics import silhouette_score as ss
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
sil_max = -1
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1
print(best_eps, sil_max, model_num)

# %%
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN    
from sklearn.metrics import silhouette_score as ss
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
sil_max = -1
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1
print(best_eps, sil_max, model_num)

# %%
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score as ss
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
max_sil = -1
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if max_sil < sil:
        max_sil = sil
        best_eps = i
        model_num = len(set(model.labels_))-1 
print(best_eps, max_sil, model_num)

# %%
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score as ss
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3,1.2, num=10)
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1
print(best_eps, sil_max, model_num)

x = pd.read_table('data_perf_add.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
print(sil_max)

# %%
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN 
from sklearn.metrics import silhouette_score
x = pd.read_table('data_perf.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
sil_max = -1 
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x,model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
        best_eps = i
        model_num = len(set(model.labels_))-1 
print(best_eps, sil_max, model_num)

x = pd.read_table('data_perf_add.txt', header=None, sep=',')
eps_grid = np.linspace(0.3, 1.2, num=10)
sil_max = -1
for i in eps_grid:
    model = DBSCAN(eps=i, min_samples=5).fit(x)
    sil = ss(x, model.labels_).round(4)
    if sil_max < sil:
        sil_max = sil
print(sil_max)

# %%
