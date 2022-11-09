# %%
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
pokemon = pd.read_csv('pokemon.csv')
features = ['Attack','Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1'] == 'Normal'
filter2 = pokemon['Type1'] == 'Fighting'
filter3 = pokemon['Type1'] == 'Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']
le = LabelEncoder()
y = le.fit_transform(y)
std = StandardScaler()
std.fit(x)
x_std = std.transform(x)
model = LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y!=y_pred).sum())
print('Accuracy: ', accuracy_score(y, y_pred).round(4))
print('F1-Score: ', f1_score(y,y_pred,average='weighted').round(4))
new = [[100,75]]
new_std = std.transform(new)
new_pred= model.predict(new_std)
print(le.inverse_transform(new_pred)) 

# %%
