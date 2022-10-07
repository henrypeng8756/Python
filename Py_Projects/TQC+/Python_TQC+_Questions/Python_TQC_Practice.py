# %%
# 101
from time import daylight


# 101
from asyncore import read


a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
print('|%5d %5d|'%(a,b))
print('|%5d %5d|'%(c,d))
print('|%-5d %-5d|'%(a,b))
print('|%-5d %-5d|'%(c,d))

# %%
# 108
x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print('(',x1,',',y1,')')
print('(',x2,',',y2,')')
print('Distance = %.4f'%(((x1-x2)**2+(y1-y2)**2)**0.5))

# %%
# 204
a = eval(input())
b = eval(input())
opt = input()
if opt == '+':
    print('%d'%(a+b))
elif opt == '-':
    print('%d'%(a-b))
elif opt == '*':
    print('%d'%(a*b))
elif opt == '/':
    print('%d'%(a/b))
elif opt == '//':
    print('%d'%(a//b))
else:
    print('%d'%(a%b))

# %%
# 208
i = eval(input())
if i >= 10 and i <= 16:
    print(str.upper(str((hex(i)))).lstrip('0X'))
else:
    print(i)

# %%
# 304
a = eval(input())
numSum = 0
for divsum in range(1,a+1):
    if divsum % 5 == 0:
        numSum += divsum
print(numSum)

# %%
# 310
n = eval(input())
numSum = 0
for times in range(2,n+1): #n=8
    numSum += 1/(((times-1)**0.5)+((times)**0.5))
print('%.4f'%numSum)
    
# %%
# 408
evenCount = 0
for numCount in range(10):
    i = eval(input())
    if i % 2 == 0:
        evenCount += 1
print('Even numbers: %d' %(evenCount))
print('Odd numbers: %d' %(10-evenCount))

# %%
# 402
numList = []
while True:
    n = int(input())
    if n != 9999:
        numList.append(n)
        continue
    else:
        print(min(numList))
        break

# %%
# 504
def compute():
    i = eval(input())
    j = eval(input())
    print('%d' %(i**j))
compute()

# %%
# 506
# x=(-b+(b**2-(4*c*a))**0.5)/(2*a)
# x=(-b-(b**2-(4*c*a))**0.5)/(2*a)
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = b**2-4*a*c
    if proof < 0:
        print('Your equation has no root.')
    elif proof == 0:
        print('%.1f' %(-b/(2*a)))
    else:
        print('%.1f, %.1f' % (((-b+(b**2-(4*c*a))**0.5)/(2*a)),((-b-(b**2-(4*c*a))**0.5)/(2*a))))
compute()

# %%
# 602
cards = []
cardsSum = 0
for i in range(5):
    cards.append(input())
for j in range(5):
    if cards[j] == 'A':
        cardsSum += 1
    elif cards[j] == 'J':
        cardsSum += 11
    elif cards[j] == 'Q':
        cardsSum += 12
    elif cards[j] == 'K':
        cardsSum += 13
    else:
        cardsSum += eval(cards[j])
print(cardsSum)

# %%
# 610
numList = []
for weeks in range(1,5):
    print('Week %d:'%(weeks))
    for days in range(1,4):
        num = eval(input('Day %s:'%(days)))
        numList.append(num)
print('Average: %.2f'%(sum(numList)/12))
print('Highest: %s'%(max(numList)))
print('Lowest: %s'%(min(numList)))

# %%
# 704
numList =set()
while True:
    i = eval(input())
    if i != -9999:
        numList.add(i)
        continue
    else:
        print('Length: %d'%(len(numList)))
        print('Max: %d'%(max(numList)))
        print('Min: %d'%(min(numList)))
        print('Sum: %d'%(sum(numList)))
        break

# %%
# 710
numDict = {}
while True:
    numKey = input('Key: ')
    if numKey != 'end':
        nameValue = input('Value: ')
        numDict = (numKey,nameValue)
        continue
    else:
        findKey = input('Search key: ')
        if findKey in numDict:
            print('True')
        else:
            print('False')
        break

# %%
# 902
#f = open("read.txt")
with open('read.txt') as file:
    content = file.read()
numList = list(map(int,content.split()))
print(sum(numList))

# %%
# 906
f_name = input()
str_old = input()
str_new = input()
#TODO
with open(f_name,'r') as file:
    content = file.read()
print("=== Before the replacement")
#TODO
print(content)
print("=== After the replacement")
#TODO
print(content.replace(str_old,str_new))
# %%

# %%
