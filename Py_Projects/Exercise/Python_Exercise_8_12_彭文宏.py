# %%
import xml.etree.ElementTree as et
import csv
tree = et.ElementTree(file='Questions/Exercise_8/FarmTransData.xml')
table = tree.getroot()
aliasList = []
goodList = []
avgPList = []
tradeVList = []
for value in table:
    aliasList.append(value[1].text)
    goodList.append(value[3].text)
    avgPList.append(value[9].text)
    tradeVList.append(value[10].text)
for showList in range(5):
    print(aliasList[showList],goodList[showList],avgPList[showList],tradeVList[showList])
with open('Questions/Exercise_8/write.csv','w',encoding='utf_8') as csvWFile:
    content = csv.writer(csvWFile)
    content.writerow(['作物代號','作物名稱','平均價','交易量'])
    for csvList in range(5):
        content.writerow([aliasList[csvList],goodList[csvList],avgPList[csvList],tradeVList[csvList]])


# %%
