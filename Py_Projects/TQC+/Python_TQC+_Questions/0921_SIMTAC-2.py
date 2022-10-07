# %% 
from email import contentmanager
import math
from time import time
from unittest.loader import VALID_MODULE_NAME
r = eval(input())
print('Radius = %.2f' %r)
print('Perimeter = %.2f' %(2*math.pi*r))
print('Area = %.2f' %(r**2*math.pi))

#%%
a = eval(input())
b = eval(input())
opt = input()
if opt == '+':
    print(a+b)
elif opt == '-':
    print(a-b)
elif opt == '*':
    print(a*b)
elif opt == '/':
    print(a/b)
elif opt == '//':
    print(a//b)
else:
    print(a%b)
    
# %%
a = eval(input())
numSum = 0
for times in range(1,a+1):
    if times % 5 == 0:
        numSum += times
print(numSum)

# %%
def compute():
    i = eval(input())
    j = eval(input())
    print(i**j)
compute()

# %%
numList = []
while True:
    n = eval(input())
    if n != 9999:
        numList.append(n)
        continue
    else:
        sorted(numList)
        print(min(numList))
        break

# %%
dayList = []
for week in range(1, 5):
    print('Week %d:' % (week))
    for days in range(1, 4):
        i = eval(input('Day %d:' % (days)))
        dayList.append(i)
print('Average: %.2f' % (sum(dayList)/12))
print('Highest: %s' % (max(dayList)))
print('Lowest: %s' % (min(dayList)))

# %%
nameDict = {}
while True:
    key = input("Key: ")
    if key != 'end':
        value = input("Value: ")
        nameDict[key] = value
        continue
    else:
        i = input('Search key: ')
        if i in nameDict:
            print('True')
        else:
            print('False')
        break
    
#Key: (後方有一空白格)
#key = input("Key: ")

#Value: (後方有一空白格)
#value = input("Value: ")

# %%
f_name = input()
str_old = input()
str_new = input()
#TODO

print("=== Before the replacement")
#TODO
with open(f_name, 'r') as file:
    content = file.read()
    print(content)

print("=== After the replacement")
#TODO
content = content.replace(str_old,str_new)
print(content)
# %%
