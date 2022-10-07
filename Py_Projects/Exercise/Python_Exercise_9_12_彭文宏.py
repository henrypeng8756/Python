# %%
import json
dayMenu = {'breakfast':50,'lunch':80,'dinner':100}
with open('../Output/menuCost.json','w') as jsonW:
    json.dump(dayMenu,jsonW)

# %%
import json
with open('../Output/menuCost.json','r') as jsonR:
    content = json.load(jsonR)
    print('早餐費用: %s 元'%(content['breakfast']))
    print('午餐費用: %s 元'%(content['lunch']))
    print('晚餐費用: %s 元'%(content['dinner']))
    

# %%
