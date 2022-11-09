# %%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score as acc
from sklearn.metrics import f1_score as f1
pokemon = pd.read_csv('pokemon.csv')
features = ['Attack','Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1'] == 'Normal'
filter2 = pokemon['Type1'] == 'Fighting'
filter3 = pokemon['Type1'] == 'Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']
std = StandardScaler()
std.fit(x)
x_std = std.transform(x)
le = LabelEncoder()
y = le.fit_transform(y)
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y != y_pred ).sum())
print('Acc:', acc(y,y_pred).round(4))
print('f1:', f1(y,y_pred,average='weighted').round(4))
new = [[100,75]]
new_std = std.transform(new)
new_pred = model.predict(new_std)
print(le.inverse_transform(new_pred))
