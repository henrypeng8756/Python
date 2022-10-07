# %%
import numpy as np
numList = []
for i in range(20):
    numList.append(np.random.randint(1,21))
arr = np.array(numList).reshape(5,4)
print(f'隨機正整數： {numList}')
print(f'X矩陣內容： \n{arr}')
print(f'最大： {arr.max()}')
print(f'最小： {arr.min()}')
print(f'平均： {arr.mean()}')
print(f'總和： {arr.sum()}')
print(f'標準差： {arr.std()}')
print(f'四個角落元素：\n{arr[np.ix_([0,4],[0,3])]}')

# %%
import numpy as np
arr = np.random.randint(1,21,(5,4))
print(f'隨機正整數： {numList}')
print(f'X矩陣內容： \n{arr}')
print(f'最大： {arr.max()}')
print(f'最小： {arr.min()}')
print(f'平均： {arr.mean()}')
print(f'總和： {arr.sum()}')
print(f'標準差： {arr.std()}')
print(f'四個角落元素：\n{arr[np.ix_([0,4],[0,3])]}')

# %%
