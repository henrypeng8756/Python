# %%
from encodings import utf_8_sig
import csv

infn = 'input.csv'
outfn = 'output.csv'
with open(infn,'r') as csvRFile:
    csvReader = csv.reader(csvRFile)
    drinkList = list(csvReader)

with open(outfn,'w',newline='',encoding='utf_8_sig') as csvOFile:
    csvWriter = csv.writer(csvOFile)
    for wRow in drinkList:
        csvWriter.writerow(wRow)

with open(outfn,'a',newline='',encoding='utf_8_sig') as csvAFile:
    csvAWriter = csv.writer(csvAFile)
    drinkList.append(['花茶', '15'])
    drinkList.append(['蜜茶', '10'])
    csvAWriter.writerow(['=========='])
    for aRow in drinkList:
        csvAWriter.writerow(aRow)

# %%
infn = 'input.csv'
outfn = 'output.csv'
with open(infn, 'r') as csvRFile:
    csvReader = csv.reader(csvRFile)
    drinkList = list(csvReader)

with open(outfn, 'w', newline='', encoding='utf_8_sig') as csvOFile:
    csvWriter = csv.writer(csvOFile)
    for wRow in drinkList:
        csvWriter.writerow(wRow)
    csvWriter.writerow(['-'*10])
    for wRow in drinkList:
        csvWriter.writerow(wRow)
    csvWriter.writerow(['花茶', '15'])
    csvWriter.writerow(['蜜茶', '10'])
