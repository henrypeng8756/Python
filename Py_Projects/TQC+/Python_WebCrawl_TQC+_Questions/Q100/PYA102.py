# %%
import xml.etree.ElementTree as et
import csv 
tree = et.ElementTree(file='read.xml')
root = tree.getroot()
with open('read.xml','r',encoding='utf_8') as csvFile:
    csvwriter = csv.writer(csvFile)
    ubike = []
    for row in root:
        sno = row.find('sno').text
        ubike.append(sno)
        sna = row.find('sna').text
        ubike.append(sna)
        tot = row.find('tot').text
        ubike.append(tot)
csvwriter.writerow(ubike)
csvFile.close()


    

# %%
