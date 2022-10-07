# %%
import json
import csv
#showList = []
with open('read.json','r') as file:
    content = json.load(file)
#for i in content:
#    showList.append(i['title'])
#    showList.append(i['showUnit'])
#    showList.append(i['startDate'])
#    showList.append(i['endDate'])
#print(showList)
with open('write.csv','w') as csvFile:
    csvWriter = csv.writer(csvFile)
    for item in content:
        csvWriter.writerow([item['title'],item['showUnit'],item['startDate'],item['endDate']])



# %%
