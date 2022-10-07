# %%
import enum
from unittest import result


def cleanstrList(dirtyList):
    dirtyList = str(dirtyList)
    dirtyList = dirtyList.strip('[]')
    dirtyList = dirtyList.replace(',','')
    print(dirtyList)

numList=[]
valueNum = eval(input('Enter a number: '))
for valueNum in range(1,valueNum+1):
    numList.append(valueNum)
    cleanstrList(numList)
cleanstrList(numList)
for valueNum in range(1,valueNum+1):
    numList.pop()
    cleanstrList(numList)

# %%
itemNumber = eval(input('Enter a number: '))
for i in range(1, itemNumber+1):
    for j in range(1,i+1):
        print(j, end=' ')
    print()

for i in range(1, itemNumber+1):
    for j in range(1,itemNumber+2-i):
        print(j, end=' ')
    print()
        
# %%

# %%
