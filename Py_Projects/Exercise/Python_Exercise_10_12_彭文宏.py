# %% 
from encodings import utf_8
import json
fltred_list = []
with open('Questions/Exercise_10/drugstore.json','r',encoding='utf_8') as jsonFile:
    content = json.load(jsonFile)
    for row in content:
        if row[0]['機構狀態'] == '開業' and row[2]['地址縣市別'] == '新北市':
            fltred_list.append('%s\t%s%s%s'%(row[1]['機構名稱'],row[2]['地址縣市別'],row[3]['地址鄉鎮市區'],row[4]['地址街道巷弄號']))
for show_row in fltred_list[10:20]:
    print(show_row)

# %%
