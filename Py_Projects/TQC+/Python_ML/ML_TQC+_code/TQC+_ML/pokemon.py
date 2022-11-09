# %%
import pandas as pd
pokemon = pd.read_csv('../待編修檔/pokemon.csv')
features = ['Attack', 'Defense']
pokemon.dropna(subset=features, inplace=True)
filter1 = pokemon['Type1'] == 'Normal'
filter2 = pokemon['Type1'] == 'Fighting'
filter3 = pokemon['Type1'] == 'Ghost'
new_data = pokemon[filter1|filter2|filter3]
x = new_data[features]
y = new_data['Type1']

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.preprocessing import StandardScaler
std = StandardScaler()
std.fit(x)
x_std = std.transform(x)

from sklearn.svm import LinearSVC   
model= LinearSVC(C=0.1, dual=False, class_weight='balanced')
model.fit(x_std,y)
y_pred = model.predict(x_std)
print((y != y_pred ).sum())

from sklearn.metrics import accuracy_score
print('Accuracy: ', accuracy_score(y, y_pred).round(4))

from sklearn.metrics import f1_score
print('F1-score: ', f1_score(y, y_pred, average='weighted').round(4))

new = [[100,75]]
new_std = std.transform(new)
new_pred = model.predict(new_std)
print(le.inverse_transform(new_pred))


# %%
