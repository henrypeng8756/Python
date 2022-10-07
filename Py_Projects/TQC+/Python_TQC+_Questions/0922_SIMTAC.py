# %%
from curses.ascii import isdigit


x1 = eval(input())
y1 = eval(input())
x2 = eval(input())
y2 = eval(input())
print(f'( {x1} , {y1} )')
print(f'( {x2} , {y2} )')
print('Distance = %.4f' %(((x1-x2)**2+(y1-y2)**2)**0.5))

# %%
num = eval(input())
if num >= 10 and num <= 15:
    hexnum = (str.upper(hex(num))).lstrip('0X')
    print(hexnum)
else:
    print(num)


# %%
numSum = 0
n = eval(input())
for sumTimes in range(2,n+1):
    numSum += 1/((sumTimes-1)**0.5+(sumTimes)**0.5)
print('%.4f'%(numSum))

# %%
oddNum = evenNum = 0
for num in range(10):
    i = eval(input())
    if i % 2 == 0:
        evenNum += 1
    else:
        oddNum += 1
print('Even numbers: %d'%(evenNum))
print('Odd numbers: %d'%(oddNum))

# %%
# -b+((b**2)-(4*a*c))**0.5/(2*a)
def compute():
    a = eval(input())
    b = eval(input())
    c = eval(input())
    proof = (b**2)-(4*a*c)
    if proof < 0:
        print('Your equation has no root.')
    elif proof == 0:
        print('%s'%(-b/(2*a)))
    else:
        print('%s, %s'%((-b+proof**0.5)/(2*a),(-b-proof**0.5)/(2*a)))
compute()

# %%
cardSum = 0
for times in range(5):
    cardNum = input()
    if cardNum == 'A':
        cardSum+=1
    elif cardNum == 'J':
        cardSum+=11
    elif cardNum == 'Q':
        cardSum+=12
    elif cardNum == 'K':
        cardSum+=13
    else:
        cardSum+=int(cardNum)
print(cardSum)
    
            


# %%
numList = set()
while True:
    n = eval(input())
    if n != -9999:
        numList.add(n)
        continue
    else:
        print('Length: %d'%(len(numList)))
        print('Max: %d'%(max(numList)))
        print('Min: %d'%(min(numList)))
        print('Sum: %d'%(sum(numList)))
        break

# %%
sentence = input()
print(sentence.upper())
print(sentence.title())

# %%
fn = 'read.txt'
with open(fn,'r') as file:
    content=file.read()
numSum = int(map(sum,(str(content)).replace(' ',',')))
print(numSum)
# %%
